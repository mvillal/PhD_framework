---
title: "Rethinking Discount Regularization: New Interpretations, Unintended Consequences, and Solutions for Regularization in Reinforcement Learning"
authors: ["Sarah Rathnam", "Sonali Parbhoo", "Siddharth Swaroop", "Weiwei Pan", "Susan A. Murphy", "Finale Doshi-Velez"]
year: 2024
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "Journal of Machine Learning Research (JMLR)"
doi: "N/A"
code: "https://github.com/dlr-rm/stable-baselines3 (Custom Schedulers Pattern)"
datasets: ["Medical-Cancer-Sim", "Synthetic-MDPs"]
tags: ["Reinforcement Learning", "Discount Regularization", "Planning Horizon", "Clinical RL", "Overfitting"]
---

# Rethinking Discount Regularization

## 📋 Executive Summary
Rathnam et al. (2024) provide a rigorous critique of **Discount Regularization**—the common practice of using a shorter planning horizon ($\gamma_{plan}$) than the evaluation horizon ($\gamma_{eval}$) to prevent overfitting in clinical RL. While intended to stabilize learning in sparse-data environments, the authors prove that this global approach has "unintended consequences." Specifically, it regularizes state-action pairs with *more* data more heavily than those with *less* data. The paper proposes a state-action-specific regularization formula to restore clinical utility and stability.

## 🛠️ Core Methodology
- **Equivalence Theorems:** Mathematically proves that planning with a lower discount factor is equivalent to:
    1.  **Model-Based:** Planning with a specific Bayesian prior on the transition matrix.
    2.  **Model-Free:** Planning with a penalized Q-function (weighted average Bellman update).
- **Unintended Consequences Analysis:** Demonstrates that standard discounting smoothed out well-sampled clinical regions toward a uniform prior, losing the "local knowledge" learned from standard care.
- **State-Action-Specific Regularization:** Introduces a formula to set regularization parameters locally ($(\lambda_{s,a})$) based on the sample count for each pair, ensuring that regularization is only applied where data is sparse.

## 📊 Dataset & Experimental Setup
- **Evaluation:** Tested on a **Medical Cancer Simulator** and various synthetic MDPs.
- **Comparison:** Compared global discount regularization vs. the proposed state-action-specific method and standard unregularized RL.

## 💡 Key Findings
- **Smoothing Flaw:** Confirmed that global discounting over-regularizes well-sampled regions, leading to poor performance in standard clinical scenarios.
- **Performance Gain:** The state-action-specific method significantly improved policy value in the cancer simulator by preserving the model's accuracy in high-data regions while providing stability in low-data regions.
- **Horizon-Model Tradeoff:** Established the formal relationship between the "effective planning horizon" and the accuracy of the underlying clinical model.

## 🩺 Clinical Relevance & Impact
This paper is vital for **Precision Oncology** and psychiatric treatment titration. It ensures that RL agents don't "forget" how to treat standard patients (where we have lots of data) in an attempt to be robust for rare cases. It provides a mathematical path toward RL models that are both stable and clinically excellent.

## 🔬 Critical Review (Antagonic Perspective)
The proposed solution (state-action-specific regularization) requires careful tracking of sample counts for every state-action pair, which can be computationally expensive and difficult to estimate in **Continuous State Spaces** (e.g., using Neural SDEs).

## 🔗 Discovery & Next Steps
- **Implementation:** Use `stable-baselines3`'s custom schedulers (fetched via Context7) to dynamically adjust $\gamma$ or penalties based on state-action counts.
- **Synthesis Link:** Updates [The State of Clinical RL (2026)](synthesis/state_of_clinical_rl_2026.md).
