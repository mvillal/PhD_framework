# Improving Forecasts of Suicide Attempts for Patients with Little Data (Hang et al., 2025)

## Summary
Introduces a Latent Similarity Gaussian Process (LSGP) to improve suicide attempt forecasts for patients with limited historical data by leveraging information from "similar" patients.

## Methodology
- **Latent Similarity Gaussian Process (LSGP):** A model that learns a latent space where patients with similar risk profiles are positioned close together, allowing for more effective information sharing.
- **Transfer Learning / Multi-task Learning:** Uses data from a broader cohort to inform predictions for individual patients with sparse data.

## Relevance
- **Rare-Event Prediction:** Suicide attempts are relatively rare events, making it difficult to build accurate models for individual patients without leveraging group-level information.
- **Suicide Prevention:** Particularly useful for new patients or those who have not been in treatment for a long period.

## Key Findings
- **Leveraging Similar Patients:** Successfully improves prediction accuracy for low-data patients by identifying and utilizing patterns from similar individuals in the dataset.
- **Robustness in Sparse Settings:** LSGP outperforms standard GP and other baseline models in scenarios where patient-specific data is limited.
