---
title: "RETFound-Green: Sustainable and Lightweight Ophthalmic Foundation Models"
authors: ["Justin Engelmann", "Miguel O. Bernabeu", "Pearse Keane (Contributor)"]
year: 2025
lab: "University of Edinburgh / Moorfields Eye Hospital"
venue: "Nature Communications"
doi: "10.1038/s41467-025-XXXXX"
code: "https://github.com/m-o-bernabeu-lab/retfound-green"
datasets: ["75k Retinal Images"]
tags: ["Sustainable AI", "RETFound-Green", "Token Reconstruction", "Lean Learning", "Low-Resource AI"]
---

# RETFound-Green: Sustainable Ophthalmic Foundation Models

## 📋 Executive Summary
Engelmann et al. (2025) introduce **RETFound-Green**, a sustainable and computationally efficient successor to the original RETFound model. While foundation models often require massive GPU clusters and energy, RETFound-Green matches the performance of the 2023 original while requiring **400x less compute** and **95% less data** for pre-training. This study democratizes ophthalmic AI, allowing state-of-the-art models to be trained and deployed in low-resource settings and on consumer-grade hardware.

## 🛠️ Core Methodology
- **Token Reconstruction (SSL):** Unlike the original model that learned from pixel-level missing patches, RETFound-Green utilizes high-level "token reconstruction." This allows the model to learn the semantic structure of the retina much faster and with less data.
- **Efficiency Bottleneck:** Focused on reducing the "Carbon Cost" of medical AI by optimizing the training lifecycle.
- **Hardware Agnostic:** Designed to be small enough (14x smaller) to run on mobile devices and edge hardware.

## 📊 Dataset & Experimental Setup
- **Pre-training:** Only **75,000 images** (vs. 1.6 million for the original).
- **Compute:** Trained on a single consumer GPU for less than £50.
- **Benchmarks:** Evaluated on 119 clinical tasks across ocular and systemic health.

## 💡 Key Findings
- **Parity with Scale:** Despite the 95% reduction in training data, RETFound-Green achieved performance parity with the original 1.6M-image model across almost all tasks.
- **Sustainability:** Reduced the training carbon footprint by over 99%.
- **Speed:** 2.6x faster inference, enabling real-time screening on standard smartphones.

## 🩺 Clinical Relevance & Impact
The development of RETFound-Green is critical for **Global Health Equity**. It enables hospitals in LMICs (Low-and-Middle-Income Countries) to build their own local models for endemic diseases without the need for massive data centers. It also aligns with the vision of **Sustainable Healthcare** promoted by leaders like Dr. Frances Mortimer.

## 🔬 Critical Review (Antagonic Perspective)
While the "Green" model is efficient, its heavy reliance on high-level token reconstruction might cause it to miss extremely subtle, low-level pixel-intensity anomalies that could be relevant for rare "Oculomics" biomarkers.

## 🔗 Discovery & Next Steps
- **Implementation:** Explore `sam2.build_sam2` patterns (fetched via Context7) for mobile-ready ophthalmic segmentation tasks.
- **Concept Link:** Updates [Ophthalmic Foundation Models](../concepts/ophthalmic_foundation_models.md).
