import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from src.domain.experiment.interfaces import ImputationModel


class SDEFunction(nn.Module):
    def __init__(self, latent_dim, hidden_dim):
        super().__init__()
        self.f = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, latent_dim),
        )
        self.g = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.Softplus(),
            nn.Linear(hidden_dim, latent_dim),
        )

    def forward(self, t, y):
        # We don't use t explicitly here but it's part of the SDE signature
        return self.f(y), self.g(y)


class SDEDecoder(nn.Module):
    def __init__(self, latent_dim, hidden_dim):
        super().__init__()
        self.sde_func = SDEFunction(latent_dim, hidden_dim)
        self.out_y = nn.Linear(latent_dim, 1)
        self.out_m = nn.Linear(latent_dim, 1)

    def forward(self, z0, seq_len, dt=0.5):
        z = z0
        zs = [z]
        for t_idx in range(1, seq_len):
            f, g = self.sde_func(t_idx * dt, z)
            dw = torch.randn_like(z) * np.sqrt(dt)
            z = z + f * dt + g * dw
            zs.append(z)

        zs = torch.stack(zs, dim=1)  # (batch, seq_len, latent_dim)
        return self.out_y(zs), self.out_m(zs)


class DSCSDEModel(nn.Module):
    def __init__(self, input_dim=2, hidden_dim=64, latent_dim=32):
        super().__init__()
        self.encoder = nn.GRU(
            input_dim, hidden_dim, batch_first=True, bidirectional=True
        )
        self.fc_mu = nn.Linear(hidden_dim * 2, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim * 2, latent_dim)
        self.decoder = SDEDecoder(latent_dim, hidden_dim)

    def encode(self, x):
        _, h = self.encoder(x)
        h = torch.cat([h[0], h[1]], dim=1)
        return self.fc_mu(h), self.fc_logvar(h)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        mu, logvar = self.encode(x)
        z0 = self.reparameterize(mu, logvar)
        recon_y, recon_m = self.decoder(z0, x.size(1))
        return recon_y, recon_m, mu, logvar


class DSCSDE(ImputationModel):
    def __init__(self, epochs=30, lr=1e-3, batch_size=32, latent_dim=32):
        self.epochs = epochs
        self.lr = lr
        self.batch_size = batch_size
        self.latent_dim = latent_dim
        self.model = DSCSDEModel(latent_dim=latent_dim)
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
