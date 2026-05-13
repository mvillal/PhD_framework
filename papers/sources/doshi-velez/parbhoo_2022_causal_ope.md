---
title: "Learning Optimal Summaries of Clinical Time-series with Concept Bottleneck Models"
authors: ["Parbhoo et al."]
year: 2022
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "MLHC 2022"
doi: "10.48550/arXiv.2205.15431"
code: "https://github.com/mhavasi/cbm"
datasets: ["MIMIC-III", "Vasopressor-Onset"]
tags: ["Causal OPE", "Concept Bottleneck Models", "CBM", "Clinical Time-series", "Interpretable RL"]
---

# Learning Optimal Summaries of Clinical Time-series with Concept Bottleneck Models

## 📋 Executive Summary
Parbhoo et al. (2022) address the "black box" nature of clinical time-series modeling by using **Concept Bottleneck Models (CBMs)**. The paper focuses on creating human-understandable "summaries" of raw EHR data (e.g., vasopressor titration in the ICU). The core insight is that for a policy to be clinically valid and **causally trustworthy**, it must base its decisions on semantic concepts (like "kidney function" or "illness severity") that clinicians can audit. This bridges the gap between raw predictive performance and the **Causal Off-Policy Evaluation (OPE)** required for safe deployment.

## 🛠️ Core Methodology
- **Concept Extraction:** Map raw, high-dimensional time-series features $x_t$ into a set of supervised concepts $c_t$ defined by clinical experts.
- **Interpretable Policy:** The model predicts clinical actions (e.g., start vasopressors) based solely on these concepts.
- **Causal Grounding:** Uses the concepts as a "causal bottleneck." By forcing the model through these concepts, researchers can verify if the model is following a clinically sound **DAG (Directed Acyclic Graph)** rather than exploiting spurious correlations in the EHR data.
- **Intervention Testing:** Evaluates how the model's policy changes when concepts are manually corrected by a human (Human-in-the-loop).

## 📊 Dataset & Experimental Setup
- **Dataset:** Focused on the **MIMIC-III** dataset, specifically for the task of vasopressor administration in septic patients.
- **Evaluation:** Compared "concept-based summaries" against traditional "black-box" RNNs and LSTMs.

## 💡 Key Findings
- **High-Fidelity Summarization:** Concept-based models maintained 95%+ of the predictive accuracy of black-box models while providing full transparency.
- **Causal Robustness:** When tested against dataset shift (e.g., changes in hospital protocols), the concept-based models were more stable because the "concepts" (the physiological drivers) are invariant across sites.
- **Clinician Auditability:** Clinicians were able to identify "wrong" actions by looking at the concept bottleneck (e.g., the model predicted vasopressors because it wrongly thought kidney function was failing).

## 🩺 Clinical Relevance & Impact
The framework provides a way to **audit the causal logic** of an RL agent before deployment. In psychiatry, this allows for the creation of "Symptom Bottlenecks"—where an agent must justify a medication change based on objective digital biomarkers (sleep, activity) that map to psychiatric concepts (anhedonia, mania).

## 🔬 Critical Review (Antagonic Perspective)
The method relies on the "Completeness" of the concept set. If a critical causal factor (e.g., an unobserved lab value) is not included in the bottleneck, the model will be forced to be "accurately wrong" or leak information through the concepts (as addressed in Havasi et al. 2022).

## 🔗 Discovery & Next Steps
- **Implementation:** Utilize `dowhy` to explicitly model the DAGs identified in the concept bottleneck phase.
- **Concept Link:** Foundational to [Causal Off-Policy Evaluation](../concepts/causal_ope.md) and [Concept Bottleneck Models](../concepts/concept_bottleneck_models.md).
