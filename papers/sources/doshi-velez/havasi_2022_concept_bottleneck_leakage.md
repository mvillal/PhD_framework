---
title: "Addressing Leakage in Concept Bottleneck Models"
authors: ["Márton Havasi", "Sonali Parbhoo", "Finale Doshi-Velez"]
year: 2022
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "NeurIPS"
doi: "10.52202/068431-1699"
url: "https://proceedings.neurips.cc/paper_files/paper/2022/hash/9597353a40ffc4ad5416de1651c0147e-Abstract-Conference.html"
tags: ["Concept Bottleneck Models", "Interpretability", "Information Leakage", "Psychiatric Diagnosis"]
---

# Addressing Leakage in Concept Bottleneck Models

## 📋 Executive Summary
Concept Bottleneck Models (CBMs) are designed to be interpretable by first predicting high-level human concepts and then using those concepts to predict the final label. This paper identifies a critical failure mode: **information leakage**, where the "soft" concept representations inadvertently encode more information than the intended concepts, allowing the model to "cheat" and bypass the intended bottleneck.

## 🛠️ Core Methodology
- **Concept Bottleneck Models (CBMs):** Architectures that use a concept layer as an intermediate representation.
- **Leakage Analysis:** Demonstrates how high-dimensional soft concepts can leak information from the original input that is unrelated to the defined concepts.
- **Mitigation Strategies:** Proposes methods to reduce leakage, ensuring that the model relies solely on the intended semantic meaning of the concepts.

## 📊 Dataset & Experimental Setup
- Evaluated on benchmark datasets (e.g., CUB-200-2011) and clinical proxy tasks.

## 💡 Key Findings
- Standard CBMs often exhibit leakage, meaning their "interpretability" is partially illusory.
- Humans intervening on concepts in a leaking model may lead to unpredictable or suboptimal results because the model is using latent features.
- Reducing leakage restores the integrity of human-in-the-loop interventions.

## 🩺 Clinical Relevance & Impact
Ensures that psychiatric diagnostic tools using human-understandable symptoms (concepts like "anhedonia" or "sleep disturbance") are actually using those symptoms to make a diagnosis, rather than "cheating" via latent, uninterpretable features in the EHR. This is crucial for trust and clinical validation.

## 🔬 Critical Review (Antagonic Perspective)
While CBMs aim for interpretability, this work proves that "soft" concepts are inherently risky. There is a fundamental trade-off: higher concept fidelity (low leakage) often comes at the cost of overall predictive accuracy. Furthermore, defining the "right" set of concepts remains a human-subjective process that can introduce its own biases.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Koh et al. (2020) for the original Concept Bottleneck Model proposal.
- **Descendant Discovery:** Exploring "Hard" vs. "Soft" bottleneck constraints in psychiatric symptom modeling.
