---
title: "Causal Evaluation of Optimality in Healthcare"
authors: ["Sonali Parbhoo", "Mario Wieser", "Finale Doshi-Velez"]
year: 2022
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "Nature Machine Intelligence"
doi: "https://doi.org/10.1038/s42256-022-00466-9"
code: "https://github.com/dtak/causal-ope"
datasets: ["ACTG 175", "Sepsis Simulator"]
tags: ["Causal Inference", "OPE", "SCM", "Transportability", "HIV"]
---

# Causal Evaluation of Optimality in Healthcare

## 📋 Executive Summary
This work introduces a causal framework for Off-Policy Evaluation (OPE), addressing the limitations of standard statistical OPE in generalizing across different clinical populations. By incorporating Structural Causal Models (SCMs), it enables "Causal Transportability," allowing policies learned in one setting to be reliably evaluated for another.

## 🛠️ Core Methodology
- **Structural Causal Models (SCMs):** Used to encode domain knowledge and causal relationships between symptoms, treatments, and outcomes.
- **Multiply-Robust Estimators:** Combining propensity scores and outcome regressions within a causal framework to reduce variance and bias.
- **Causal Transportability:** Utilizing Pearl's do-calculus to formalize how a treatment effect or policy value can be "transported" from a source population (e.g., a clinical trial) to a target population (e.g., a specific hospital's demographics).

## 📊 Dataset & Experimental Setup
- **Data Source:** **ACTG 175 HIV Data** (AIDS Clinical Trials Group) and a synthetic Sepsis Simulator.
- **Sample Size:** ACTG 175 included 2,139 HIV-infected individuals.
- **Features:** CD4 counts, age, weight, and antiretroviral treatment history.
- **Evaluation Metrics:** Policy Value (V), Identifiability of causal effects, and Mean Squared Error (MSE) of value estimates.

## 💡 Key Findings
- **Technical Results:** Causal OPE significantly outperformed standard OPE methods in scenarios with distribution shift (population mismatch).
- **Statistical Significance:** Demonstrates that ignoring the causal structure leads to highly biased value estimates when transferring policies between different clinical sites.
- **Ablation Studies:** Showed that even partial knowledge of the SCM can improve the robustness of policy evaluation.

## 🩺 Clinical Relevance & Impact
Crucial for HIV treatment and sepsis, where clinicians need to know if a protocol developed in a major research hospital will work for their local patient population. This provides a formal mathematical bridge from "global" evidence to "local" application.

## 🔬 Critical Review (Antagonic Perspective)
The framework assumes the SCM is correctly specified. In complex psychiatric or multi-comorbidity cases, the true causal graph is often unknown or partially hidden, which can introduce unobserved confounding.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Pearl (2009)] for Causal Inference/do-calculus.
- **Descendant Discovery:** [Huyuk et al. (2025)](huyuk_2025_strategically_linked_decisions.md) for explaining the temporal logic of these causal links.
