---
title: "Neural Stochastic Differential Equations (Neural SDEs)"
concept_type: "Modeling Framework"
tags: ["Continuous-Time", "Neural SDEs", "Psychiatric Risk", "EMA"]
sources: ["../../sources/doshi-velez/lu_2026_neural_sdes_suicide_risk.md", "../../sources/doshi-velez/hang_2025_suicide_forecast_sparse_data.md"]
---

# Neural Stochastic Differential Equations (Neural SDEs)

## 📋 Definition
Neural Stochastic Differential Equations (Neural SDEs) are a class of continuous-time models that parameterize the drift and diffusion terms of an SDE using neural networks. In clinical settings, they allow for modeling patient trajectories that are irregularly sampled and inherently stochastic.

## 🛠️ Key Technical Components
- **Compact State Spaces**: Recent advancements (Lu et al., 2026) impose hard boundary constraints (e.g., $[0, 10]$ scales) on the SDE state space. This ensures that psychiatric risk scores remain within clinically valid ranges without requiring post-hoc clipping.
- **Continuous-Time Inference**: Unlike discrete-time RNNs, Neural SDEs can predict the latent state (and associated risk) at any arbitrary time point $t$, making them ideal for real-time monitoring via smartphone-based EMA.
- **Latent Similarity Gaussian Processes (LSGP)**: To handle the "cold start" or sparse data problem for new patients, LSGP frameworks (Hang et al., 2025) allow models to "borrow strength" from similar patient cohorts by positioning them in a shared latent space.

## 🩺 Clinical Applications
- **Suicide Risk Forecasting**: High-frequency monitoring of Suicidal Thoughts and Behaviors (STBs) where the interval between patient self-reports is variable.
- **Uncertainty Quantification**: The diffusion term in the SDE provides a natural measure of uncertainty that grows as the time since the last observation increases.

## 🔗 Related Concepts
- [Offline Reinforcement Learning](offline_rl.md)
- [Causal Off-Policy Evaluation](causal_ope.md)
