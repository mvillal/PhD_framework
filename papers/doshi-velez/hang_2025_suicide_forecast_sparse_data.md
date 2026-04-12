---
title: "Improving Forecasts of Suicide Attempts for Patients with Little Data"
authors: ["Zhi Hang", "Finale Doshi-Velez"]
year: 2025
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "KDD (Knowledge Discovery and Data Mining)"
doi: "Forthcoming/Preprint"
url: "Forthcoming"
code: "N/A"
datasets: ["EHR", "EMA"]
tags: ["LSGP", "Sparse Data", "Suicide Prevention", "Transfer Learning"]
---

# Improving Forecasts of Suicide Attempts for Patients with Little Data

## 📋 Executive Summary
A major challenge in suicide prevention is the "cold start" problem: new patients have very little data, yet they may be at high risk. This paper introduces the Latent Similarity Gaussian Process (LSGP) to "borrow strength" from similar patients to make accurate rare-event predictions for those with sparse histories.

## 🛠️ Core Methodology
- **LSGP (Latent Similarity Gaussian Process):** A multi-task learning framework where the similarity between patients is learned in a latent space.
- **Borrowing Strength:** The model uses the "shared experience" of similar patients in the latent space to inform the prior for a new patient.
- **Rare-Event Prediction:** Optimized for the extreme class imbalance of suicide attempts (where "no attempt" is the 99.9% baseline).

## 📊 Dataset & Experimental Setup
- **Data Source:** Mixed EHR (Electronic Health Records) and EMA (Ecological Momentary Assessment) datasets.
- **Sample Size:** Large-scale historical cohorts used to train the "latent similarity" prior.
- **Features:** Demographic history, past psychiatric admissions, and high-frequency mood data.
- **Evaluation Metrics:** Precision-Recall AUC (critical for rare events), Sensitivity at fixed specificity.

## 💡 Key Findings
- **Technical Results:** LSGP significantly improved prediction accuracy for patients with < 5 data points compared to standard GPs or pooled LSTMs.
- **Clustering in Latent Space:** Found that patients clustered into distinct "risk phenotypes" (e.g., "chronic-stable" vs. "acute-volatile").
- **Ablation Studies:** Showed that learning the similarity metric was more effective than using fixed clinical similarities (e.g., ICD codes).

## 🩺 Clinical Relevance & Impact
Directly addresses the "First 48 Hours" problem in psychiatric care. By leveraging data from similar historical cases, the AI can provide a "warm start" risk assessment for a new patient before a long-term clinical baseline has been established.

## 🔬 Critical Review (Antagonic Perspective)
"Borrowing strength" can be dangerous if the "similar" patients are from a different demographic or have different underlying causes for their distress. It risks "stereotyping" a new patient based on the aggregate behavior of a latent cluster.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Williams & Rasmussen (2006)] for Gaussian Process theory.
- **Descendant Discovery:** [Lu et al. (2026)](lu_2026_neural_sdes_suicide_risk.md) for how to transition these sparse forecasts into continuous-time models.
