---
title: "Neural SDEs for Suicide Risk Modeling in Continuous Time"
authors: ["Yuzhe Lu", "Finale Doshi-Velez"]
year: 2026
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "TBD / Preprint"
doi: "Forthcoming/Preprint"
url: "Forthcoming"
code: "N/A"
datasets: ["EMA"]
tags: ["Neural SDE", "Suicide Prevention", "Continuous Time", "EMA"]
---

# Neural SDEs for Suicide Risk Modeling in Continuous Time

## 📋 Executive Summary
This research employs Neural Stochastic Differential Equations (Neural SDEs) to model the volatile dynamics of suicide risk. Unlike discrete models, Neural SDEs capture the continuous-time evolution of mood and risk, using constraints to keep predictions within clinically valid bounds (e.g., 0-10 scales).

## 🛠️ Core Methodology
- **Neural Stochastic Differential Equations (Neural SDEs):** Models the drift and diffusion of risk as a continuous process $dX_t = f(X_t, t)dt + g(X_t, t)dW_t$.
- **Compact State Space Constraints:** Ensures the "latent risk state" stays within a defined range (e.g., 0-10) using specialized activation functions or barrier methods, mirroring clinical psychiatric scales.
- **Adjoint Method Training:** Efficiently backpropagating through the SDE solver for parameter optimization.

## 📊 Dataset & Experimental Setup
- **Data Source:** **EMA** (Ecological Momentary Assessment) data from high-risk psychiatric cohorts.
- **Sample Size:** Longitudinal data from high-frequency smartphone surveys.
- **Features:** Mood ratings (**0-10 scales**), sleep quality, stress levels, and suicidal ideation intensity.
- **Evaluation Metrics:** Negative Log-Likelihood (NLL), Continuous-Time Prediction Error, and "Time-to-Crisis" accuracy.

## 💡 Key Findings
- **Technical Results:** Neural SDEs outperformed LSTMs and standard ODEs by better capturing the "stochastic jumps" and volatility inherent in mental health crises.
- **Clinical Interpretability:** By constraining the state space to 0-10, clinicians can interpret the model's "internal mood" as a direct digital twin of the patient's self-report.
- **Ablation Studies:** Showed that the "stochastic" component (diffusion) is critical for modeling the unpredictability of suicidal ideation.

## 🩺 Clinical Relevance & Impact
Provides a "weather forecast" for suicide risk. Instead of predicting if a patient will be at risk next week, it estimates the *probability trajectory* of risk over the next 24 hours, allowing for proactive, rather than reactive, intervention.

## 🔬 Critical Review (Antagonic Perspective)
The complexity of Neural SDEs makes them "black-box" in their own way. While the output (0-10) is interpretable, the underlying drift/diffusion functions are high-dimensional neural networks, which may be difficult to "explain" to a grieving family or a legal review board.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Chen et al. (2018)] for Neural ODEs.
- **Descendant Discovery:** [Hang et al. (2025)](hang_2025_suicide_forecast_sparse_data.md) for handling the "sparse data" problem often found in these EMA streams.
