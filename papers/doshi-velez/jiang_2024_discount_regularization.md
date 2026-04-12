---
title: "Rethinking Discount Regularization for Clinical Offline RL"
authors: ["Ray Jiang", "Melanie Pradier", "Finale Doshi-Velez"]
year: 2024
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "ICML (International Conference on Machine Learning)"
doi: "N/A"
code: "N/A"
datasets: ["MIMIC-III", "Simulated mHealth"]
tags: ["Regularization", "Discounting", "Offline RL", "Sepsis"]
---

# Rethinking Discount Regularization for Clinical Offline RL

## 📋 Executive Summary
This paper introduces a novel regularization technique for Offline RL: state-action-specific discounting. By allowing the discount factor ($\gamma$) to vary based on the confidence or density of data in the state-action space, it prevents the agent from over-optimizing in low-data regimes.

## 🛠️ Core Methodology
- **State-Action-Specific Discounting:** Instead of a fixed $\gamma$ (e.g., 0.99), the algorithm uses a function $\gamma(s, a)$ that lowers the discount in regions where data is sparse.
- **Regularization Effect:** Effectively "shrinks" the value estimates of rarely-seen actions, preventing the agent from being lured by high-variance (and potentially over-optimistic) reward signals.
- **Low-Data Regime Optimization:** Specifically designed for clinical settings where certain treatment paths are rarely taken.

## 📊 Dataset & Experimental Setup
- **Data Source:** **MIMIC-III** (Sepsis cohort) and simulated **mHealth** environments.
- **Sample Size:** Standardized sepsis subset from MIMIC.
- **Features:** Hemodynamics, fluid balance, and vasopressor dosages.
- **Evaluation Metrics:** Estimated Policy Value, Variance of Value Estimates, and Robustness to Sample Size.

## 💡 Key Findings
- **Technical Results:** Improved the stability of value functions in the "deadly triad" context.
- **Overfitting Mitigation:** Prevented the agent from choosing extreme treatments (e.g., maximum vasopressor dose) that appeared "optimal" due to a few lucky historical outliers.
- **Ablation Studies:** Showed that global discounting consistently led to more "brittle" policies than state-action-specific discounting.

## 🩺 Clinical Relevance & Impact
Addresses the "safety-first" requirement of psychiatry and critical care. By regularizing the discount factor, the AI is incentivized to stick to "well-trodden" paths unless there is overwhelming evidence for an alternative, mimicking the conservative nature of clinical expertise.

## 🔬 Critical Review (Antagonic Perspective)
The method relies on an accurate density estimation of the state-action space. If the density model is flawed, the agent might prematurely discount valid, life-saving (but rare) interventions.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Jiang et al. (2015)] for original work on discount factors.
- **Descendant Discovery:** [Trella et al. (2024)](trella_2024_online_rl_fidelity.md) for real-time monitoring of these regularized policies.
