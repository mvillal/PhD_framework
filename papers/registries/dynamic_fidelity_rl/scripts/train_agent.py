import os
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from rl_environment import PsychiatricPOMDPEnv
from fidelity_controller import DynamicFidelityController


class PolicyNet(nn.Module):
    """A simple Policy Network for the REINFORCE algorithm."""

    def __init__(self, input_dim=3, hidden_dim=16, output_dim=2):
        super(PolicyNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return self.softmax(x)


def train(constrained=True, num_episodes=100):
    RESULTS_DIR = "../results"
    os.makedirs(RESULTS_DIR, exist_ok=True)

    env = PsychiatricPOMDPEnv(horizon_days=10)  # 40 steps per episode
    policy = PolicyNet()
    optimizer = optim.Adam(policy.parameters(), lr=0.01)

    # Safe baseline policy: 50/50 uniform random exploration
    safe_baseline = np.array([0.5, 0.5])

    training_log = []

    for episode in range(num_episodes):
        controller = DynamicFidelityController(window_size=20, ess_threshold=0.7)
        obs, _ = env.reset()

        log_probs = []
        rewards = []

        done = False
        while not done:
            obs_tensor = torch.FloatTensor(obs).unsqueeze(0)
            probs = policy(obs_tensor)

            # Sample action
            dist = torch.distributions.Categorical(probs)
            action = dist.sample()

            log_prob = dist.log_prob(action)
            action_item = action.item()

            # Update fidelity controller
            pi_e_dist = probs.squeeze(0).detach().numpy()
            controller.update(
                pi_e_prob=pi_e_dist[action_item], pi_b_prob=safe_baseline[action_item]
            )

            # Step environment
            next_obs, env_reward, done, info = env.step(action_item)

            # Calculate penalty if constrained
            fidelity_penalty = 0.0
            if constrained:
                # Strong penalty lambda to aggressively correct deviation
                fidelity_penalty = controller.get_fidelity_penalty(
                    pi_e_dist, safe_baseline, lambda_penalty=10.0
                )

            total_reward = env_reward + fidelity_penalty

            log_probs.append(log_prob)
            rewards.append(total_reward)
            obs = next_obs

        # Update policy (REINFORCE)
        discounted_rewards = []
        R = 0
        for r in rewards[::-1]:
            R = r + 0.99 * R
            discounted_rewards.insert(0, R)

        discounted_rewards = torch.FloatTensor(discounted_rewards)
        # Normalize rewards for stability
        if discounted_rewards.std() > 0:
            discounted_rewards = (discounted_rewards - discounted_rewards.mean()) / (
                discounted_rewards.std() + 1e-8
            )
        else:
            discounted_rewards = discounted_rewards - discounted_rewards.mean()

        loss = []
        for log_prob, r in zip(log_probs, discounted_rewards):
            loss.append(-log_prob * r)

        loss = torch.cat(loss).sum()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        ep_reward = sum(rewards)
        ess = controller.compute_ess()

        training_log.append({"episode": episode + 1, "reward": ep_reward, "ess": ess})

        if (episode + 1) % 20 == 0:
            mode = "CONSTRAINED" if constrained else "UNCONSTRAINED"
            print(
                f"[{mode}] Ep {episode + 1:03d}/{num_episodes} | Total Reward: {ep_reward:+.3f} | Final ESS: {ess:05.2f}/20.0"
            )

    # Save results to CSV for traceability
    mode_str = "constrained" if constrained else "unconstrained"
    df = pd.DataFrame(training_log)
    csv_path = os.path.join(RESULTS_DIR, f"training_log_{mode_str}.csv")
    df.to_csv(csv_path, index=False)
    print(f"Training results saved to {csv_path}")


if __name__ == "__main__":
    # Ensure reproducibility
    torch.manual_seed(42)
    np.random.seed(42)

    # Set working directory to this script's location
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("--- Training UNCONSTRAINED Agent (Prone to Adaptivity Trap) ---")
    train(constrained=False, num_episodes=100)

    print("\n--- Training CONSTRAINED Agent (Dynamic Fidelity) ---")
    train(constrained=True, num_episodes=100)
