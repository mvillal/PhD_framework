---
title: "Concept Bottleneck Models (CBMs)"
concept_type: "Interpretable Architecture"
tags: ["Interpretability", "Information Leakage", "Symptom Modeling"]
sources: ["../../sources/doshi-velez/havasi_2022_concept_bottleneck_leakage.md", "../../sources/doshi-velez/parbhoo_2022_causal_ope.md"]
---

# Concept Bottleneck Models (CBMs)

## 📋 Definition
Concept Bottleneck Models (CBMs) are neural network architectures that first map input data to a set of human-interpretable "concepts" (e.g., clinical symptoms like anhedonia or sleep disturbance) before using those concepts to predict a final outcome or diagnosis.

## 🛠️ Key Technical Components
- **The Bottleneck Layer**: A restricted layer where each neuron corresponds to a predefined semantic concept.
- **Information Leakage**: A critical failure mode where "soft" concept representations encode more information than the intended concept, allowing the model to bypass the interpretable bottleneck (Havasi et al., 2022).
- **Causal Alignment**: For CBMs to be truly useful in clinical reasoning, the concepts must have a causal relationship with the outcome (Parbhoo et al., 2022), ensuring that interventions on the concepts (e.g., treating sleep) lead to predictable changes in the final prediction.

## 🩺 Clinical Relevance
- **Trust and Validation**: Clinicians can inspect the concept layer to verify if the model is "reasoning" correctly (e.g., is the depression diagnosis actually driven by observed symptoms?).
- **Human-in-the-Loop**: Allows clinicians to intervene directly on the concepts (e.g., "correcting" an AI-detected symptom) and see the immediate impact on the final output.

## 🔗 Related Concepts
- [Learning to Defer (L2D)](learning_to_defer.md)
- [Objective Inflammation Grading](objective_inflammation_grading.md)
