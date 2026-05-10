---
title: "Detecting Inflammation in Fundus Photographs Using Machine Learning: A Non-Invasive Surrogate for Fluorescein Angiography"
authors: ["S. Saeed Mohammadi", "Quan Dong Nguyen (Corresponding)", "et al."]
year: 2026
lab: "Nguyen Lab, Stanford University / Byers Eye Institute"
venue: "Ophthalmology Science"
doi: "10.1016/j.xops.2025.XXXXX"
code: "Google-Vertex-AI-AutoML"
datasets: ["302 UWF Images", "UWFFP vs UWFFA Pairings"]
tags: ["Uveitis", "Ultra-Widefield (UWF)", "Inflammation Detection", "AutoML", "Non-Invasive Monitoring"]
---

# UWF Inflammation Detection: Surrogates for Angiography

## 📋 Executive Summary
Mohammadi et al. (2026) establish **Ultra-Widefield Fundus Photographs (UWFFP)** as a reliable, non-invasive surrogate for **Fluorescein Angiography (UWFFA)**—the clinical gold standard for detecting active posterior uveitis. By using machine learning to detect inflammatory signals (e.g., vascular leakage, peripheral haze) that are often invisible to the human eye on standard photographs, the researchers demonstrate that invasive dye injections can be reduced without sacrificing diagnostic accuracy.

## 🛠️ Core Methodology
- **AI Platform:** Leveraged **Google Cloud Vertex AI (AutoML)** for single-label image classification.
- **Ground Truth:** Training was supervised by "paired" images, where active inflammation was confirmed via the presence of leakage on corresponding UWF fluorescein angiography.
- **Data Modality:** Focused specifically on **Ultra-Widefield (200-degree)** images, which capture peripheral inflammatory markers often missed by standard 45-degree fundus cameras.

## 📊 Dataset & Experimental Setup
- **Cohort:** 302 UWF fundus photographs (113 active inflammation, 189 without).
- **Validation:** Internal and external test sets, including a "specialist vs. AI" head-to-head comparison.

## 💡 Key Findings
- **Superior Accuracy:** The AI achieved an **AUC of 0.943**, with 95% accuracy in a head-to-head specialist test.
- **Clinician Benchmarking:** The AI outperformed:
    *   Uveitis Specialists (80–85% accuracy)
    *   Glaucoma Specialists (70% accuracy)
    *   Comprehensive Ophthalmologists (65% accuracy)
- **Subclinical Signal:** The model proved that active inflammation produces "latent" pixel-level deviations on color photographs that AI can identify even when human experts cannot.

## 🩺 Clinical Relevance & Impact
This paper provides the basis for **Low-Risk, High-Frequency Monitoring**. Patients can be screened for uveitis recurrence using simple UWF photography in primary care or community optometry settings, only being referred for invasive angiography if the AI detects a subclinical signal. This reduces the risk of allergic reactions to fluorescein and decreases clinical costs.

## 🔬 Critical Review (Antagonic Perspective)
The use of **AutoML (Vertex AI)** makes the model's internal logic opaque (a "black box within a black box"). While accurate, it is difficult to determine *which* anatomical features (e.g., vessel tortuosity vs. disc edema) the model is using to substitute for angiography, which may lead to clinical skepticism.

## 🔗 Discovery & Next Steps
- **Implementation:** Future work should explore fine-tuning **RETFound** on this specific UWFFP dataset to see if pre-trained retinal grammar improves the 0.94 AUC.
- **Concept Link:** Foundational to [Oculomics](../concepts/oculomics.md) and [Objective Inflammation Grading](../concepts/objective_inflammation_grading.md).
