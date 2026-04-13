---
title: "Offline Reinforcement Learning in Healthcare"
type: "concept"
tags: ["RL", "Batch RL", "OPE", "Safety"]
---

# Offline Reinforcement Learning in Healthcare

Offline (or Batch) Reinforcement Learning is the study of learning optimal decision-making policies from fixed, observational datasets without real-time environment interaction.

## 📋 Definition & Core Philosophy
In healthcare, RL is primarily "Offline" due to the ethical and safety risks of exploring non-expert policies on live patients. The core goal is to identify **Decision Points** where clinical actions significantly impact long-term survival or recovery.

## 🔬 Evolution of Thought (PhD Synthesis)
1. **The Deadly Triad (2019):** Gottesman et al. established the primary risks in clinical RL: Function Approximation, Bootstrapping, and Off-policy learning. The lab's initial stance was "Defense-First," emphasizing safe evaluation (OPE) over policy discovery.
   - *Source:* [Gottesman et al. (2019)](../../doshi-velez/gottesman_2019_clinical_rl_guidelines.md)
2. **Discount Regularization (2024):** Jiang & Doshi-Velez shifted the focus to **Overfitting in Low-Data Regimes**, introducing state-action-specific discounting to prevent agents from choosing short-term physiological fixes over long-term survival.
   - *Source:* [Jiang & Doshi-Velez (2024)](../../doshi-velez/jiang_2024_discount_regularization.md)
3. **Strategic Linkage (2025):** The introduction of **Strategic Link Scores** moved RL from a "Black Box" to a tool for explaining the long-term prerequisites of clinical actions.
   - *Source:* [Hüyük & Doshi-Velez (2025)](../../doshi-velez/huyuk_2025_strategically_linked_decisions.md)

## 📊 Key Metrics & Benchmarks
- **OPE Metrics:** Weighted Importance Sampling (WIS), Effective Sample Size (ESS).
- **Evaluation:** Policy Value (V) compared to "Standard of Care."

## 🩺 Clinical Challenges
- **Automation Bias:** Clinicians may follow incorrect RL recommendations even when explanations are provided.
- **Algorithm Fidelity:** Ensuring that real-time clinical trial participants are safe while monitoring the autonomous agent.

## 🔗 Discovery & Next Steps
- **Causal OPE:** Explore how Structural Causal Models (SCMs) can generalize offline policies to new subpopulations.
   - *Source:* [Parbhoo et al. (2022)](../../doshi-velez/parbhoo_2022_causal_ope.md)
