---
title: "Pre-emptive Learning to Defer for Sequential Medical Decision-Making Under Uncertainty"
authors: ["Shalmali Joshi", "Sonali Parbhoo", "Finale Doshi-Velez"]
year: 2021
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "ICML"
doi: "10.48550/arXiv.2109.06312"
url: "https://arxiv.org/abs/2109.06312"
tags: ["Learning to Defer", "Sequential Decision Making", "Bayesian Uncertainty", "Human-AI Collaboration"]
---

# Pre-emptive Learning to Defer for Sequential Medical Decision-Making Under Uncertainty

## 📋 Executive Summary
This paper introduces a framework for **Sequential Learning-to-Defer (SLTD)**, which determines whether an AI agent should take an action or defer to a human expert in a sequential clinical setting. Unlike static deferral models, SLTD considers the long-term impact of deferral, accounting for how uncertainty propagates over time in non-stationary medical environments.

## 🛠️ Core Methodology
- **Sequential Learning-to-Defer (SLTD):** A framework that optimizes a policy to either act or hand over control to a human expert.
- **Bayesian Uncertainty Quantification:** Uses Bayesian models to estimate aleatoric and epistemic uncertainty.
- **Pre-emptive Deferral:** Analyzes whether deferring now is more beneficial than deferring later by looking ahead at the trajectory of uncertainty.

## 📊 Dataset & Experimental Setup
- Validated using non-stationary simulators for **Sepsis** and **Diabetes**.
- Compared against standard RL agents and static deferral policies.

## 💡 Key Findings
- SLTD identifies regions of the state space where the model is likely to fail before errors occur.
- Outperforms static deferral by accounting for the sequential nature of medical decisions.
- Decomposing uncertainty improves the interpretability of why a deferral was triggered.

## 🩺 Clinical Relevance & Impact
In high-risk psychiatric or medical scenarios, an RL agent should know its limits. This work provides a safety mechanism by identifying when a human expert's judgment is required to ensure patient safety in complex, evolving clinical cases.

## 🔬 Critical Review (Antagonic Perspective)
A major challenge is modeling the human expert's behavior. If the expert's error profile is unknown or changes over time, the deferral policy could become suboptimal. Additionally, pre-emptive deferral relies on accurate uncertainty propagation, which is computationally expensive for complex, high-dimensional psychiatric state spaces.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Madras et al. (2018) for initial "Learning to Defer" frameworks.
- **Descendant Discovery:** Extending SLTD to mHealth settings where deferral involves direct clinician intervention via smartphone alerts.
