---
title: "The Myth of Generalisability in Clinical Research and Machine Learning in Health Care"
authors: ["Futoma et al."]
year: 2020
lab: "Data to Actionable Knowledge Lab (DtAK) / Harvard"
venue: "The Lancet Digital Health"
doi: "10.1016/S2589-7500(20)30186-2"
code: "N/A"
datasets: ["MIMIC-III", "EHR-Heterogeneity"]
tags: ["Generalizability", "Dataset Shift", "Local Validation", "Clinical Utility", "EHR Bias"]
---

# The Myth of Generalisability in Clinical Machine Learning

## 📋 Executive Summary
Futoma et al. (2020) challenge the prevailing notion that "universal generalizability" is the ultimate measure of quality for clinical machine learning models. They argue that healthcare is fundamentally heterogeneous—spanning diverse patient populations, clinical protocols, and data recording practices. Pursuing a model that works everywhere often leads to models that are mediocre everywhere. Instead, they advocate for **Local Validation** and **Continuous Adaptation**, where a model's value is defined by its clinical utility at a specific bedside.

## 🛠️ Core Methodology
- **Critical Analysis of External Validation:** Evaluates why models that pass "external validation" on secondary datasets often fail when deployed in real-world clinical workflows.
- **Framework for Local Adaptation:** Proposes shifting the focus from "frozen models" to "robust methodologies" and retraining pipelines that can adapt to local data distributions.
- **Analysis of Dataset Shift:** Identifies three types of shift that break generalizability:
    1. **Population Shift:** Changes in patient demographics.
    2. **Protocol Shift:** Changes in how clinicians treat patients (e.g., new sepsis guidelines).
    3. **Recording Shift:** Changes in EHR systems or coding practices.

## 📊 Dataset & Experimental Setup
- **Context:** The authors leverage their extensive experience with **MIMIC-III** and multi-hospital EHR studies to illustrate how "Hospital A's" model fails at "Hospital B" due to unobserved local confounders.

## 💡 Key Findings
- **The "Local Knowledge" Advantage:** Site-specific models often outperform globally generalized models because they capture local clinical nuances and institutional biases that are actually informative for prediction.
- **Generalizability of Methodology:** The authors suggest that what should be "generalized" is the *method* of building and validating the model, not the *weights* of the model itself.
- **Utility over Universality:** A model with 0.95 AUROC at one hospital is more clinically valuable than a model with 0.75 AUROC that works at ten hospitals.

## 🩺 Clinical Relevance & Impact
This paper provides the ethical and technical justification for **Site-Specific AI Deployment**. It suggests that regulators (like the FDA) should move toward certifying "Adaptive AI Lifecycles" rather than static "Medical Devices." For psychiatry, this is critical because "depression" or "suicide risk" can manifest differently across cultures and clinical settings.

## 🔬 Critical Review (Antagonic Perspective)
The "Local Validation" approach risks creating **Data Silos** and may be infeasible for small clinics that lack the compute/data to train local models. It may also mask **Systemic Biases**—if a local model learns to replicate a clinician's biased behavior, "local validation" will confirm that bias as "clinical utility."

## 🔗 Discovery & Next Steps
- **Concept Link:** Foundational to [Causal Transportability](../concepts/causal_falsification.md) and [Offline RL](concepts/offline_rl.md).
- **Synthesis Link:** Directly connects to [The State of Clinical RL (2026)](synthesis/state_of_clinical_rl_2026.md).
