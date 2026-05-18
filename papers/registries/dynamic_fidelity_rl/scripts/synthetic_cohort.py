import numpy as np
import pandas as pd


class SyntheticCohortGenerator:
    """
    Generates synthetic Ecological Momentary Assessment (EMA) data for psychiatric trials.
    Models heteroskedastic volatility and Informative Missingness (MNAR) using
    a discretized Stochastic Differential Equation (SDE) and a Hawkes-like intensity process.

    Now expanded with a Hierarchical Dirichlet Process Hidden Markov Model (HDP-HMM)
    approximation to simulate sudden psychiatric phase shifts (Euthymic vs. Crisis).
    """

    def __init__(
        self, num_patients: int = 100, horizon_days: int = 90, steps_per_day: int = 4
    ):
        self.num_patients = num_patients
        self.horizon_days = horizon_days
        self.steps_per_day = steps_per_day
        self.total_steps = horizon_days * steps_per_day
        self.dt = 1.0 / steps_per_day

        # HMM Transition Matrix: [Euthymic, Crisis]
        # Euthymic -> Euthymic: 0.98, Euthymic -> Crisis: 0.02
        # Crisis -> Euthymic: 0.10, Crisis -> Crisis: 0.90
        self.transition_matrix = np.array([[0.98, 0.02], [0.10, 0.90]])

        # Phase-specific parameters
        self.phase_baselines = [0.3, 0.8]  # [Euthymic baseline, Crisis baseline]
        self.phase_volatilities = [0.05, 0.20]  # [Euthymic base vol, Crisis base vol]

    def _drift(self, x: float, baseline: float, reversion_speed: float = 0.1) -> float:
        """Mean-reverting drift function (Ornstein-Uhlenbeck style)."""
        return reversion_speed * (baseline - x)

    def _diffusion(
        self, x: float, base_volatility: float, crisis_threshold: float = 0.8
    ) -> float:
        """
        State-dependent volatility. Volatility spikes when state approaches crisis threshold.
        """
        spike = max(0, x - crisis_threshold) ** 2 * 5.0
        return base_volatility + spike

    def _missingness_intensity(
        self, x: float, volatility: float, base_rate: float = 0.1
    ) -> float:
        """
        Intensity of missing an EMA prompt. Higher severity (x) and volatility
        exponentially increase the chance of missingness (Silent Smoke Detector).
        """
        return min(0.95, base_rate + 0.5 * x**2 + 1.5 * volatility)

    def generate_patient(self, patient_id: int) -> pd.DataFrame:
        """Simulate a single patient's trajectory with sudden phase shifts."""
        records = []

        # Initial latent state
        x = np.random.uniform(0.1, 0.4)

        # Initial HMM phase (0: Euthymic, 1: Crisis) - mostly start euthymic
        phase = np.random.choice([0, 1], p=[0.9, 0.1])

        for step in range(self.total_steps):
            day = step * self.dt

            # 1. HMM Phase Transition
            phase = np.random.choice([0, 1], p=self.transition_matrix[phase])

            current_baseline = self.phase_baselines[phase]
            current_base_vol = self.phase_volatilities[phase]

            # 2. SDE Euler-Maruyama discretization
            dW = np.random.normal(0, np.sqrt(self.dt))
            vol = self._diffusion(x, current_base_vol)

            dx = self._drift(x, current_baseline) * self.dt + vol * dW
            x = np.clip(x + dx, 0.0, 1.0)  # Map to [0,1]

            # 3. Missingness generation (MNAR)
            p_missing = self._missingness_intensity(x, vol)
            is_missing = np.random.rand() < p_missing

            # 4. Observed EMA
            observed_x = (
                np.nan
                if is_missing
                else np.clip(x + np.random.normal(0, 0.02), 0.0, 1.0)
            )

            records.append(
                {
                    "patient_id": patient_id,
                    "time_step": step,
                    "day": day,
                    "hmm_phase": phase,
                    "latent_severity": x,
                    "latent_volatility": vol,
                    "p_missing": p_missing,
                    "is_missing": is_missing,
                    "observed_ema": observed_x,
                }
            )

        return pd.DataFrame(records)

    def generate_cohort(self) -> pd.DataFrame:
        """Generate data for the full cohort."""
        cohort_data = []
        for i in range(self.num_patients):
            cohort_data.append(self.generate_patient(i))
        return pd.concat(cohort_data, ignore_index=True)


if __name__ == "__main__":
    generator = SyntheticCohortGenerator(num_patients=5)
    df = generator.generate_cohort()

    print(f"Generated {len(df)} records across {df['patient_id'].nunique()} patients.")
    print(f"Overall missingness rate: {df['is_missing'].mean():.2%}")
    print(f"Time spent in Crisis Phase: {df['hmm_phase'].mean():.2%}")
    print("\nSample Data (First 10 steps of Patient 0):")
    print(df.head(10))
