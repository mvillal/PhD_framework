# Recommended Literature and Tooling for Dynamic Fidelity-Constrained RL

## Academic Literature
1. **Neural SDEs and Compact State-Spaces:**
   - *Reference:* Li et al., 2020 ("Scalable Gradients for Stochastic Differential Equations") & "Neural Stochastic Differential Equations on Compact State-Spaces" (arXiv:2508.23000, 2025).
   - *Relevance:* Justifies the use of continuous-time models for irregularly sampled EMA data and provides a theoretical foundation for strictly bounding the latent clinical state (e.g., 0 to 1 severity) to prevent simulation divergence.

2. **Informative Missingness (MNAR):**
   - *Reference:* Lin, HW., Mermelstein, R.J., & Hedeker, D. (2018). "Latent trait shared-parameter mixed models for missing ecological momentary assessment data."
   - *Relevance:* Seminal work establishing that missing EMA data is a behavioral phenotype (I-MNAR). It defends our choice to model missingness via a Hawkes process coupled to the latent clinical severity (the "Silent Smoke Detector" effect).

3. **Safety Constraints in Clinical Offline RL:**
   - *Reference:* Wu, Y., Tucker, G., & Nachum, O. (2019). "Behavior Regularized Actor Critic (BRAC)."
   - *Relevance:* Formalizes the use of Reverse KL divergence penalties in Offline RL to anchor policies to safe, historically validated clinical behaviors (preventing OOD actions).

4. **Distributionally Robust Optimization:**
   - *Reference:* "A Unified Distributionally Robust Formulation for Offline RL" (arXiv 2024).
   - *Relevance:* Provides a mathematically rigorous way to frame our fidelity penalty, presenting the constraint not just as a regularization term, but as an uncertainty set around the empirical data distribution to handle non-stationary shifts (HMM phase transitions).

## Open-Source Software & Tooling
To upgrade our custom PyTorch implementation to production-grade, state-of-the-art standards, we should integrate the following libraries:

1. **`torchsde` (PyTorch)**
   - *Source:* Google Research (https://github.com/google-research/torchsde)
   - *Use Case:* Replace our manual Euler-Maruyama discretization in `rl_environment.py` with `torchsde`. It provides highly efficient, differentiable SDE solvers with GPU support and adjoint method sensitivity analysis, necessary for scaling up the Neural SDE-GAN.

2. **`d3rlpy` (PyTorch)**
   - *Source:* https://github.com/takuseno/d3rlpy
   - *Use Case:* The most practical and clinically adopted library for Offline RL. It implements Conservative Q-Learning (CQL) and Implicit Q-Learning (IQL), and crucially, includes built-in Off-Policy Evaluation (OPE) tooling (like Doubly Robust estimators) that we need to evaluate the Dynamic Fidelity Controller on historical data.

3. **`PyHealth` (PyTorch)**
   - *Source:* https://github.com/sunlabuiuc/PyHealth
   - *Use Case:* If we move to test our algorithm on MIMIC-III or eICU instead of strictly synthetic data, PyHealth provides the most robust ecosystem for extracting the "State-Action-Reward" tuples from raw Electronic Health Records (EHR).
