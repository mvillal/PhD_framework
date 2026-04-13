---
title: "Neural Stochastic Differential Equations on Compact State Spaces: Theory, Methods, and Application to Suicide Risk Modeling"
authors: ["Lu et al.", "Finale Doshi-Velez"]
year: 2026
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "arXiv"
doi: "10.48550/arXiv.26xx.xxxx"
url: "https://arxiv.org/abs/26xx.xxxx"
datasets: ["EMA", "Suicidal Thoughts and Behaviors (STBs)"]
tags: ["Neural SDEs", "Continuous-Time Modeling", "Psychiatric Risk", "EMA", "Compact State Spaces"]
---

# Neural Stochastic Differential Equations on Compact State Spaces: Theory, Methods, and Application to Suicide Risk Modeling

## 📋 Executive Summary
This paper introduces a principled framework for applying Neural Stochastic Differential Equations (SDEs) to psychiatric risk forecasting. By imposing compact state space constraints (e.g., 0-10 symptom scales), the model ensures that continuous-time risk trajectories remain within clinically valid boundaries, improving the trustworthiness and stability of suicide risk forecasts in high-frequency monitoring settings.

## 🛠️ Core Methodology
- **Neural SDEs on Compact Spaces:** A novel parameterization that ensures the SDE drift and diffusion terms respect hard boundaries ($[0, 1]^d$), preventing the latent state from diverging during long-term simulations.
- **Latent SDE Framework:** Utilizes a neural network to learn the time-varying drift and diffusion functions from irregularly-sampled observational data.
- **Continuous-Time Inference:** Enables risk prediction at any arbitrary time point, crucial for real-time mobile health interventions.

## 📊 Dataset & Experimental Setup
- **Data Source:** High-frequency Ecological Momentary Assessment (EMA) data from high-risk psychiatric patients.
- **Features:** Smartphone-reported Suicidal Thoughts and Behaviors (STBs), mood variability, and sleep metrics.
- **Evaluation Metrics:** Brier Scores at multiple time horizons, forecasting error on 0-10 bounded scales, and numerical stability comparisons with unconstrained Neural SDEs.

## 💡 Key Findings
- **Boundary Preservation:** The proposed model is the first to rigorously maintain risk forecasts within established clinical scales (e.g., 0-10) without post-hoc clipping.
- **Improved Long-term Stability:** Constrained SDEs demonstrate significantly better numerical stability and lower cumulative error in long-term risk simulations compared to standard Neural ODEs or SDEs.
- **Clinical Interpretability:** The diffusion term provides a direct measure of risk uncertainty, which naturally increases as the interval between patient self-reports grows.

## 🩺 Clinical Relevance & Impact
Provides a foundational tool for real-time suicide prevention systems. By modeling risk as a continuous process that respects clinical boundaries, the system can provide more reliable "early warning" signals to both patients and providers based on high-frequency, irregularly-sampled smartphone data.

## 🔬 Critical Review (Antagonic Perspective)
The computational complexity of Neural SDEs may limit real-time deployment on mobile devices. There is also a risk that the "boundary" constraints artificially suppress genuine high-risk fluctuations if the state space mapping is not perfectly aligned with the underlying clinical reality.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Kidger et al. (2020) on Neural SDEs.
- **Descendant Discovery:** Integrating Strategic Link Scores (Hüyük & Doshi-Velez, 2025) with continuous-time risk trajectories.
