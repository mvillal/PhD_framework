import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import torch
import torch.nn as nn
import torch.optim as optim
from rl_environment import PsychiatricPOMDPEnv
from fidelity_controller import DynamicFidelityController

sns.set_theme(style="whitegrid")
OUTPUT_DIR = "../plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)


class PolicyNet(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=16, output_dim=2):
        super(PolicyNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.softmax(self.fc2(x))


def train_and_evaluate(mode="dynamic", num_episodes=200, seed=42):
    torch.manual_seed(seed)
    np.random.seed(seed)

    env = PsychiatricPOMDPEnv(horizon_days=10)  # 40 steps
    policy = PolicyNet()
    optimizer = optim.Adam(policy.parameters(), lr=0.01)
    safe_baseline = np.array([0.5, 0.5])

    final_rewards = []
    final_ess = []
    final_missing = []

    for episode in range(num_episodes):
        controller = DynamicFidelityController(window_size=20, ess_threshold=0.7)
        obs, _ = env.reset()

        log_probs = []
        rewards = []
        missing_count = 0

        done = False
        while not done:
            obs_tensor = torch.FloatTensor(obs).unsqueeze(0)
            probs = policy(obs_tensor)

            if mode == "random":
                action_item = np.random.choice([0, 1])
                log_prob = torch.tensor(0.0)  # Dummy
            else:
                dist = torch.distributions.Categorical(probs)
                action = dist.sample()
                log_prob = dist.log_prob(action)
                action_item = action.item()

            pi_e_dist = (
                probs.squeeze(0).detach().numpy() if mode != "random" else safe_baseline
            )
            controller.update(
                pi_e_prob=pi_e_dist[action_item], pi_b_prob=safe_baseline[action_item]
            )

            next_obs, env_reward, done, info = env.step(action_item)
            if info["was_missing"]:
                missing_count += 1

            fidelity_penalty = 0.0
            if mode == "dynamic":
                fidelity_penalty = controller.get_fidelity_penalty(
                    pi_e_dist, safe_baseline, lambda_penalty=10.0
                )
            elif mode == "static":
                # Static KL penalty regardless of ESS
                pi_e_safe = np.clip(pi_e_dist, 1e-8, 1.0)
                pi_safe_safe = np.clip(safe_baseline, 1e-8, 1.0)
                kl_div = np.sum(pi_e_safe * np.log(pi_e_safe / pi_safe_safe))
                fidelity_penalty = -10.0 * kl_div

            total_reward = env_reward + fidelity_penalty

            if mode != "random":
                log_probs.append(log_prob)
            rewards.append(total_reward)
            obs = next_obs

        if mode != "random":
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

        final_rewards.append(sum(rewards))
        final_ess.append(controller.compute_ess())
        final_missing.append(missing_count)

    # Return average over the last 50 episodes
    return {
        "Reward": np.mean(final_rewards[-50:]),
        "ESS": np.mean(final_ess[-50:]),
        "Missingness Rate": np.mean(final_missing[-50:]) / 40.0,
    }


def run_comparisons():
    print("Running Baseline Comparisons...")
    modes = ["random", "unconstrained", "static", "dynamic"]
    results = []

    for mode in modes:
        print(f"Training {mode}...")
        metrics = {"Reward": [], "ESS": [], "Missingness Rate": []}
        for seed in [42, 100, 2024]:
            res = train_and_evaluate(mode=mode, num_episodes=200, seed=seed)
            for k in metrics:
                metrics[k].append(res[k])

        results.append(
            {
                "Policy": mode.capitalize(),
                "Reward": np.mean(metrics["Reward"]),
                "Reward_std": np.std(metrics["Reward"]),
                "ESS": np.mean(metrics["ESS"]),
                "ESS_std": np.std(metrics["ESS"]),
                "Missingness": np.mean(metrics["Missingness Rate"]),
                "Missingness_std": np.std(metrics["Missingness Rate"]),
            }
        )

    df = pd.DataFrame(results)
    print("\n--- Final Metrics ---")
    print(df)

    # Plotting
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    sns.barplot(x="Policy", y="Reward", data=df, ax=axes[0], capsize=0.1, errorbar=None)
    axes[0].errorbar(
        x=range(len(df)),
        y=df["Reward"],
        yerr=df["Reward_std"],
        fmt="none",
        c="black",
        capsize=5,
    )
    axes[0].set_title("Average Proximal Reward")
    axes[0].set_ylabel("Reward")

    sns.barplot(x="Policy", y="ESS", data=df, ax=axes[1], capsize=0.1, errorbar=None)
    axes[1].errorbar(
        x=range(len(df)),
        y=df["ESS"],
        yerr=df["ESS_std"],
        fmt="none",
        c="black",
        capsize=5,
    )
    axes[1].axhline(y=14.0, color="r", linestyle="--", label="Critical Threshold (14)")
    axes[1].set_title("Effective Sample Size (ESS)")
    axes[1].set_ylabel("ESS (Max 20)")
    axes[1].legend()

    sns.barplot(
        x="Policy", y="Missingness", data=df, ax=axes[2], capsize=0.1, errorbar=None
    )
    axes[2].errorbar(
        x=range(len(df)),
        y=df["Missingness"],
        yerr=df["Missingness_std"],
        fmt="none",
        c="black",
        capsize=5,
    )
    axes[2].set_title("Informative Missingness Rate")
    axes[2].set_ylabel("Missingness Ratio")

    plt.tight_layout()
    plot_path = os.path.join(OUTPUT_DIR, "baseline_comparisons.png")
    plt.savefig(plot_path, dpi=300)
    plt.close()
    print(f"\nSaved {plot_path}")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run_comparisons()
