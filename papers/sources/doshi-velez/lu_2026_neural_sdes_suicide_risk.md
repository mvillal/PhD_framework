---
title: "Neural Stochastic Differential Equations on Compact State Spaces: Theory, Methods, and Application to Suicide Risk Modeling"
authors: ["Lu et al."]
year: 2026
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "TBD"
doi: "TBD"
code: "https://github.com/rtqichen/torchdiffeq (Core Engine)"
datasets: ["EHR-Suicide-2026", "Digital-Phenotype-Longitudinal"]
tags: ["Neural SDEs", "Compact State Spaces", "Suicide Risk", "Continuous-Time Modeling", "Adjoint Method"]
---

# Neural Stochastic Differential Equations on Compact State Spaces

## 📋 Executive Summary
Lu et al. (2026) introduce a novel framework for modeling psychiatric risk (specifically suicide risk) using **Neural Stochastic Differential Equations (Neural SDEs)**. The primary innovation is the enforcement of **compact state spaces**, ensuring that the latent risk variables remain within clinically interpretable and mathematically stable bounds (e.g., [0, 1]). This prevents the "divergence" common in standard latent SDEs when applied to sparse, noisy EHR data.

## 🛠️ Core Methodology
- **Neural SDE Formulation:** $dx_t = f_\theta(x_t, t)dt + g_\phi(x_t, t)dW_t$, where $f$ is the drift (deterministic trend) and $g$ is the diffusion (stochastic noise/uncertainty).
- **Compact State Spaces:** The model utilizes a **barrier function** or **diffeomorphic mapping** (e.g., sigmoid or tanh transformations within the SDE) to ensure the latent trajectory $x_t$ never exits a pre-defined compact set.
- **Memory Efficiency:** Employs the **Adjoint Method** (`odeint_adjoint`) from `torchdiffeq` to train the SDE with $O(1)$ memory cost, allowing for long-horizon longitudinal modeling (months of patient data) without GPU memory overflow.

## 📊 Dataset & Experimental Setup
- **Dataset:** A multi-site EHR dataset comprising 50,000+ longitudinal patient records with high-frequency "digital phenotype" sensor data (mobility, sleep, typing dynamics).
- **Baselines:** Compared against discrete-time LSTMs, GRU-ODEs, and standard Neural ODEs.

## 💡 Key Findings
- **Uncertainty Quantification:** Unlike Neural ODEs, the Neural SDE successfully captures **aleatoric uncertainty**, providing a "confidence interval" for suicide risk that widens during periods of missing data (e.g., if a patient stops using their phone).
- **Performance:** Achieved an **AUROC of 0.89** for 30-day suicide attempt prediction, a 12% improvement over GRU-ODE baselines.
- **Stability:** The compact state space constraint reduced training instability by 40% compared to unconstrained Neural SDEs.

## 🩺 Clinical Relevance & Impact
The model moves from "point predictions" to **Continuous-Time Risk Trajectories**. Clinicians can see not just a "high risk" flag, but a dynamic trend where the widening of the uncertainty band (diffusion) signals a need for active human intervention or "Learning to Defer" (L2D).

## 🔬 Critical Review (Antagonic Perspective)
While the compact state space solves mathematical stability, it may introduce **Biased Clipping** if the true risk latent is more volatile than the barrier function allows. Furthermore, the diffusion term $g_\phi$ is difficult to validate clinically—does "model uncertainty" truly map to "clinical instability"?

## 🔗 Discovery & Next Steps
- **Implementation:** Explore the use of `torchsde` for more advanced Ito/Stratonovich solvers.
- **Synthesis Link:** Connects to [Agentic Foundations & Autoresearcher Frameworks](synthesis/agentic_foundations_2026.md) as a core predictive engine for research agents.
