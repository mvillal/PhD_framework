---
title: "Computer-Aided Grading of Vitreous Haze using Optical Coherence Tomography"
authors: ["Sayed Haggag", "et al."]
year: 2021
lab: "Collaborative Research"
venue: "Sensors"
doi: "10.3390/s21XXXXX"
code: "N/A"
datasets: ["200 SD-OCT Images"]
tags: ["Vitreous Haze", "OCT", "Grading", "U-Net", "FCNN", "Quantitative Biomarkers"]
---

# Objective Vitreous Haze Grading using OCT

## 📋 Executive Summary
Haggag et al. (2021) introduce an automated Computer-Aided Diagnostic (CAD) system for the objective grading of vitreous haze in patients with uveitis. Traditional grading (SUN criteria) relies on subjective clinical inspection, which has high inter-observer variability. This CAD system uses **Optical Coherence Tomography (OCT)** to quantify haze levels, providing a reproducible and quantitative biomarker for ocular inflammation.

## 🛠️ Core Methodology
- **Automated Vitreous Segmentation:** Uses a **U-net Convolutional Neural Network (U-CNN)** to segment the vitreous region. It incorporates "fused images" (original OCT + shape priors) to improve precision in low-contrast scans.
- **Inflammation Grading:** Extracts the **Cumulative Distribution Function (CDF)** of signal intensities within the segmented vitreous.
- **Classification:** A **Fully Connected Neural Network (FCNN)** classifies the haze into grades 0 to 3 based on the CDF signature.

## 📊 Dataset & Experimental Setup
- **Modality:** Spectral Domain OCT (SD-OCT).
- **Dataset:** 200 OCT images representing various inflammation severities.
- **Metrics:** Dice Coefficient of 0.988 for segmentation; 86% average accuracy for grading.

## 💡 Key Findings
- **High Precision:** The model demonstrated exceptionally high segmentation accuracy (98.8%), critical for reliable quantification.
- **Clinical Correlation:** The AI grades showed strong correlation with human expert consensus while eliminating the subjectivity inherent in manual SUN grading.
- **Robustness:** The CDF-based feature extraction was effective at distinguishing subtle differences in signal intensity that characterize early-stage vitritis.

## 🩺 Clinical Relevance & Impact
The system enables **Objective Monitoring** of treatment response. Clinicians can use these AI-generated scores to detect minor changes in inflammation that are invisible to the eye, allowing for faster titration of steroids and better preservation of vision.

## 🔬 Critical Review (Antagonic Perspective)
The study uses a relatively small dataset (200 images). For this to be a universal "gold standard," it requires validation on a wider variety of OCT hardware (Heidelberg vs. Zeiss) and more diverse uveitis etiologies, as different inflammatory particles may scatter light differently.

## 🔗 Discovery & Next Steps
- **Implementation:** Utilize `monai` segmentation patterns to implement similar U-Net pipelines for custom vitreous datasets.
- **Concept Link:** Foundational to [Objective Inflammation Grading](../concepts/objective_inflammation_grading.md).
