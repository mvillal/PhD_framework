---
title: "Interpretable multi-model deep learning framework for automated four-class diagnosis of ocular toxoplasmosis using fundus imaging"
authors: ["Laraib Umer", "Javed Iqbal", "et al."]
year: 2025
lab: "Collaborative (Nature Portfolio)"
venue: "Scientific Reports"
doi: "10.1038/s41598-025-XXXXX"
code: "https://github.com/ultralytics/ultralytics (YOLOv11)"
datasets: ["OT-Fundus-FourClass-Registry"]
tags: ["Ocular Toxoplasmosis", "YOLOv11", "Infectious Uveitis", "Real-Time AI", "Interpretable AI", "Lesion Localization"]
---

# Automated Diagnosis of Ocular Toxoplasmosis using YOLOv11

## 📋 Executive Summary
Umer et al. (2025) introduce a state-of-the-art deep learning framework for the automated diagnosis of **Ocular Toxoplasmosis (OT)**—the leading cause of infectious posterior uveitis. Moving beyond binary detection, the framework achieves high-precision classification into four clinically critical categories: **Active Lesions**, **Inactive Scars**, **Mixed Presentation**, and **Healthy Retina**. The core of the system is a **YOLOv11** architecture, which enables both lesion localization and rapid classification, making it suitable for real-time clinical decision support and teleophthalmology.

## 🛠️ Core Methodology
- **AI Architecture:** Utilizes **YOLOv11** (You Only Look Once) for anchor-free object detection and classification.
- **Task Formulation:** A four-class classification problem designed to distinguish between active parasitic inflammation and historical scarring.
- **Interpretability:** Integrates **SHAP (Shapley Additive Explanations)** and **EigenCAM** to generate pathological heatmaps, ensuring the model focuses on retinochoroidal lesions rather than image noise.
- **High-Speed Inference:** Optimized for low-latency deployment (2.8ms on GPU), facilitating mobile screening in resource-limited settings.

## 📊 Dataset & Experimental Setup
- **Dataset:** A diverse registry of fundus images curated for OT lesion variety (active vs. inactive).
- **Performance:** Achieved a landmark **98% classification accuracy** and a Matthew's Correlation Coefficient (MCC) of 0.885.
- **Benchmarking:** Outperformed standard CNN (ResNet) and Vision Transformer (Swin-T) baselines in both speed and robustness.

## 💡 Key Findings
- **Superior Localization:** YOLOv11's ability to localize lesions significantly improved the model's accuracy on "mixed" eyes where both scars and active inflammation are present.
- **Real-Time Readiness:** The model's speed on CPU (65ms) confirms its potential for deployment on standard clinical laptops without specialized hardware.
- **Pathological Grounding:** Visualization confirmed that the AI "looks" at lesion borders and vitreous haze patches to determine activity.

## 🩺 Clinical Relevance & Impact
The framework provides a reliable **Decision Support System** for managing infectious uveitis. By distinguishing active from inactive toxoplasmosis, it helps prevent unnecessary antiparasitic treatment for healed scars while ensuring that active flare-ups are treated aggressively to prevent permanent vision loss. It is a cornerstone of the move toward **Digital Uveitis Clinics**.

## 🔬 Critical Review (Antagonic Perspective)
The study relies on fundus imaging alone. In clinical practice, OT diagnosis often requires **multimodal verification** (e.g., OCT or serology). An AI model that only looks at a 2D photograph may miss deep-seated inflammation or subretinal fluid that is critical for determining lesion "activity."

## 🔗 Discovery & Next Steps
- **Implementation:** Explore using the `ultralytics` YOLOv11 package for fine-tuning on other infectious uveitis datasets (e.g., Acute Retinal Necrosis).
- **Concept Link:** Updates [Objective Inflammation Grading](../concepts/objective_inflammation_grading.md).
