---
title: "Guidelines for Reinforcement Learning in Healthcare"
authors: ["Omer Gottesman", "Joseph Futoma", "Yao Liu", "Finale Doshi-Velez"]
year: 2019
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "Nature Medicine"
doi: "10.1038/s41591-018-0310-5"
url: "https://www.nature.com/articles/s41591-018-0310-5"
datasets: ["MIMIC-III", "eICU"]
tags: ["Reinforcement Learning", "Off-Policy Evaluation", "Healthcare AI", "FQE", "Batch RL"]
---

# Guidelines for Reinforcement Learning in Healthcare

## 📋 Executive Summary
This paper establishes the foundational guidelines for applying Reinforcement Learning (RL) to clinical data. Recognizing the unique challenges of healthcare (safety, sparse data, confounding), the authors provide a rigorous checklist for evaluating clinical RL, emphasizing the necessity of robust Off-Policy Evaluation (OPE) and stakeholder engagement.

## 🛠️ Core Methodology
- **Offline/Batch RL:** The standard for clinical settings where interaction with patients is not possible during training.
- **Fitted Q-Evaluation (FQE):** A primary technique for estimating the value (expected reward) of a new clinical policy using historical data.
- **Robustness to Unmeasured Confounding:** Frameworks for assessing how hidden variables might bias the RL agent's learned policy.
- **Bootstrapping and Uncertainty:** Using ensemble methods or bootstrapping to quantify the agent's confidence in its recommended actions.

## 📊 Dataset & Experimental Setup
- **Data Source:** Demonstrations and evaluations using MIMIC-III (Medical Information Mart for Intensive Care) and eICU Collaborative Research Database.
- **Clinical Task:** Management of sepsis (fluid and vasopressor titration) and sedation levels in ventilated patients.
- **Evaluation Metrics:** Expected Value (V), Effective Sample Size (ESS), and Weighted Importance Sampling (WIS) for policy evaluation.

## 💡 Key Findings
- **Checklist for Clinical RL:** Defines mandatory steps for researchers, including data preprocessing, policy safety constraints, and clinical sanity checks.
- **OPE Reliability:** Demonstrates that FQE provides more stable estimates of clinical policy performance compared to standard importance sampling in sparse data regimes.
- **Deadly Triad Management:** Strategies to avoid divergence (the "deadly triad") when combining function approximation, bootstrapping, and off-policy data.

## 🩺 Clinical Relevance & Impact
Provides the first "safety manual" for clinical RL, crucial for psychiatric applications where treatment is often sequential (e.g., medication titration). By adhering to these guidelines, researchers can develop treatment-recommending agents that are both statistically robust and clinically safe.

## 🔬 Critical Review (Antagonic Perspective)
The guidelines heavily rely on the availability of high-quality, dense time-series data (like MIMIC-III), which is often missing in psychiatric outpatient settings. The assumptions of Markovian states (MDPs) may be too strong for behavioral health, where "hidden state" (internal patient psychology) is the primary driver of outcomes.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Sutton & Barto (2018) for foundational RL theory.
- **Descendant Discovery:** Parbhoo et al. (2022) for causal extensions to clinical OPE.
