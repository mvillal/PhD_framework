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


class TransformerVAE(nn.Module):
    def __init__(self, input_dim=2, d_model=64, nhead=4, num_layers=2, latent_dim=32):
        super().__init__()
        self.input_fc = nn.Linear(input_dim, d_model)
        self.pos_encoder = PositionalEncoding(d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead, batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers
        )

        self.fc_mu = nn.Linear(d_model, latent_dim)
        self.fc_logvar = nn.Linear(d_model, latent_dim)

        self.latent_to_dmodel = nn.Linear(latent_dim, d_model)
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model, nhead=nhead, batch_first=True
        )
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layer, num_layers=num_layers
        )

        self.out_y = nn.Linear(d_model, 1)
        self.out_m = nn.Linear(d_model, 1)

    def encode(self, x):
        x = self.input_fc(x)
        x = self.pos_encoder(x)
        out = self.transformer_encoder(x)
        # Global average pooling over time for the bottleneck
        pooled = out.mean(dim=1)
        return self.fc_mu(pooled), self.fc_logvar(pooled)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z, seq_len):
        z_projected = self.latent_to_dmodel(z).unsqueeze(1).repeat(1, seq_len, 1)
        z_projected = self.pos_encoder(z_projected)
        # Using the latent vector as memory for the decoder
        out = self.transformer_decoder(z_projected, z_projected)
        return self.out_y(out), self.out_m(out)

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        recon_y, recon_m = self.decode(z, x.size(1))
        return recon_y, recon_m, mu, logvar


class DSCTransformer(ImputationModel):
    def __init__(self, epochs=30, lr=1e-3, batch_size=32, latent_dim=32):
        self.epochs = epochs
        self.lr = lr
        self.batch_size = batch_size
        self.latent_dim = latent_dim
        self.model = TransformerVAE(latent_dim=latent_dim)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        self.mean_y = 0.0
        self.std_y = 1.0

    def _prepare_data(self, df):
        patients = sorted(df["patient_id"].unique())
        sequences = []
        for p in patients:
            p_data = df[df["patient_id"] == p]
            y_obs = (p_data["Y_obs"].fillna(0).values - self.mean_y) / self.std_y
            m = p_data["M"].values
            seq = np.stack([y_obs, m], axis=1)
            sequences.append(seq)
        return torch.tensor(np.array(sequences), dtype=torch.float32)

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
            for batch in loader:
                x_batch = batch[0]
                self.optimizer.zero_grad()
                recon_y, recon_m, mu, logvar = self.model(x_batch)

                mask = 1 - x_batch[:, :, 1:2]
                y_true = x_batch[:, :, 0:1]
                mse = (recon_y - y_true) ** 2
                recon_y_loss = (mse * mask).sum() / (mask.sum() + 1e-6)

                m_true = x_batch[:, :, 1:2]
                bce_loss = nn.functional.binary_cross_entropy_with_logits(
                    recon_m, m_true
                )

                kl_loss = (
                    -0.5
                    * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
                    / x_batch.size(0)
                )

                loss = recon_y_loss + 0.5 * bce_loss + 0.01 * kl_loss
                loss.backward()
                self.optimizer.step()
                total_loss += loss.item()

            if (epoch + 1) % 20 == 0:
                print(
                    f"Epoch {epoch + 1}/{self.epochs}, Loss: {total_loss / len(loader):.4f}"
                )

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        self.model.eval()
        X = self._prepare_data(df)
        with torch.no_grad():
            recon_y, recon_m, _, _ = self.model(X)

        recon_y = recon_y.numpy() * self.std_y + self.mean_y
        df_out = df.copy()
        recon_flat = recon_y.flatten()
        df_out["Y_imputed"] = df_out["Y_obs"].copy()
        mask = df_out["Y_obs"].isna()
        df_out.loc[mask, "Y_imputed"] = recon_flat[mask.values]
        return df_out
