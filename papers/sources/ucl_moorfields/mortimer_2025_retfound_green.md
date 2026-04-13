---
title: "RETFound-Green: Smartphone-Optimized Foundation Models for Global Oculomics"
authors: ["R. Mortimer", "Y. Zhou", "Pearse Keane"]
year: 2025
lab: "UCL Institute of Ophthalmology / Moorfields Eye Hospital"
venue: "Lancet Digital Health (Accepted)"
doi: "TBD"
code: "Moorfields Research GitHub"
datasets: ["Moorfields-Global", "Singapore-OASIS", "NIH-Eye"]
tags: ["Foundation Models", "Oculomics", "Smartphone AI", "Global Health", "RETFound"]
---

# RETFound-Green: Smartphone-Optimized Foundation Models for Global Oculomics

## 📋 Executive Summary
RETFound-Green is a distilled, "green AI" version of the original 2023 RETFound foundation model. It is specifically optimized to run on smartphone hardware while maintaining the capability to detect not only ocular diseases but also systemic conditions (Parkinson's, kidney disease) via "oculomics." This represents a major leap in global health equity.

## 🛠️ Core Methodology
- **Knowledge Distillation:** Compressing the 300M+ parameter RETFound model into a lean version (<50M parameters) using a novel student-teacher architecture.
- **Multimodal Oculomics:** Training the model to recognize retinal signatures of systemic health using data from global biobanks.
- **On-Device Inference:** Specialized kernels for low-power processing on standard smartphone chips, enabling real-time screening without cloud connectivity.

## 📊 Dataset & Experimental Setup
- **Data Source:** Expansion of the RETFound dataset to 100 million images, with a focus on diverse ethnicities (Global South cohorts).
- **Validation:** Clinical validation across multiple sites in the UK, Singapore, and West Africa.

## 💡 Key Findings
- **High Sensitivity:** Maintains >90% of the original model's accuracy for major eye diseases like Diabetic Retinopathy.
- **Systemic Forecasting:** Successfully detected early signs of Parkinson's Disease from standard fundus photos with a high degree of correlation to clinical diagnosis.
- **Energy Efficiency:** 80% reduction in inference energy consumption, making it viable for rural, off-grid clinical settings.

## 🩺 Clinical Relevance & Impact
Enables high-quality clinical screening in low-resource settings where expensive fundus cameras and expert ophthalmologists are unavailable. It transforms the smartphone into a powerful diagnostic tool for both eye and systemic health.

## 🔬 Critical Review (Antagonic Perspective)
The reliance on smartphone camera quality introduces significant data variability. While the model is "Green," the initial 100M image pre-training process remains computationally and environmentally expensive.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Zhou et al. (2023) RETFound.
- **Descendant Discovery:** Clinical deployment in national screening programs in Southeast Asia (2026).
