---
title: "Causal Off-Policy Evaluation for Sequential Decisions"
authors: ["Sonali Parbhoo", "Alihan Hüyük", "Finale Doshi-Velez"]
year: 2022
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "Nature Machine Intelligence / MLHC"
doi: "10.1038/s42256-022-00475-7"
url: "https://www.nature.com/articles/s42256-022-00475-7"
datasets: ["HIV (ACTG 175)", "Sepsis Simulators"]
tags: ["Causal Inference", "OPE", "Sequential Decision-Making", "Transportability", "Hidden Confounding"]
---

# Causal Off-Policy Evaluation for Sequential Decisions

## 📋 Executive Summary
This paper introduces a framework for Causal Off-Policy Evaluation (OPE) that explicitly addresses hidden confounding and transportability in clinical settings. By leveraging Structural Causal Models (SCMs), the authors derive optimality guarantees and identification conditions for policy evaluation using observational data, move beyond standard statistical correlations to causal estimands.

## 🛠️ Core Methodology
- **Causal Transportability:** A framework to determine if a policy evaluated in one population (e.g., an RCT) can be safely applied to a different observational cohort.
- **SCM-based OPE:** Use of Structural Causal Models to define the causal mechanisms and identify treatment effects even in the presence of unmeasured confounders.
- **Optimality Bounds:** Derivation of upper and lower bounds for the expected value (V) of a target policy under various causal assumptions.

## 📊 Dataset & Experimental Setup
- **Data Source:** Validated using the ACTG 175 trial data (HIV) and various sepsis simulators.
- **Features:** Treatment histories (e.g., zidovudine monotherapy vs. combination therapy) and long-term outcomes (CD4 cell counts).
- **Evaluation Metrics:** Causal Identifiability conditions and Value Estimation Error (MSE).

## 💡 Key Findings
- **Identification Conditions:** The study identifies the specific causal structures (e.g., front-door/back-door criteria) that must hold for OPE to be valid in healthcare.
- **Transportability Logic:** Successfully demonstrates how a policy's performance can "transfer" across different patient distributions without retraining.
- **Improved HIV Policy:** Identifies treatment strategies in HIV care that would have outperformed historical clinical practice by specifically accounting for population-level causal shifts.

## 🩺 Clinical Relevance & Impact
Provides a rigorous foundation for Precision Psychiatry, where treatment effects must be personalized but are often derived from sparse, observational EHR data. The causal framework ensures that recommended changes (e.g., antidepressant switches) are based on true causal impact rather than observational bias.

## 🔬 Critical Review (Antagonic Perspective)
The framework assumes that the researcher can correctly specify the underlying SCM, which is a significant hurdle in psychiatry where the causal pathways are often unknown or partially observed. Specification errors in the SCM could lead to biased causal estimates that are worse than simple statistical models.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Pearl (2009) on Causal Inference.
- **Descendant Discovery:** Hüyük & Doshi-Velez (2025) on Strategic Link Scores as an extension of causal dependency modeling.
