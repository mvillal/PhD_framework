import torch
import torch.nn as nn
import numpy as np
from src.infrastructure.adapters.models.dsc_model import DSCMethod


class AttentionLayer(nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.attn = nn.Linear(hidden_dim, 1)

    def forward(self, gru_out):
        # gru_out: [batch, seq, hidden]
        weights = torch.softmax(self.attn(gru_out), dim=1)
        # Context vector is weighted sum of hidden states
        context = torch.sum(weights * gru_out, dim=1)
        return context, weights


class JointVAEAttn(nn.Module):
    def __init__(self, input_dim=2, hidden_dim=64, latent_dim=32):
        super().__init__()
        self.encoder = nn.GRU(
            input_dim, hidden_dim, batch_first=True, bidirectional=True
        )
        self.attn = AttentionLayer(hidden_dim * 2)
        self.fc_mu = nn.Linear(hidden_dim * 2, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim * 2, latent_dim)

        self.decoder = nn.GRU(latent_dim, hidden_dim, batch_first=True)
        self.out_y = nn.Linear(hidden_dim, 1)
        self.out_m = nn.Linear(hidden_dim, 1)

    def encode(self, x):
        out, _ = self.encoder(x)
        context, _ = self.attn(out)
        return self.fc_mu(context), self.fc_logvar(context)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z, seq_len):
        z_seq = z.unsqueeze(1).repeat(1, seq_len, 1)
        out, _ = self.decoder(z_seq)
        return self.out_y(out), self.out_m(out)

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        recon_y, recon_m = self.decode(z, x.size(1))
        return recon_y, recon_m, mu, logvar


class DSCTransformer(nn.Module):
    def __init__(
        self, input_dim=2, hidden_dim=64, latent_dim=32, n_heads=4, n_layers=2
    ):
        super().__init__()
        self.embedding = nn.Linear(input_dim, hidden_dim)
        self.pos_encoder = nn.Parameter(
            torch.zeros(1, 1000, hidden_dim)
        )  # Max seq len 1000

        encoder_layers = nn.TransformerEncoderLayer(
            d_model=hidden_dim, nhead=n_heads, batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layers, num_layers=n_layers
        )

        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        self.decoder_embedding = nn.Linear(latent_dim, hidden_dim)
        decoder_layers = nn.TransformerDecoderLayer(
            d_model=hidden_dim, nhead=n_heads, batch_first=True
        )
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layers, num_layers=n_layers
        )

        self.out_y = nn.Linear(hidden_dim, 1)
        self.out_m = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        batch_size, seq_len, _ = x.size()
        x_emb = self.embedding(x) + self.pos_encoder[:, :seq_len, :]
        h = self.transformer_encoder(x_emb)
        # Pool across time for latent
        h_pooled = h.mean(dim=1)
        mu = self.fc_mu(h_pooled)
        logvar = self.fc_logvar(h_pooled)

        std = torch.exp(0.5 * logvar)
        z = mu + torch.randn_like(std) * std

        z_emb = self.decoder_embedding(z).unsqueeze(1).repeat(1, seq_len, 1)
        # For simplicity, self-attention in decoder
        out = self.transformer_decoder(z_emb, h)
        return self.out_y(out), self.out_m(out), mu, logvar


class DSCLatentSDE(nn.Module):
    """
    Simplified Latent SDE using Euler-Maruyama.
    f(z, t) = mu_sde * (theta - z)
    g(z, t) = sigma_sde
    """

    def __init__(self, input_dim=2, hidden_dim=64, latent_dim=32):
        super().__init__()
        self.encoder = nn.GRU(input_dim, hidden_dim, batch_first=True)
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)

        self.drift = nn.Linear(latent_dim, latent_dim)
        self.diffusion = nn.Linear(latent_dim, latent_dim)

        self.out_y = nn.Linear(latent_dim, 1)
        self.out_m = nn.Linear(latent_dim, 1)
        self.latent_dim = latent_dim

    def forward(self, x):
        batch_size, seq_len, _ = x.size()
        _, h = self.encoder(x)
        h = h.squeeze(0)
        mu = self.fc_mu(h)
        logvar = self.fc_logvar(h)

        std = torch.exp(0.5 * logvar)
        z0 = mu + torch.randn_like(std) * std

        # Euler-Maruyama integration
        z = [z0]
        dt = 1.0  # Normalized time step
        for t in range(1, seq_len):
            dz_drift = self.drift(z[-1]) * dt
            dz_diffusion = self.diffusion(z[-1]) * torch.randn_like(z[-1]) * np.sqrt(dt)
            z.append(z[-1] + dz_drift + dz_diffusion)

        z_stack = torch.stack(z, dim=1)  # [batch, seq, latent]
        return self.out_y(z_stack), self.out_m(z_stack), mu, logvar


