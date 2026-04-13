---
title: "Offline Reinforcement Learning"
type: "Concept"
category: "Methodology"
tags: ["Reinforcement Learning", "Batch RL", "OPE", "Sepsis", "Psychiatry"]
---

# Offline Reinforcement Learning

## 📋 Overview
Offline Reinforcement Learning (also known as Batch RL) is the process of learning an optimal decision policy from a fixed dataset of historical interactions, without any ability to interact further with the environment during training. This is the standard paradigm for clinical applications, where real-time exploration (trial and error) is often unethical or unsafe.

## 🔬 Role in Clinical Research
- **Safety Guidelines:** Foundational research has established rigorous checklists for clinical offline RL, emphasizing robust Off-Policy Evaluation (OPE) and stakeholder engagement [[Gottesman et al. (2019)](../../sources/doshi-velez/gottesman_2019_clinical_rl_guidelines.md)].
- **Discount Regularization:** New frameworks address the "unintended consequences" of standard regularization by introducing state-action-specific discount regularization, which is strongest in data-sparse regions to ensure safety [[Jiang & Doshi-Velez (2024)](../../sources/doshi-velez/jiang_2024_discount_regularization.md)].
- **Decision Point Discovery:** Offline RL is used to identify critical "decision points" in patient trajectories where interventions have the most significant impact on clinical outcomes [[Zhang & Doshi-Velez (2021)](../../sources/doshi-velez/zhang_2021_decision_points_rl.md)].

## 📊 High-Signal Metrics & Characteristics
- **Evaluation:** Primarily evaluated using **Fitted Q-Evaluation (FQE)** and **Weighted Importance Sampling (WIS)**.
- **Reliability:** Metrics such as **Effective Sample Size (ESS)** are critical for determining the confidence of policy evaluation in clinical datasets like **MIMIC-III** and **eICU**.

## 🔗 Related Sources
- [Gottesman et al. (2019): Guidelines for RL in Healthcare](../../sources/doshi-velez/gottesman_2019_clinical_rl_guidelines.md)
- [Jiang & Doshi-Velez (2024): Discount Regularization in Offline RL](../../sources/doshi-velez/jiang_2024_discount_regularization.md)
- [Zhang & Doshi-Velez (2021): Decision Points in RL](../../sources/doshi-velez/zhang_2021_decision_points_rl.md)
