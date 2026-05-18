import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from synthetic_cohort import SyntheticCohortGenerator
import torch
import torch.nn as nn
import torch.optim as optim
from rl_environment import PsychiatricPOMDPEnv
from fidelity_controller import DynamicFidelityController

# Setup plot styling
sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.size": 12})

OUTPUT_DIR = "../plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_patient_trajectory():
    """Generates a plot of a single patient's trajectory showing HMM phases and MNAR."""
    print("Generating Patient Trajectory Plot...")
    generator = SyntheticCohortGenerator(
        num_patients=1, horizon_days=45, steps_per_day=4
    )
    df = generator.generate_patient(0)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Background shading for HMM Phase
    for step in range(len(df)):
        if df.loc[step, "hmm_phase"] == 1:
            ax1.axvspan(
                df.loc[step, "day"],
                df.loc[step, "day"] + 0.25,
                color="red",
                alpha=0.1,
                lw=0,
            )
            ax2.axvspan(
                df.loc[step, "day"],
                df.loc[step, "day"] + 0.25,
                color="red",
                alpha=0.1,
                lw=0,
            )

    # Plot 1: Latent Severity vs Observed EMA
    ax1.plot(
        df["day"],
        df["latent_severity"],
        label="True Latent Severity",
        color="blue",
        alpha=0.7,
    )

    # Plot observed EMA points (handling NaNs)
    observed = df[~df["is_missing"]]
    ax1.scatter(
        observed["day"],
        observed["observed_ema"],
        color="black",
        marker="x",
        label="Observed EMA",
        zorder=5,
    )

    missing = df[df["is_missing"]]
    ax1.scatter(
        missing["day"],
        [0] * len(missing),
        color="red",
        marker="|",
        s=100,
        label="Missing EMA (MNAR)",
        zorder=5,
    )

    ax1.set_ylabel("Severity [0, 1]")
    ax1.set_title(
        "Psychiatric Trajectory with Informative Missingness and Crisis Phases"
    )
    ax1.legend(loc="upper left")

    # Plot 2: Volatility
    ax2.plot(
        df["day"], df["latent_volatility"], label="Latent Volatility", color="orange"
    )
    ax2.set_xlabel("Time (Days)")
    ax2.set_ylabel("Volatility")
    ax2.legend(loc="upper left")

    plt.tight_layout()
    plot_path = os.path.join(OUTPUT_DIR, "patient_trajectory.png")
    plt.savefig(plot_path, dpi=300)
    plt.close()
    print(f"Saved {plot_path}")


class PolicyNet(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=16, output_dim=2):
        super(PolicyNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.softmax(self.fc2(x))


def simulate_training_ess(num_episodes=150):
    """Runs a simplified training loop to capture ESS over time for constrained vs unconstrained."""
    print("Simulating ESS Dynamics during Training...")

    def run_training(constrained):
        env = PsychiatricPOMDPEnv(horizon_days=5)  # Short horizon for fast simulation
        policy = PolicyNet()
        optimizer = optim.Adam(policy.parameters(), lr=0.01)
        safe_baseline = np.array([0.5, 0.5])

        ess_history = []
        reward_history = []

        for episode in range(num_episodes):
            controller = DynamicFidelityController(window_size=20, ess_threshold=0.7)
            obs, _ = env.reset()
            log_probs = []
            rewards = []

            done = False
            while not done:
                obs_tensor = torch.FloatTensor(obs).unsqueeze(0)
                probs = policy(obs_tensor)
                dist = torch.distributions.Categorical(probs)
                action = dist.sample()
                log_prob = dist.log_prob(action)

                pi_e_dist = probs.squeeze(0).detach().numpy()
                controller.update(
                    pi_e_prob=pi_e_dist[action.item()],
                    pi_b_prob=safe_baseline[action.item()],
                )

                next_obs, env_reward, done, _ = env.step(action.item())

                fidelity_penalty = 0.0
                if constrained:
                    fidelity_penalty = controller.get_fidelity_penalty(
                        pi_e_dist, safe_baseline, lambda_penalty=10.0
                    )

                rewards.append(env_reward + fidelity_penalty)
                log_probs.append(log_prob)
                obs = next_obs

            discounted_rewards = []
            R = 0
            for r in rewards[::-1]:
                R = r + 0.99 * R
                discounted_rewards.insert(0, R)
            discounted_rewards = torch.FloatTensor(discounted_rewards)
            if discounted_rewards.std() > 0:
                discounted_rewards = (
                    discounted_rewards - discounted_rewards.mean()
                ) / (discounted_rewards.std() + 1e-8)
            else:
                discounted_rewards = discounted_rewards - discounted_rewards.mean()

            loss = torch.cat(
                [-lp * r for lp, r in zip(log_probs, discounted_rewards)]
            ).sum()
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            ess_history.append(controller.compute_ess())
            reward_history.append(sum(rewards))

        return ess_history, reward_history

    ess_unconstrained, _ = run_training(constrained=False)
    ess_constrained, _ = run_training(constrained=True)

    # Plotting ESS
    plt.figure(figsize=(10, 6))

    # Apply rolling mean for smooth plotting
    window = 10
    ess_unc_smooth = pd.Series(ess_unconstrained).rolling(window, min_periods=1).mean()
    ess_con_smooth = pd.Series(ess_constrained).rolling(window, min_periods=1).mean()

    plt.plot(ess_unc_smooth, label="Unconstrained Agent", color="red", lw=2)
    plt.plot(
        ess_con_smooth, label="Dynamic Fidelity-Constrained Agent", color="green", lw=2
    )
    plt.axhline(
        y=14.0,
        color="black",
        linestyle="--",
        label="Critical Fidelity Threshold (ESS=14)",
    )

    plt.title("Algorithm Fidelity (Effective Sample Size) During Live Deployment")
    plt.xlabel("Training Episode")
    plt.ylabel("Terminal Effective Sample Size (Window=20)")
    plt.legend()
    plt.ylim(0, 21)

    plot_path = os.path.join(OUTPUT_DIR, "ess_comparison.png")
    plt.savefig(plot_path, dpi=300)
    plt.close()
    print(f"Saved {plot_path}")


if __name__ == "__main__":
    np.random.seed(42)
    torch.manual_seed(42)

    # Set working directory to this script's location so imports work cleanly
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    plot_patient_trajectory()
    simulate_training_ess()
    print("\nAll plots generated successfully.")