class DSCVariantWrapper(DSCMethod):
    def __init__(self, variant="attn", **kwargs):
        super().__init__(**kwargs)
        if variant == "attn":
            self.model = JointVAEAttn()
        elif variant == "transformer":
            self.model = DSCTransformer()
        elif variant == "sde":
            self.model = DSCLatentSDE()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)


class BRITS(nn.Module):
    """
    Simplified BRITS implementation.
    """

    def __init__(self, input_dim=1, hidden_dim=64):
        super().__init__()
        self.rnn_f = nn.LSTMCell(input_dim * 2, hidden_dim)  # [y, m]
        self.rnn_b = nn.LSTMCell(input_dim * 2, hidden_dim)
        self.out_y = nn.Linear(hidden_dim * 2, input_dim)
        self.hidden_dim = hidden_dim

    def forward(self, x):
        batch_size, seq_len, _ = x.size()
        h_f = torch.zeros(batch_size, self.hidden_dim)
        c_f = torch.zeros(batch_size, self.hidden_dim)
        h_b = torch.zeros(batch_size, self.hidden_dim)
        c_b = torch.zeros(batch_size, self.hidden_dim)

        outputs_f = []
        for t in range(seq_len):
            xt = x[:, t, :]
            h_f, c_f = self.rnn_f(xt, (h_f, c_f))
            outputs_f.append(h_f)

        outputs_b = []
        for t in range(seq_len - 1, -1, -1):
            xt = x[:, t, :]
            h_b, c_b = self.rnn_b(xt, (h_b, c_b))
            outputs_b.append(h_b)
        outputs_b.reverse()

        h_cat = torch.cat(
            [torch.stack(outputs_f, dim=1), torch.stack(outputs_b, dim=1)], dim=-1
        )
        recon_y = self.out_y(h_cat)
        # BRITS dummy M reconstruction (not really used in original BRITS for the same purpose)
        recon_m = torch.zeros_like(recon_y)
        return recon_y, recon_m, torch.zeros(batch_size, 1), torch.zeros(batch_size, 1)


class NeuralCDE(nn.Module):
    """
    Simplified Neural CDE inspired architecture.
    """

    def __init__(self, input_dim=2, hidden_dim=64):
        super().__init__()
        self.func = nn.Sequential(
            nn.Linear(hidden_dim, 128),
            nn.ReLU(),
            nn.Linear(128, hidden_dim * input_dim),
        )
        self.initial = nn.Linear(input_dim, hidden_dim)
        self.readout = nn.Linear(hidden_dim, 1)
        self.hidden_dim = hidden_dim
        self.input_dim = input_dim

    def forward(self, x):
        batch_size, seq_len, _ = x.size()
        h = self.initial(x[:, 0, :])

        outputs = [self.readout(h)]
        for t in range(1, seq_len):
            dx = x[:, t, :] - x[:, t - 1, :]
            f_h = self.func(h).view(batch_size, self.hidden_dim, self.input_dim)
            dh = torch.bmm(f_h, dx.unsqueeze(-1)).squeeze(-1)
            h = h + dh
            outputs.append(self.readout(h))

        recon_y = torch.stack(outputs, dim=1)
        return (
            recon_y,
            torch.zeros_like(recon_y),
            torch.zeros(batch_size, 1),
            torch.zeros(batch_size, 1),
        )


class MRNN(nn.Module):
    def __init__(self, input_dim=2, hidden_dim=64):
        super().__init__()
        self.rnn = nn.GRU(input_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.out = nn.Linear(hidden_dim * 2, 1)

    def forward(self, x):
        out, _ = self.rnn(x)
        recon_y = self.out(out)
        return (
            recon_y,
            torch.zeros_like(recon_y),
            torch.zeros(x.size(0), 1),
            torch.zeros(x.size(0), 1),
        )


class CSDILite(nn.Module):
    def __init__(self, input_dim=2, hidden_dim=64):
        super().__init__()
        self.embedding = nn.Linear(input_dim, hidden_dim)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_dim, nhead=4, batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=2)
        self.out = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        h = self.embedding(x)
        h = self.transformer(h)
        recon_y = self.out(h)
        return (
            recon_y,
            torch.zeros_like(recon_y),
            torch.zeros(x.size(0), 1),
            torch.zeros(x.size(0), 1),
        )


class BaselineWrapper(DSCMethod):
    def __init__(self, method="brits", **kwargs):
        super().__init__(**kwargs)
        if method == "brits":
            self.model = BRITS()
        elif method == "ncde":
            self.model = NeuralCDE()
        elif method == "mrnn":
            self.model = MRNN()
        elif method == "csdi":
            self.model = CSDILite()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)
