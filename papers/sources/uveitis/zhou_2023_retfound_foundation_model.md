---
title: "RETFound: A Foundation Model for Generalizable Disease Detection"
authors: ['Zhou et al.']
year: 2023
lab: "UCL / Moorfields Eye Hospital (UK)"
venue: "Nature"
doi: "TBD"
code: "TBD"
datasets: ["TBD"]
tags: ["TBD"]
---

# RETFound: A Foundation Model for Generalizable Disease Detection

## 📋 Executive Summary
The study introduces RETFound, a large-scale foundation model for ophthalmology, demonstrating its ability to detect various diseases with high generalizability and performance, especially when labeled data is scarce.

## 🛠️ Core Methodology
- **Self-Supervised Learning (SSL):** Trained on 1.6 million unlabeled retinal images using a Masked Autoencoder (MAE) architecture.
- **MAE Architecture:** Randomly masks 75% of input image patches and trains the model to reconstruct them, learning robust spatial features.
- **Dataset:** Integrated large-scale clinical image datasets from the NHS (UK) and Stanford (USA).

## 📊 Dataset & Experimental Setup
TBD

## 💡 Key Findings
- **Superior Performance:** Outperforms traditional supervised models in multiple clinical tasks, including diabetic retinopathy, glaucoma, and age-related macular progression.
- **Data Efficiency:** Demonstrates high performance even when fine-tuned on very small labeled datasets (e.g., <100 images).
- **Generalizability:** The model's features generalize across different imaging devices and patient populations.

## 🩺 Clinical Relevance & Impact
- **Sparse Data in Uveitis:** Provides a powerful tool for feature extraction in rare uveitis cases where large labeled datasets are unavailable.
- **Standardized Foundation:** Establishes a benchmark for building future ophthalmic AI systems on a pre-trained base.

## 🔬 Critical Review (Antagonic Perspective)
TBD

## 🔗 Discovery & Next Steps
TBD
