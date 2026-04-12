# Neural SDEs for Suicide Risk Modeling (Lu et al., 2026)

## Summary
Employs Neural Stochastic Differential Equations (Neural SDEs) constrained to "compact state spaces" to model and forecast suicide risk in continuous time.

## Methodology
- **Neural Stochastic Differential Equations (Neural SDEs):** Combines the expressiveness of neural networks with the formal framework of SDEs to model complex, continuous-time dynamics.
- **Compact State Space Constraints:** Constrains the model's state space to align with clinical scales (e.g., 0-10), ensuring that the model's outputs remain within interpretable and clinically meaningful bounds.

## Data
- **EMA (Ecological Momentary Assessment):** Uses high-frequency data collected via mobile devices from high-risk suicide cohorts.

## Relevance
- **Continuous-Time Risk Forecasting:** Allows for the prediction of suicide risk at any point in time, rather than at fixed intervals.
- **Psychiatric Crisis Prevention:** Provides a more granular and timely understanding of a patient's risk profile, potentially enabling earlier intervention.

## Key Findings
- **Accurate Risk Trajectories:** Neural SDEs are effective at capturing the non-linear and stochastic nature of suicide risk over time.
- **Clinical Interpretability:** The compact state space constraint makes the model's internal states easier for clinicians to interpret and relate to standard assessment tools.
