---
title: "eICU Collaborative Research Database"
type: "Entity"
category: "Dataset"
tags: ["Intensive Care", "EHR", "OPE", "Sepsis"]
---

# eICU Collaborative Research Database

## 📋 Overview
The eICU Collaborative Research Database is a large, multi-center database made available by Philips Healthcare in partnership with MIT. It contains data from over 200,000 patient stays across dozens of ICUs in the United States, providing a broader, more heterogeneous population than single-site databases like MIMIC-III.

## 🔬 Role in Research
- **Multi-Site Policy Evaluation:** Crucial for testing the transportability and robustness of clinical RL policies across different hospital systems.
- **Sepsis & Sedation Titration:** Used alongside MIMIC-III to establish the "Guidelines for Reinforcement Learning in Healthcare," particularly in demonstrating the effectiveness of **Fitted Q-Evaluation (FQE)** [[Gottesman et al. (2019)](../../sources/doshi-velez/gottesman_2019_clinical_rl_guidelines.md)].

## 📊 High-Signal Metrics & Characteristics
- **Population:** >200,000 patient stays.
- **Coverage:** Multi-center (various hospitals across the US), unlike the single-center nature of MIMIC-III.
- **Application:** Ideal for validating **Batch RL** safety protocols and assessing the impact of unmeasured confounding across diverse clinical practices.

## 🔗 Related Sources
- [Gottesman et al. (2019): Guidelines for RL in Healthcare](../../sources/doshi-velez/gottesman_2019_clinical_rl_guidelines.md)
