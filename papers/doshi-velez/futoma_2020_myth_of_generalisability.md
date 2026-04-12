---
title: "The Myth of Generalisability in Clinical Machine Learning"
authors: ["Joseph Futoma", "Michael J. Pencina", "Finale Doshi-Velez"]
year: 2020
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "Lancet Digital Health"
doi: "https://doi.org/10.1016/S2589-7500(20)30186-2"
code: "N/A"
datasets: ["MIMIC-III", "NYU Langone"]
tags: ["Generalizability", "Local Validation", "LSTM", "Measurement Bias"]
---

# The Myth of Generalisability in Clinical Machine Learning

## 📋 Executive Summary
A critical analysis of the push for "globally generalizable" AI models. It argues that clinical models often pick up on local administrative and practice patterns (e.g., when a doctor decides to order a test) rather than universal biological truths, making performance on external datasets misleading.

## 🛠️ Core Methodology
- **LSTMs (Long Short-Term Memory):** Used to model the temporal sequences of EHR data.
- **Measurement Indicator Variables:** Explicitly encoding the *timing* of clinical actions as features. The model learns that the act of ordering a lab test is often more predictive of an outcome than the lab result itself.
- **Cross-Site Evaluation:** Comparing model performance when trained on one hospital system and tested on another with different administrative protocols.

## 📊 Dataset & Experimental Setup
- **Data Source:** **MIMIC-III** (Beth Israel) and **NYU Langone Health** clinical data.
- **Sample Size:** Large-scale EHR cohorts from both institutions.
- **Features:** Longitudinal vitals, labs, medication orders, and administrative timestamps.
- **Evaluation Metrics:** AUROC, AUPRC, and "Calibration Drift" across sites.

## 💡 Key Findings
- **Technical Results:** Models trained at NYU performed poorly at Beth Israel (and vice versa) primarily due to differences in how clinicians *interact* with patients, not differences in patient biology.
- **Local Trap:** The model learns the "local practice" as a shortcut for the clinical outcome (e.g., "if the doctor orders an urgent lactate test, the patient is likely septic").
- **Ablation Studies:** Removing measurement timestamps significantly dropped AUROC, proving the model was relying on human behavioral cues.

## 🩺 Clinical Relevance & Impact
Challenges the "plug-and-play" approach to medical AI. It mandates that psychiatric or critical care models must be re-validated or fine-tuned for the specific workflows of the target clinic to avoid "phantom" performance.

## 🔬 Critical Review (Antagonic Perspective)
While the paper highlights a real problem, it may discourage the development of foundational models. The "Myth" might be partially solved by better representation learning that disentangles practice patterns from physiology, rather than just accepting localism.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Lipton (2018)] for "The Myth of Model Interpretability".
- **Descendant Discovery:** [Fischer et al. (2025)](fischer_2025_clinician_expectations.md) for how clinicians view these local monitoring needs.
