---
title: "Objective Inflammation Grading"
concept_type: "Diagnostic Methodology"
tags: ["Uveitis", "OCT", "Segmentation", "U-Net", "UWF"]
sources: ["../../sources/uveitis/haggag_2021_oct_vitreous_haze_grading.md", "../../sources/uveitis/mohammadi_2026_uwf_inflammation_detection.md"]
---

# Objective Inflammation Grading

## 📋 Definition
Objective Inflammation Grading refers to the use of automated computer vision tools to quantify ocular inflammation, moving away from subjective clinician-reported scales like the Standardized Uveitis Nomenclature (SUN).

## 🛠️ Key Technical Components
- **U-Net Segmentation**: Automated segmentation of the vitreous region and the Retinal Pigment Epithelium (RPE) in OCT B-scans (Haggag et al., 2021).
- **VIT/RPE Intensity Ratio**: An objective metric for vitreous haze calculated by comparing the mean pixel intensity of the vitreous to a stable anatomical reference (the RPE).
- **Ultra-Widefield (UWF) Surrogates**: Deep learning models trained on UWF color fundus photography (Mohammadi et al., 2026) to detect posterior inflammation features (e.g., vasculitis, peripheral leakage) that typically require invasive Fluorescein Angiography (FA).

## 🩺 Clinical Relevance
- **Clinical Trial Endpoints**: Provides reproducible and sensitive metrics for assessing treatment efficacy in clinical trials.
- **Non-Invasive Monitoring**: Reduces the need for repeated dye injections (Fluorescein) by using standard color photography as a surrogate for activity detection.

## 🔗 Related Concepts
- [Ophthalmic Foundation Models](ophthalmic_foundation_models.md)
- [Learning to Defer (L2D)](learning_to_defer.md)
