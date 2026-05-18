import numpy as np
import d3rlpy
from d3rlpy.dataset import MDPDataset
from rl_environment import PsychiatricPOMDPEnv


def generate_offline_dataset(num_episodes=500):
    """
    Generates a static historical dataset using a sub-optimal "Clinician" baseline policy.
    This simulates retrospective data collected before an RL agent is deployed.
    """
    env = PsychiatricPOMDPEnv(horizon_days=10)  # 40 steps per episode

    observations = []
    actions = []
    rewards = []
    terminals = []

    for _ in range(num_episodes):
        obs, _ = env.reset()
        done = False

        while not done:
            observations.append(obs)

            # Simulated Clinician Policy:
            # Intervenes (~70% of the time) if EMA is high, otherwise 30% of the time.
            if obs[0] > 0.6:
                action = np.random.choice([0, 1], p=[0.3, 0.7])
            else:
                action = np.random.choice([0, 1], p=[0.7, 0.3])

            actions.append(action)

            obs, reward, done, _ = env.step(action)
            rewards.append(reward)
            terminals.append(1 if done else 0)

    # Create d3rlpy MDPDataset
    dataset = MDPDataset(
        observations=np.array(observations, dtype=np.float32),
        actions=np.array(actions, dtype=np.int32),
        rewards=np.array(rewards, dtype=np.float32),
        terminals=np.array(terminals, dtype=np.float32),
    )

    return dataset


def train_and_evaluate_offline_rl():
    import os
    import pandas as pd

    RESULTS_DIR = "../results"
    os.makedirs(RESULTS_DIR, exist_ok=True)

    print("Generating synthetic historical dataset (MIMIC/eICU style)...")
    dataset = generate_offline_dataset(num_episodes=1000)

    print(f"Dataset generated with {len(dataset.episodes)} episodes.")

    # Initialize Conservative Q-Learning (CQL) - State-of-the-Art Offline RL
    # CQL penalizes Out-Of-Distribution (OOD) actions, enforcing a form of algorithm fidelity.
    cql = d3rlpy.algos.DiscreteCQLConfig(
        learning_rate=1e-3, target_update_interval=100
    ).create()

    print("\nTraining CQL Offline Agent...")
    # Train the agent purely on the offline dataset
    cql.fit(dataset, n_steps=5000, n_steps_per_epoch=1000, show_progress=False)

    print("\nTraining complete.")

    print(
        "\nEvaluating the trained CQL policy in the live environment (Online Evaluation)..."
    )
    env = PsychiatricPOMDPEnv(horizon_days=10)

    total_rewards = []
    for _ in range(50):
        obs, _ = env.reset()
        done = False
        ep_reward = 0
        while not done:
            # Predict action from the offline-trained CQL policy
            action = cql.predict(np.array([obs]))[0]
            obs, reward, done, _ = env.step(action)
            ep_reward += reward
        total_rewards.append(ep_reward)

    avg_reward = np.mean(total_rewards)
    std_reward = np.std(total_rewards)
    print(
        f"Average Reward over 50 test episodes: {avg_reward:.3f} +/- {std_reward:.3f}"
    )

    # Save results to CSV for traceability
    df_eval = pd.DataFrame({"reward": total_rewards})
    csv_path = os.path.join(RESULTS_DIR, "offline_eval_log.csv")
    df_eval.to_csv(csv_path, index=False)

    summary_path = os.path.join(RESULTS_DIR, "offline_eval_summary.json")
    import json

    with open(summary_path, "w") as f:
        json.dump(
            {"avg_reward": avg_reward, "std_reward": std_reward, "episodes": 50},
            f,
            indent=4,
        )
    print(f"Offline evaluation results saved to {RESULTS_DIR}")


if __name__ == "__main__":
    # Ensure reproducibility
    np.random.seed(42)
    import torch

    torch.manual_seed(42)

    train_and_evaluate_offline_rl()
