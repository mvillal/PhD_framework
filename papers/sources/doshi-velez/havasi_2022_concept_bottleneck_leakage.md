---
title: "Addressing Leakage in Concept Bottleneck Models"
authors: ["Havasi et al."]
year: 2022
lab: "Data to Actionable Knowledge Lab (DtAK) / Harvard"
venue: "NeurIPS 2022"
doi: "https://doi.org/10.48550/arXiv.2205.15431"
code: "https://github.com/mhavasi/cbm"
datasets: ["CUB-2011", "MIMIC-III"]
tags: ["Concept Bottleneck Models", "CBM", "Information Leakage", "Interpretability", "Side-Channel"]
---

# Addressing Leakage in Concept Bottleneck Models

## 📋 Executive Summary
Havasi et al. (2022) identify and solve a critical flaw in **Concept Bottleneck Models (CBMs)**: information leakage. While CBMs are designed to be interpretable by predicting human-defined concepts (e.g., "fluid in lungs") before the final label (e.g., "Heart Failure"), "Soft CBMs" often leak extra label-related information through the concept probabilities. This "cheating" makes models appear accurate but breaks their **intervenability**—correcting a concept doesn't fix the final prediction because the model relies on the leaked signal. This paper introduces the **Side-Channel CBM**, which restores predictive performance to Hard CBMs without sacrificing the semantic integrity of the concepts.

## 🛠️ Core Methodology
- **Leakage Identification:** Formally proves that Soft CBMs can encode non-concept information in the high-entropy regions of the concept distribution.
- **Side-Channel Architecture:** Introduces a set of **unlabeled latent concepts** alongside the supervised ones. This "side channel" absorbs all necessary information for the task that isn't captured by the human-defined concepts, keeping the bottleneck "clean."
- **Autoregressive Concept Predictor:** Instead of predicting concepts independently, the model predicts them sequentially ($P(c_i | x, c_{<i})$). This captures correlations between concepts (e.g., if "wing" is present, "feather" is likely), improving accuracy without leakage.

## 📊 Dataset & Experimental Setup
- **Evaluation:** Benchmarked on **CUB-2011** (bird species classification) and **MIMIC-III** (clinical mortality and diagnosis).
- **Metric:** Focused on **Intervention Accuracy**—how much the final prediction improves when a human provides the correct ground-truth for a subset of concepts.

## 💡 Key Findings
- **Clean Bottlenecks:** The Side-Channel CBM matches the accuracy of black-box models while maintaining a "pure" concept bottleneck.
- **Intervention Superiority:** On MIMIC-III, the proposed model showed significantly higher improvement during human intervention compared to leaky Soft CBMs.
- **Markovian Assumption:** The paper demonstrates that the traditional CBM's failure is often due to the "Markovian assumption" (concepts containing all info) being false in complex clinical domains.

## 🩺 Clinical Relevance & Impact
In psychiatry, where concepts (e.g., "anhedonia," "sleep disturbance") are subjective and interlinked, the Side-Channel CBM allows for **Trustworthy AI**. Clinicians can correct a misinterpreted symptom, and the model will update its risk forecast in a way that is logically consistent with that correction, rather than being "stuck" on a leaked, uninterpretable signal.

## 🔬 Critical Review (Antagonic Perspective)
The introduction of the "Side-Channel" (latent concepts) effectively re-introduces a **black-box component** into the interpretable model. While the *supervised* concepts remain pure, the final decision still depends on uninterpretable latent features, which may hide their own biases.

## 🔗 Discovery & Next Steps
- **Implementation:** Explore the `ValidationNode` pattern in LangGraph to ensure that agents providing concept labels are audited for consistency.
- **Concept Link:** Updates [Concept Bottleneck Models](../concepts/concept_bottleneck_models.md).
