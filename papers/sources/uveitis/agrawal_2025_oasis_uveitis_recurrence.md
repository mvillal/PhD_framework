---
title: "Machine learning for predicting recurrent course in uveitis using baseline clinical characteristics"
authors: ["Utami et al.", "Rupesh Agrawal (Corresponding)"]
year: 2025
lab: "OASIS / PROTON Registry (Multinational)"
venue: "Investigative Ophthalmology & Visual Science (IOVS)"
doi: "10.1167/iovs.XXXXX"
code: "N/A"
datasets: ["OASIS-Registry-1.4k-eyes", "PROTON-Multinational"]
tags: ["Uveitis", "Recurrence Prediction", "OASIS Registry", "Random Forest", "Feature Importance"]
---

# Predicting Uveitis Recurrence using OASIS Data

## 📋 Executive Summary
Utami, Agrawal, et al. (2025) develop an etiology-agnostic machine learning framework to predict whether a patient will follow a recurrent or monophasic course of uveitis. Using data from the multinational **OASIS (Ocular Autoimmune Systemic Inflammatory Infectious Study)** registry, the model aims to solve the "proactive stratification" challenge—identifying which patients require aggressive steroid-sparing therapy early vs. those who can be monitored conservatively.

## 🛠️ Core Methodology
- **Registry Analysis:** Extracted data from 966 patients (1,432 eyes) from the OASIS 1 (retrospective) and OASIS 2 (prospective) databases.
- **Model Selection:** Compared Random Forest (RF), XGBoost, and Radial Basis Function SVC.
- **Feature Engineering:** Leveraged 20+ baseline clinical parameters including anatomical presentation, cells/flare grading, and etiological screening results.
- **SHAP Analysis:** Used to provide clinicians with "feature importance" for each prediction.

## 📊 Dataset & Experimental Setup
- **Dataset:** OASIS Multinational Registry (10 years of longitudinal follow-up).
- **Metric:** Accuracy (0.77), Specificity (0.93), Sensitivity (0.44).
- **Validation:** Tested on "unseen" center data to verify cross-center stability.

## 💡 Key Findings
- **High Specificity:** The Random Forest model was exceptionally good at identifying patients who were **low risk for recurrence** (93% specificity), allowing for potential reduction in unnecessary follow-ups.
- **Strongest Predictors:** Baseline **Vitreous Haze**, retrolental cells, and non-infectious etiology were the most significant drivers of recurrent disease.
- **Idiopathic Shift:** 50.8% of cases initially labeled as idiopathic received a specific diagnosis within 10 years, highlighting the need for continuous ML re-calibration as new data emerges.

## 🩺 Clinical Relevance & Impact
The Agrawal 2025 model shifts uveitis management from "watchful waiting" to **Proactive Risk Stratification**. It provides a validated way to identify patients with vitreous haze who are at high risk for a difficult, recurrent course, justifying early systemic intervention.

## 🔬 Critical Review (Antagonic Perspective)
The model's **low sensitivity (0.44)** is a significant hurdle. While it identifies "safe" patients well, it misses more than half of the recurrent cases. Relying solely on this model could lead to dangerous under-treatment for a large subset of the high-risk population.

## 🔗 Discovery & Next Steps
- **Implementation:** Explore using `causalml`'s uplift modeling (found via Context7) to identify which patients' "recurrence risk" is most reduced by specific immunosuppressants.
- **Concept Link:** Updates [Objective Inflammation Grading](../concepts/objective_inflammation_grading.md).
