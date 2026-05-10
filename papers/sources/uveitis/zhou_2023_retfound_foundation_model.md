---
title: "A foundation model for generalizable disease detection from retinal images"
authors: ["Yukun Zhou", "et al."]
year: 2023
lab: "Keane Lab, Moorfields Eye Hospital / UCL"
venue: "Nature"
doi: "10.1038/s41586-023-06555-x"
code: "https://github.com/microsoft/retfound"
datasets: ["1.6M Retinal Images", "UK Biobank", "Moorfields-EHR"]
tags: ["RETFound", "Foundation Model", "Retinal Imaging", "Self-Supervised Learning", "Oculomics"]
---

# RETFound: A Foundation Model for Retinal Imaging

## 📋 Executive Summary
Zhou et al. (2023) introduce **RETFound**, the first medical foundation model specifically designed for retinal imaging. By training on 1.6 million unlabeled retinal images (color fundus photographs and OCT scans) using self-supervised learning (SSL), the model learns a "grammar" of the human retina. This allows it to be fine-tuned for specific tasks with significantly less expert-labeled data, proving highly effective for detecting both ocular diseases and systemic health conditions (Oculomics).

## 🛠️ Core Methodology
- **Architecture:** Uses a **Masked Autoencoder (MAE)** based on Vision Transformers (ViT).
- **Self-Supervised Learning:** The model is trained to reconstruct missing patches of retinal images, forcing it to learn meaningful spatial and physiological features without explicit labels.
- **Fine-Tuning:** The pre-trained weights are then adapted to task-specific labels (e.g., diabetic retinopathy vs. Parkinson's risk) using a simple linear head.
- **Multimodal Support:** Capable of processing both 2D fundus photos and 3D OCT scans.

## 📊 Dataset & Experimental Setup
- **Pre-training:** 1.6 million unlabeled images from Moorfields Eye Hospital.
- **Evaluation:** Benchmarked against standard supervised models (ResNet, Inception) on tasks including glaucoma, AMD, heart failure, myocardial infarction, and Parkinson’s disease.
- **Validation:** Tested on diverse external cohorts including the UK Biobank and Singapore-based datasets.

## 💡 Key Findings
- **Generalizability:** RETFound consistently outperformed standard supervised models, especially on "Oculomics" tasks where features are subtle.
- **Label Efficiency:** Achieved high diagnostic performance even when trained on only 1% to 10% of the usual expert-labeled data.
- **Fairness:** Demonstrated robust and fair performance across multiple ethnic groups and clinical sites.

## 🩺 Clinical Relevance & Impact
RETFound represents a paradigm shift in clinical AI, moving away from "one-model-per-disease" to a single, generalizable platform. It establishes the eye as a reliable, non-invasive "window" to systemic health, enabling large-scale cardiovascular and neurological screening through routine optometric scans.

## 🔬 Critical Review (Antagonic Perspective)
While RETFound is efficient, its MAE architecture is computationally intensive to train initially. Furthermore, the "Oculomics" predictions (e.g., Parkinson's) still require large-scale longitudinal verification before they can be used for clinical diagnosis rather than just "risk stratification."

## 🔗 Discovery & Next Steps
- **Implementation:** Utilize `monai.networks.nets.ViT` patterns for fine-tuning foundation models on custom volumetric OCT data.
- **Entity Link:** Foundational to [UCL Moorfields](../entities/ucl_moorfields.md) and [Oculomics](../concepts/oculomics.md).
