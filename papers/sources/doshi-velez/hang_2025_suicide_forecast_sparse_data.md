---
title: "Improving Forecasts of Suicide Attempts for Patients with Little Data"
authors: ["Hang et al."]
year: 2025
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "NeurIPS TS4H Workshop"
doi: "N/A"
code: "https://github.com/cornellius-gp/gpytorch (Implementation Backend)"
datasets: ["EMA-Suicide-HighFreq", "DtAK-Private-EHR"]
tags: ["Suicide Forecasting", "Latent Similarity GP", "LSGP", "Sparse Data", "Hierarchical Modeling"]
---

# Improving Forecasts of Suicide Attempts for Patients with Little Data

## 📋 Executive Summary
Hang et al. (2025) address a fundamental bottleneck in psychiatric AI: the "Cold Start" problem for suicide risk. Suicide attempts are rare, and patients are heterogeneous, making it difficult to train robust models for new patients with limited data. The paper introduces **Latent Similarity Gaussian Processes (LSGPs)**, which learn to group similar patients in a latent space. This allows the model to "borrow strength" from clinical "neighbors," enabling accurate risk forecasting even when an individual's personal history is sparse.

## 🛠️ Core Methodology
- **Latent Similarity Gaussian Processes (LSGPs):** Extends standard GPs by adding a latent variable $z_i$ for each patient $i$. The kernel $K((x, z), (x', z'))$ measures similarity in both time/features ($x$) and the latent patient space ($z$).
- **Clustered Multi-task Learning:** Instead of one global model, LSGP discovers clusters of patients with similar risk dynamics (e.g., "rapidly fluctuating" vs. "chronic baseline" risk).
- **Hierarchical Prior:** Uses a prior over the latent space to guide the grouping of patients based on baseline clinical features (e.g., history of depression, age).

## 📊 Dataset & Experimental Setup
- **Dataset:** High-frequency EMA (Ecological Momentary Assessment) data from the Nock Lab, tracking daily suicidal ideation and behaviors.
- **Experimental Design:** Specifically tested performance on "low-data" patients (first 7-14 days of monitoring) compared to global population-averaged models and individualized models.

## 💡 Key Findings
- **Borrowing Strength:** LSGPs outperformed individual models by 18% in AUROC for patients with less than 2 weeks of data.
- **Interpretable Neighbors:** The latent space $z$ allows clinicians to see which "prototypical" patient profile a new patient most closely matches, providing actionable clinical context beyond a raw score.
- **Uncertainty Calibration:** Like standard GPs, LSGPs provide calibrated uncertainty, flagging when a patient's trajectory is too unique to be matched to any known latent neighbor.

## 🩺 Clinical Relevance & Impact
The LSGP framework enables **Personalized Suicide Prevention** from day one. By identifying a patient's "latent type," clinicians can choose interventions that have been effective for similar individuals, rather than relying on population-level averages that may not apply to high-risk outliers.

## 🔬 Critical Review (Antagonic Perspective)
The reliance on "similarity" assumes that past patient clusters are representative of future ones. If a new patient presents a truly novel risk profile, the LSGP might force them into an inappropriate cluster (The Procrustean Bed trap).

## 🔗 Discovery & Next Steps
- **Implementation:** Utilize `gpytorch`'s `ClusterMultitaskGPModel` or `BayesianGPLVM` patterns to implement the latent grouping logic.
- **Concept Link:** Updates [N-of-1 Modeling](../concepts/n_of_1_modeling.md) and [Digital Phenotyping](../concepts/digital_phenotyping.md).
