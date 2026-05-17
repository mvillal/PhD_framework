import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from src.domain.experiment.interfaces import ImputationModel


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * (-np.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe.unsqueeze(0))

    def forward(self, x):
        return x + self.pe[:, : x.size(1)]


class CrossAttention(nn.Module):
    def __init__(self, d_model, nhead):
        super().__init__()
        self.multihead_attn = nn.MultiheadAttention(d_model, nhead, batch_first=True)
        self.norm = nn.LayerNorm(d_model)

    def forward(self, query, key, value):
        attn_output, _ = self.multihead_attn(query, key, value)
        return self.norm(query + attn_output)


class AttentionWeightedSDEFunction(nn.Module):
    def __init__(self, latent_dim, context_dim, hidden_dim, nhead=2):
        super().__init__()
        self.latent_to_context = nn.Linear(latent_dim, context_dim)
        self.attention = CrossAttention(context_dim, nhead)
        self.f = nn.Sequential(
            nn.Linear(latent_dim + context_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim),
        )
        self.g = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.Softplus(),
            nn.Linear(hidden_dim, latent_dim),
        )

    def forward(self, t, z, memory):
        z_query = self.latent_to_context(z).unsqueeze(1)
        attn_context = self.attention(z_query, memory, memory).squeeze(1)
        feat = torch.cat([z, attn_context], dim=-1)
        return self.f(feat), self.g(z)


class LatentSDETransformer(nn.Module):
    def __init__(
        self,
        input_dim=2,
        d_model=64,
        nhead=4,
        num_layers=2,
        latent_dim=32,
        hidden_dim=64,
    ):
        super().__init__()
        self.input_fc = nn.Linear(input_dim, d_model)
        self.pos_encoder = PositionalEncoding(d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead, batch_first=True, norm_first=True, dropout=0.1
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers
        )
        self.fc_mu = nn.Linear(d_model, latent_dim)
        self.fc_logvar = nn.Linear(d_model, latent_dim)
        self.sde_func = AttentionWeightedSDEFunction(
            latent_dim, d_model, hidden_dim, nhead=nhead
        )
        self.out_y = nn.Linear(latent_dim, 1)
        self.out_m = nn.Linear(latent_dim, 1)

    def encode(self, x):
        src = self.input_fc(x)
        src = self.pos_encoder(src)
        memory = self.transformer_encoder(src)
        terminal_state = memory[:, -1, :]
        return self.fc_mu(terminal_state), self.fc_logvar(terminal_state), memory

    def reparameterize(self, mu, logvar):
        if self.training:
            std = torch.exp(0.5 * logvar)
            eps = torch.randn_like(std)
            return mu + eps * std
        return mu

    def decode(self, z0, memory, seq_len, dt=0.5):
        z = z0
        zs = [z]
        for t_idx in range(1, seq_len):
            f, g = self.sde_func(t_idx * dt, z, memory)
            z = z + f * dt + g * (torch.randn_like(z) * np.sqrt(dt))
            zs.append(z)
        zs = torch.stack(zs, dim=1)
        return self.out_y(zs), self.out_m(zs), zs

    def forward(self, x):
        mu, logvar, memory = self.encode(x)
        z = self.reparameterize(mu, logvar)
        recon_y, recon_m, latent_traj = self.decode(z, memory, x.size(1))
        return recon_y, recon_m, mu, logvar, latent_traj


class DSCMethod(ImputationModel):
    def __init__(
        self, epochs=40, lr=1e-3, batch_size=64, latent_dim=32, causal_lambda=15.0
    ):
        self.epochs = epochs
        self.lr = lr
        self.batch_size = batch_size
        self.causal_lambda = causal_lambda
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = LatentSDETransformer(latent_dim=latent_dim).to(self.device)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        self.mean_y = 0.0
        self.std_y = 1.0

    def _prepare_data(self, df):
        df_sorted = df.sort_values(["patient_id", "time"])
        patients = df_sorted["patient_id"].unique()
        seq_len = len(df_sorted["time"].unique())
        y_obs = (df_sorted["Y_obs"].fillna(0).values - self.mean_y) / (
            self.std_y + 1e-6
        )
        X = np.stack([y_obs, df_sorted["M"].values], axis=1).reshape(
            len(patients), seq_len, 2
        )
        return torch.tensor(X, dtype=torch.float32).to(self.device)

    def fit(self, df: pd.DataFrame) -> None:
        self.mean_y = df["Y_obs"].mean()
        self.std_y = df["Y_obs"].std() if df["Y_obs"].std() > 0 else 1.0
        X = self._prepare_data(df)
        dataset = torch.utils.data.TensorDataset(X)
        loader = torch.utils.data.DataLoader(
            dataset, batch_size=self.batch_size, shuffle=True
        )
        self.model.train()
        for epoch in range(self.epochs):
            total_loss = 0
            for (x_batch,) in loader:
                self.optimizer.zero_grad()
                ry, rm, mu, lv, _ = self.model(x_batch)
                mask = 1 - x_batch[:, :, 1:2]
                ry_loss = ((ry - x_batch[:, :, 0:1]) ** 2 * mask).sum() / (
                    mask.sum() + 1e-6
                )
                bce_loss = nn.functional.binary_cross_entropy_with_logits(
                    rm, x_batch[:, :, 1:2]
                )
                kl = -0.5 * torch.sum(1 + lv - mu.pow(2) - lv.exp()) / x_batch.size(0)
                m_prob = torch.sigmoid(rm)
                fid = torch.mean(m_prob * (ry - (-2.0)) ** 2)
                loss = ry_loss + 1.0 * bce_loss + 0.1 * kl + self.causal_lambda * fid
                loss.backward()
                self.optimizer.step()
                total_loss += loss.item()
            if (epoch + 1) % 10 == 0:
                print(
                    f"Epoch {epoch + 1}/{self.epochs}, Loss: {total_loss / len(loader):.4f}"
                )

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        self.model.eval()
        X = self._prepare_data(df)
        with torch.no_grad():
            ry, rm, _, _, _ = self.model(X)
        ry_np = (ry.cpu().numpy() * self.std_y + self.mean_y).flatten()
        df_out = df.copy()
        df_out["Y_imputed"] = df_out["Y_obs"].copy()
        mask = df_out["Y_obs"].isna().values
        df_out.loc[mask, "Y_imputed"] = ry_np[mask]
        df_out["M_prob"] = torch.sigmoid(rm).cpu().numpy().flatten()
        return df_out
