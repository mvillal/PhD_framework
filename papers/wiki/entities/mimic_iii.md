---
title: "MIMIC-III (Medical Information Mart for Intensive Care)"
type: "Entity"
category: "Dataset"
tags: ["Intensive Care", "EHR", "Benchmarking", "Clinical RL"]
---

# MIMIC-III (Medical Information Mart for Intensive Care)

## 📋 Overview
MIMIC-III is a large, freely available database comprising de-identified health-related data associated with over forty thousand patients who stayed in critical care units of the Beth Israel Deaconess Medical Center between 2001 and 2012. It serves as the primary benchmark dataset for clinical machine learning, particularly in reinforcement learning and intensive care modeling.

## 🔬 Role in Research
- **Clinical RL Benchmarking:** Used extensively to evaluate off-policy evaluation (OPE) methods and batch RL policies for sepsis management and sedation titration [[Gottesman et al. (2019)](../../sources/doshi-velez/gottesman_2019_clinical_rl_guidelines.md)].
- **Decision Point Analysis:** Leveraged to identify critical states in patient trajectories where treatment decisions have the highest impact on outcomes [[Zhang & Doshi-Velez (2021)](../../sources/doshi-velez/zhang_2021_decision_points_rl.md)].
- **Generalizability Challenges:** Served as a case study for identifying site-specific administrative patterns that can bias ML models when transferred to other institutions [[Futoma et al. (2020)](../../sources/doshi-velez/futoma_2020_myth_of_generalisability.md)].

## 📊 High-Signal Metrics & Characteristics
- **Population:** >40,000 patients, >50,000 stays.
- **Data Density:** High-frequency vital signs, laboratory measurements, medications, and caregiver notes.
- **Usage:** Standard evaluation environment for **Fitted Q-Evaluation (FQE)** and **Weighted Importance Sampling (WIS)**, with metrics like **Effective Sample Size (ESS)** being critical for reliability.

## 🔗 Related Sources
- [Gottesman et al. (2019): Guidelines for RL in Healthcare](../../sources/doshi-velez/gottesman_2019_clinical_rl_guidelines.md)
- [Zhang & Doshi-Velez (2021): Decision Points in RL](../../sources/doshi-velez/zhang_2021_decision_points_rl.md)
- [Futoma et al. (2020): The Myth of Generalizability](../../sources/doshi-velez/futoma_2020_myth_of_generalisability.md)
