---
title: "Automated early detection of acute retinal necrosis from ultra-widefield color fundus photography using deep learning"
authors: ["Liao et al.", "Eye Hospital of Wenzhou Medical University"]
year: 2024
lab: "Eye Hospital of Wenzhou Medical University"
venue: "Eye and Vision / IOVS (ARVO)"
doi: "https://doi.org/10.1167/iovs.65.1.34"
url: "https://doi.org/10.1167/iovs.65.1.34"
code: "N/A"
datasets: ["Multicenter Dataset (11,508 images)"]
tags: ["DeepDrARN", "Swin Transformer", "Acute Retinal Necrosis", "ARN", "Uveitis"]
---

# Automated Early Detection of Acute Retinal Necrosis (Liao et al., 2024)

## Summary
The study develops and validates **DeepDrARN**, a deep learning framework based on the **Swin Transformer** architecture, for the automated and early detection of Acute Retinal Necrosis (ARN) using ultra-widefield color fundus photography (UWFCFP).

## Methodology
- **DeepDrARN Model:** Developed using the Swin Transformer architecture to capture high-resolution features from UWF images.
- **Multicenter Study:** Trained and validated using a large dataset of **11,508 images** from 1,112 participants across multiple clinical sites.
- **Comparison:** Performance compared against seven independent ophthalmologists.

## Findings
- **High Accuracy:** Achieved an AUROC of **0.996** (internal) and **0.973** (external) for general uveitis screening, and **0.960–0.971** for ARN identification.
- **Human Outperformance:** The model outperformed seven ophthalmologists, increasing diagnostic accuracy by **6.57%** for uveitis and **11.14%** for ARN.
- **Clinical Utility:** Highlights the potential for fast, low-cost early intervention in sight-threatening viral uveitis.

## Relevance
- **Early Intervention:** Crucial for ARN management to prevent irreversible vision loss and retinal detachment.
- **Scalable Diagnostics:** Demonstrates the power of transformer architectures in high-resolution medical imaging for rare infectious diseases.
