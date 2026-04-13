---
title: "Ophthalmic Foundation Models"
concept_type: "Architectural Pattern"
tags: ["Foundation Models", "SSL", "Ophthalmology", "RETFound"]
sources: ["../../sources/uveitis/zhou_2023_retfound_foundation_model.md"]
---

# Ophthalmic Foundation Models

## 📋 Definition
Ophthalmic Foundation Models are large-scale neural networks pre-trained on massive datasets of unlabeled clinical images (e.g., retinal fundus or OCT) using self-supervised learning. These models serve as a general-purpose feature extractor that can be fine-tuned for a wide variety of downstream clinical tasks.

## 🛠️ Key Technical Components
- **Self-Supervised Learning (SSL)**: Models like **RETFound** (Zhou et al., 2023) are trained on over 1.6 million unlabeled images.
- **Masked Autoencoders (MAE)**: The architecture typically involves masking large portions of the input image (e.g., 75%) and tasking the model with reconstructing the missing patches, forcing it to learn robust spatial representations of ocular anatomy.
- **Data Efficiency**: Foundation models significantly reduce the amount of labeled data required for new tasks, demonstrating high performance even with fewer than 100 labeled examples.

## 🩺 Clinical Applications
- **Rare Disease Detection**: Particularly effective for conditions like uveitis where large, labeled datasets are difficult to compile.
- **Generalizability**: These models demonstrate superior "transportability" across different imaging devices (e.g., Topcon vs. Zeiss) and diverse patient populations compared to traditional supervised models.

## 🔗 Related Concepts
- [Objective Inflammation Grading](objective_inflammation_grading.md)
- [Concept Bottleneck Models](concept_bottleneck_models.md)
