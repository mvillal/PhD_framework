---
title: "Causal Off-Policy Evaluation (OPE)"
type: "Concept"
category: "Methodology"
tags: ["Off-Policy Evaluation", "Causal Inference", "SCM", "Sepsis", "Psychiatry"]
---

# Causal Off-Policy Evaluation (OPE)

## 📋 Overview
Causal Off-Policy Evaluation (OPE) extends standard OPE methods by incorporating Structural Causal Models (SCMs) and causal inference principles. This approach allows researchers to evaluate treatment policies more reliably, specifically addressing unmeasured confounding and the transportability of policies across different patient populations.

## 🔬 Role in Clinical Research
- **Reliable Evaluation:** Introduced SCM-based Causal OPE to evaluate treatment optimality in clinical settings like sepsis and HIV, where confounding and site-specific administrative patterns are prevalent [[Parbhoo et al. (2022)](../../sources/doshi-velez/parbhoo_2022_causal_ope.md)].
- **Transportability:** Causal OPE frameworks enable researchers to assess how well a policy learned at one clinical site (e.g., MIMIC-III) will perform at another with different practice patterns.

## 📊 High-Signal Metrics & Characteristics
- **Methodology:** Utilizes Structural Causal Models (SCMs) to explicitly model the relationship between treatments, outcomes, and both measured and unmeasured variables [[Parbhoo et al. (2022)](../../sources/doshi-velez/parbhoo_2022_causal_ope.md)].
- **Benefit:** Reduces bias in policy value estimation compared to purely associative OPE methods in the presence of unmeasured confounding.

## 🔗 Related Sources
- [Parbhoo et al. (2022): Causal OPE](../../sources/doshi-velez/parbhoo_2022_causal_ope.md)
- [Gottesman et al. (2019): Guidelines for RL in Healthcare](../../sources/doshi-velez/gottesman_2019_clinical_rl_guidelines.md)
