import numpy as np
import pandas as pd
import os


def generate_sdpc_2026(
    n_patients: int = 100,
    n_days: int = 60,
    dt: float = 0.5,  # Half-day intervals
    mu: float = -0.1,
    sigma: float = 0.15,
    lambda_jump: float = 0.05,
    mu_jump: float = -0.8,  # Deeper, more distinct crises
    sigma_jump: float = 0.2,
    beta_0: float = -1.5,  # Hardened base missingness
    beta_s: float = -5.0,  # Aggressive MNAR effect
    p_persistence: float = 0.95,  # Extreme persistence to kill interpolation
    seed: int = 42,
    seasonal_amplitude: float = 0.3,
    tech_reliability_range: tuple = (0.01, 0.2),
) -> pd.DataFrame:
    """
    Generates synthetic longitudinal trajectories for psychiatric states
    using a Jump-Diffusion process and Persistent MNAR mechanism.

    Hardened for certification-level benchmarks where simple interpolation must fail.
    """
    np.random.seed(seed)
    n_steps = int(n_days / dt)
    times = np.linspace(0, n_days, n_steps)

    all_data = []

    for patient_id in range(n_patients):
        S = np.zeros(n_steps)
        S[0] = np.random.uniform(0.7, 1.3)  # Start in healthy range

        tech_noise = np.random.uniform(*tech_reliability_range)
        device_quality = np.random.uniform(0.1, 1.0)
        p_tech_dropout = 0.05 * (1.0 - device_quality)

        # Seasonal drift component
        drift = seasonal_amplitude * (
            np.cos(2 * np.pi * times / 365.0) + 0.5 * np.sin(4 * np.pi * times / 365.0)
        )

        for t in range(1, n_steps):
            target = 1.0 + drift[t]
            dW = np.random.normal(0, np.sqrt(dt))
            # Ornstein-Uhlenbeck
            dS_diffusion = mu * (S[t - 1] - target) * dt + sigma * dW

            # Poisson Jump (Crises)
            dN = np.random.poisson(lambda_jump * dt)
            jump = 0
            if dN > 0:
                jump = np.random.normal(mu_jump, sigma_jump)

            S[t] = S[t - 1] + dS_diffusion + jump
            S[t] = max(-1.0, min(2.0, S[t]))  # Broader range for crisis

        Y_star = S + np.random.normal(0, tech_noise, n_steps)

        # Persistent MNAR mechanism
        M = np.zeros(n_steps, dtype=int)
        for t in range(n_steps):
            # Sigmoid(S) mapped to missingness
            # If S is low (crisis), logits is high (missing)
            logits = beta_0 + beta_s * (S[t] - 0.5)
            prob_mnar = 1 / (1 + np.exp(-logits))
            prob_init = 1 - (1 - prob_mnar) * (1 - p_tech_dropout)

            if t > 0 and M[t - 1] == 1:
                # Disengaged patients STAY disengaged during crisis
                M[t] = np.random.binomial(
                    1, p_persistence + (1 - p_persistence) * prob_init
                )
            else:
                M[t] = np.random.binomial(1, prob_init)

        Y_obs = Y_star.copy()
        Y_obs[M == 1] = np.nan

        patient_df = pd.DataFrame(
            {
                "patient_id": patient_id,
                "time": times,
                "S_true": S,
                "Y_star": Y_star,
                "M": M,
                "Y_obs": Y_obs,
                "tech_reliability": tech_noise,
                "device_quality": device_quality,
            }
        )
        all_data.append(patient_df)

    return pd.concat(all_data, ignore_index=True)


if __name__ == "__main__":
    output_path = "data/sdpc_2026_synthetic.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = generate_sdpc_2026(n_patients=1000, n_days=60)
    df.to_csv(output_path, index=False)
    print(f"Generated Hardened Certification Set at {output_path}")
    print(f"Missingness rate: {df['M'].mean():.2%}")
