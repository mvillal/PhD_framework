---
title: "Causal Falsification of Clinical Decision Policies using Small-Scale RCT Data"
authors: ["G. Mozannar", "D. Sontag"]
year: 2025
lab: "MIT CSAIL Clinical Machine Learning Group"
venue: "CLeaR / ICLR (Accepted)"
doi: "TBD"
code: "Sontag Lab GitHub"
datasets: ["MIMIC-III", "Proton Trial Proxy"]
tags: ["Causal Inference", "Offline RL", "Causal Falsification", "Sontag Lab"]
---

# Causal Falsification of Clinical Decision Policies using Small-Scale RCT Data

## 📋 Executive Summary
This paper addresses the "credibility crisis" in offline Reinforcement Learning (RL) for healthcare. It introduces a framework for **Causal Falsification**, which uses data from small-scale randomized controlled trials (RCTs) to identify and reject clinical policies learned from biased observational data (EHRs). This provides a critical safety layer for clinical AI deployment.

## 🛠️ Core Methodology
- **Causal Consistency Checking:** Comparing the expected outcomes of a learned policy against the actual outcomes observed in a small, high-fidelity RCT cohort.
- **Policy Falsification:** A statistical test to determine if the observational policy's value estimate is "falsified" by the RCT data, indicating hidden confounding or model misspecification.
- **Transfer Learning (RCT -> EHR):** Using the RCT data not to train a model, but to "audit" the model trained on large-scale, biased EHR data (e.g., MIMIC-III).

## 📊 Dataset & Experimental Setup
- **Data Source:** Models trained on MIMIC-III (Observational) and validated against simulated and real-world small-scale RCT data in oncology.
- **Clinical Task:** Chemotherapy dosing and sepsis management policies.

## 💡 Key Findings
- **High Sensitivity to Bias:** The falsification test successfully rejected 85% of biased clinical policies that would have passed standard cross-validation.
- **Safe Policy Deployment:** Provides a rigorous threshold for when an observational policy is "safe enough" to enter large-scale clinical trials.

## 🩺 Clinical Relevance & Impact
Ensures that treatment-recommending agents are not merely learning the "bad habits" or administrative signatures of a specific hospital. Crucial for life-critical decisions in oncology and intensive care.

## 🔬 Critical Review (Antagonic Perspective)
The method requires access to even a "small" RCT, which may not exist for all clinical conditions. It assumes the RCT cohort is representative of the observational population, which is often not the case due to strict RCT exclusion criteria.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Gottesman et al. (2019) Guidelines for Clinical RL.
- **Descendant Discovery:** Automated "Causal Auditing" dashboards for health systems (2026).
