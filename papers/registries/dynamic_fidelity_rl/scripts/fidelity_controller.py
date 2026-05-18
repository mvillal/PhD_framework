import numpy as np


class DynamicFidelityController:
    """
    Monitors Algorithm Fidelity by calculating the Effective Sample Size (ESS)
    using Importance Sampling weights. Penalizes policies that diverge too
    far from the baseline (safe) protocol, preventing the 'Adaptivity Trap'.
    """

    def __init__(self, window_size: int = 50, ess_threshold: float = 0.3):
        self.window_size = window_size
        # Threshold as a percentage of window size
        self.ess_threshold_abs = window_size * ess_threshold
        self.weights_history = []

    def update(self, pi_e_prob: float, pi_b_prob: float):
        """
        Update the controller with the probability of the chosen action
        under the evaluation policy (pi_e) and behavioral/baseline policy (pi_b).
        """
        # Protect against division by zero
        pi_b_prob = max(pi_b_prob, 1e-8)

        # Incremental IS weight
        w = pi_e_prob / pi_b_prob
        self.weights_history.append(w)

        if len(self.weights_history) > self.window_size:
            self.weights_history.pop(0)

    def compute_ess(self) -> float:
        """Computes Kish's Effective Sample Size over the current window."""
        if not self.weights_history:
            return 0.0

        w_array = np.array(self.weights_history)
        sum_w = np.sum(w_array)

        if sum_w == 0:
            return 0.0

        ess = (sum_w**2) / np.sum(w_array**2)
        return ess

    def get_fidelity_penalty(
        self,
        pi_e_dist: np.ndarray,
        pi_safe_dist: np.ndarray,
        lambda_penalty: float = 1.0,
    ) -> float:
        """
        Returns a penalty if the ESS drops below the critical threshold.
        The penalty is proportional to the KL divergence between the current
        policy and the safe baseline policy.
        """
        ess = self.compute_ess()

        # If ESS is healthy, no penalty (Euthymic Expansion allowed)
        if (
            ess >= self.ess_threshold_abs
            or len(self.weights_history) < self.window_size // 2
        ):
            return 0.0

        # Crisis Contraction: ESS is critically low. Calculate KL Divergence
        # D_KL(pi_e || pi_safe) = sum(pi_e * log(pi_e / pi_safe))
        pi_e_safe = np.clip(pi_e_dist, 1e-8, 1.0)
        pi_safe_safe = np.clip(pi_safe_dist, 1e-8, 1.0)

        kl_div = np.sum(pi_e_safe * np.log(pi_e_safe / pi_safe_safe))

        # The penalty grows stronger the lower the ESS gets below the threshold
        severity_multiplier = (self.ess_threshold_abs - ess) / self.ess_threshold_abs

        return -1.0 * lambda_penalty * severity_multiplier * kl_div


if __name__ == "__main__":
    # Test the controller
    controller = DynamicFidelityController(
        window_size=20, ess_threshold=0.7
    )  # Threshold is 14

    safe_policy = np.array([0.5, 0.5])  # 50% chance to intervene
    eval_policy_good = np.array([0.6, 0.4])  # Slight deviation
    eval_policy_bad = np.array([0.99, 0.01])  # Extreme deviation (gaming)

    print("--- Testing Dynamic Fidelity Controller ---")

    # Simulate actions taken by the safe behavioral policy in the environment
    actions_taken = [0, 1] * 10  # 10 of action 0, 10 of action 1

    # 1. Simulate healthy exploration
    for action in actions_taken:
        controller.update(
            pi_e_prob=eval_policy_good[action], pi_b_prob=safe_policy[action]
        )

    ess = controller.compute_ess()
    penalty = controller.get_fidelity_penalty(eval_policy_good, safe_policy)
    print(f"Healthy Exploration -> ESS: {ess:.2f}/20.0 | Penalty: {penalty:.4f}")

    # 2. Simulate dangerous 'gaming'
    controller = DynamicFidelityController(window_size=20, ess_threshold=0.7)
    for action in actions_taken:
        controller.update(
            pi_e_prob=eval_policy_bad[action], pi_b_prob=safe_policy[action]
        )

    ess = controller.compute_ess()
    penalty = controller.get_fidelity_penalty(eval_policy_bad, safe_policy)
    print(f"Dangerous Gaming    -> ESS: {ess:.2f}/20.0 | Penalty: {penalty:.4f}")
