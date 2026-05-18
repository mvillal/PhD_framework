import numpy as np
import torch
import torchsde


class PatientLatentSDE(torch.nn.Module):
    noise_type = "diagonal"
    sde_type = "ito"

    def __init__(self):
        super().__init__()

    def f(self, t, y):
        # y = [latent_x, baseline, base_vol]
        x = y[:, 0:1]
        baseline = y[:, 1:2]
        drift_x = 0.1 * (baseline - x)
        return torch.cat(
            [drift_x, torch.zeros_like(baseline), torch.zeros_like(baseline)], dim=1
        )

    def g(self, t, y):
        x = y[:, 0:1]
        base_vol = y[:, 2:3]
        spike = torch.relu(x - 0.8) ** 2 * 5.0
        diff_x = base_vol + spike
        return torch.cat(
            [diff_x, torch.zeros_like(base_vol), torch.zeros_like(base_vol)], dim=1
        )


class PsychiatricPOMDPEnv:
    """
    Partially Observable Markov Decision Process (POMDP) Environment for
    Psychiatric Digital Interventions (mHealth/EMA).

    The agent only observes:
    - The last reported EMA score (if any)
    - Time since last response (Informative Missingness feature)
    - Action fatigue (moving average of recent interventions)

    The true latent state (severity, volatility, & HMM phase) is hidden.
    """

    def __init__(self, horizon_days: int = 90, steps_per_day: int = 4):
        self.horizon_days = horizon_days
        self.steps_per_day = steps_per_day
        self.total_steps = horizon_days * steps_per_day
        self.dt = 1.0 / steps_per_day

        # HMM Transition Matrix: [Euthymic, Crisis]
        self.transition_matrix = np.array([[0.98, 0.02], [0.10, 0.90]])

        # Phase-specific parameters
        self.phase_baselines = [0.3, 0.8]  # [Euthymic baseline, Crisis baseline]
        self.phase_volatilities = [0.05, 0.20]  # [Euthymic base vol, Crisis base vol]

        # State variables
        self.current_step = 0
        self.hmm_phase = 0
        self.latent_x = 0.0
        self.latent_baseline = 0.0

        # Observation trackers
        self.time_since_last_response = 0
        self.last_observed_ema = 0.0
        self.fatigue = 0.0

        # TorchSDE module
        self.sde = PatientLatentSDE()

    def reset(self):
        """Initialize a new patient trajectory."""
        self.current_step = 0
        self.hmm_phase = np.random.choice([0, 1], p=[0.9, 0.1])
        self.latent_x = np.random.uniform(0.1, 0.4)
        self.latent_baseline = self.phase_baselines[self.hmm_phase]

        self.time_since_last_response = 0
        self.last_observed_ema = self.latent_x + np.random.normal(0, 0.02)
        self.fatigue = 0.0

        return self._get_observation(), self._get_info()

    def _missingness_intensity(self, x: float, vol: float, fatigue: float) -> float:
        # High severity, high volatility, and high intervention fatigue increase missingness
        return min(0.95, 0.1 + 0.5 * x**2 + 1.5 * vol + 0.3 * fatigue)

    def step(self, action: int):
        """
        action = 0 (Passive Monitoring)
        action = 1 (Send EMA / Intervene)
        """
        self.current_step += 1

        # 1. HMM Phase Transition
        self.hmm_phase = np.random.choice(
            [0, 1], p=self.transition_matrix[self.hmm_phase]
        )
        self.latent_baseline = self.phase_baselines[self.hmm_phase]
        current_base_vol = self.phase_volatilities[self.hmm_phase]

        # 2. Advance latent SDE using torchsde
        y0 = torch.tensor(
            [[self.latent_x, self.latent_baseline, current_base_vol]],
            dtype=torch.float32,
        )
        t_span = torch.tensor([0.0, self.dt], dtype=torch.float32)

        with torch.no_grad():
            res = torchsde.sdeint(self.sde, y0, t_span, method="euler", dt=self.dt)

        new_x = res[-1, 0, 0].item()

        # Action effect on latent state (Interventions slightly reduce severity if successful)
        treatment_effect = 0.0
        if action == 1:
            treatment_effect = -0.05 * self.dt  # Mild positive effect
            self.fatigue = min(1.0, self.fatigue + 0.2)  # Increases fatigue
        else:
            self.fatigue = max(0.0, self.fatigue - 0.05)  # Recovers

        self.latent_x = np.clip(new_x + treatment_effect, 0.0, 1.0)

        # Approximate volatility
        vol_approx = self.sde.g(t_span[0], y0)[0, 0].item()

        # 3. Determine Observation & Missingness
        is_missing = True
        reward = 0.0

        if action == 1:
            p_missing = self._missingness_intensity(
                self.latent_x, vol_approx, self.fatigue
            )
            is_missing = np.random.rand() < p_missing

            if not is_missing:
                self.last_observed_ema = np.clip(
                    self.latent_x + np.random.normal(0, 0.02), 0.0, 1.0
                )
                self.time_since_last_response = 0
                # Reward for successfully gathering data and mild clinical improvement
                reward = 0.1 - (self.latent_x * 0.1)
            else:
                self.time_since_last_response += 1
                # Penalty: Annoyed a patient in crisis or high fatigue
                reward = -0.2
        else:
            self.time_since_last_response += 1
            # Base clinical penalty for letting severity rise unattended
            reward = -(self.latent_x * 0.05)

        # 4. Check termination
        done = self.current_step >= self.total_steps

        return (
            self._get_observation(),
            reward,
            done,
            self._get_info(action, is_missing, current_base_vol),
        )

    def _get_observation(self):
        """
        The POMDP observation. The agent DOES NOT see self.latent_x.
        Returns: [last_observed_ema, time_since_last_response, fatigue]
        """
        return np.array(
            [self.last_observed_ema, float(self.time_since_last_response), self.fatigue]
        )

    def _get_info(self, action=None, is_missing=None, current_base_vol=0.05):
        y0 = torch.tensor(
            [[self.latent_x, self.latent_baseline, current_base_vol]],
            dtype=torch.float32,
        )
        vol_approx = self.sde.g(torch.tensor(0.0), y0)[0, 0].item()
        return {
            "hmm_phase": self.hmm_phase,
            "latent_severity": self.latent_x,
            "latent_volatility": vol_approx,
            "action_taken": action,
            "was_missing": is_missing,
        }


if __name__ == "__main__":
    env = PsychiatricPOMDPEnv(horizon_days=5)  # Short horizon for testing
    obs, info = env.reset()

    print(
        "--- Testing Psychiatric POMDP Environment (with Phase Shifts & torchsde) ---"
    )
    print(
        f"Initial State | Phase: {info['hmm_phase']} | Latent X: {info['latent_severity']:.2f} | Obs: {obs}"
    )

    cumulative_reward = 0
    done = False

    while not done:
        # Dummy policy: Intervene every other step
        action = 1 if env.current_step % 2 == 0 else 0

        obs, reward, done, info = env.step(action)
        cumulative_reward += reward

        phase_str = "CRISIS" if info["hmm_phase"] == 1 else "EUTHYMIC"

        print(
            f"Step {env.current_step:02d} | Phase: {phase_str:8s} | Action: {action} | Missed: {info['was_missing']} | "
            f"Obs: {obs} | Reward: {reward:+.3f} | True X: {info['latent_severity']:.2f}"
        )

    print(f"Episode finished. Cumulative Reward: {cumulative_reward:.3f}")
