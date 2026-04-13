---
title: "Improving Forecasts of Suicide Attempts for Patients with Little Data"
authors: ["Hang et al.", "Finale Doshi-Velez"]
year: 2025
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "NeurIPS / TS4H"
doi: "10.48550/arXiv.2511.18199"
url: "https://arxiv.org/abs/2511.18199"
datasets: ["EMA", "Suicidal Thoughts and Behaviors (STBs)"]
tags: ["LSGP", "Sparse Data", "Suicide Forecasting", "Rare Events", "Latent Space"]
---

# Improving Forecasts of Suicide Attempts for Patients with Little Data

## 📋 Executive Summary
This paper introduces the Latent Similarity Gaussian Process (LSGP), a framework specifically designed for suicide attempt forecasting in high-risk psychiatric patients with sparse individual data. By positioning patients in a latent similarity space, LSGP allows individual-level models to "borrow strength" from similar patient trajectories, improving the forecasting of rare, high-risk events.

## 🛠️ Core Methodology
- **Latent Similarity Gaussian Processes (LSGP):** A Bayesian framework that learns a latent space mapping where patients with similar behavioral trends are positioned closer together.
- **"Borrowing Strength":** Unlike global models that average across all patients or per-patient models that overfit, LSGP uses a kernel that combines individual time dynamics with cross-patient latent similarity.
- **Handling Sparse EMA Data:** Optimizes performance for patients who provide infrequent or incomplete smartphone self-reports.

## 📊 Dataset & Experimental Setup
- **Data Source:** Ecological Momentary Assessment (EMA) data capturing real-time Suicidal Thoughts and Behaviors (STBs) via smartphones.
- **Features:** High-frequency, self-reported symptom scores, mood, and sleep indicators (n = 100+ high-risk participants).
- **Evaluation Metrics:** AUPRC (Area Under Precision-Recall Curve), Brier Scores, and "Early Warning" lead time.

## 💡 Key Findings
- **LSGP Superiority:** Outperforms standard per-patient GPs and pooled global models by significant margins in patients with less than 2 weeks of data.
- **Latent Mapping:** Identifies distinct cohorts of suicidal patients based on symptom trajectory patterns rather than static clinical demographics.
- **Rare Event Detection:** Correctly identifies more "pre-attempt" windows while maintaining lower false-alarm rates compared to existing baseline models.

## 🩺 Clinical Relevance & Impact
Provides a more principled and accurate tool for real-time psychiatric risk monitoring. This directly impacts suicide prevention by enabling clinicians to intervene more precisely for individual patients, even when those patients have only recently begun being monitored.

## 🔬 Critical Review (Antagonic Perspective)
The learned latent similarity might be biased by data density; patients with more data might disproportionately influence the latent structure. The "borrowed strength" mechanism assumes that similar behavioral trends imply similar underlying risk, which might not hold if the latent features miss critical contextual nuances (e.g., life events).

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Yacoby et al. (2020) on Gaussian Processes for healthcare.
- **Descendant Discovery:** Integrating Neural SDEs with LSGP for continuous-time risk forecasting (Lu et al., 2026).
