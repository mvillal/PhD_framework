---
title: "Synthetic Clinical Cohorts"
tags: ["Generative Modeling", "Privacy", "Digital Phenotyping", "EHR", "Causal Transportability"]
---

# Synthetic Clinical Cohorts

## 📖 Definition
**Synthetic Clinical Cohorts** are artificially generated datasets that maintain the statistical properties and causal relationships of real patient populations while protecting individual privacy. In psychiatry, they are increasingly used to bypass the logistical and ethical hurdles of sharing sensitive longitudinal sensor data or EHRs.

## 🧪 Core Methodology
1.  **Causally Weighted Gaussian Mixture Models:** Generating synthetic patients that preserve the causal dependencies between features (e.g., Sleep → Mood → Activity).
2.  **Differential Privacy (DP):** Integrating DP during the training of generative models (like GANs or Variational Autoencoders) to ensure that the synthetic data does not "leak" the identity of real participants.
3.  **Cross-Hospital Transportability:** Using synthetic cohorts to simulate "counterfactual hospitals" where the EHR structure or patient demographics differ, allowing for the stress-testing of ML models before real-world deployment.

## 🚀 Use Cases in Psychiatry
- **Filling the Informative Missingness Gap:** Generating synthetic data points that follow the estimated causal paths of patients who dropped out of a study, allowing for more robust model training.
- **Privacy-Preserving Algorithm Benchmarking:** Enabling researchers from different labs (e.g., [[onnela_lab]] and [[torous_lab_digital_psychiatry]]) to compare algorithms on shared "synthetic truth" without transferring raw patient data.
- **Simulating Rare Events:** Creating synthetic trajectories of rare psychiatric events (e.g., acute psychotic breaks) to train early-warning systems when real-world examples are sparse.

## 🔬 Challenges
- **Fidelity vs. Privacy:** Balancing the accuracy of the synthetic data with the strength of the privacy guarantees.
- **Causal Collapse:** The risk that a generative model captures correlations but fails to maintain the true causal structure, leading to "biased" synthetic cohorts.

## ⚠️ Statistical Limitations
- **Identifiability Constraints:** The recovery of the latent state $S_t$ from MNAR data in Joint-VAEs is strictly dependent on the identifiability of the generative model. Without sufficient auxiliary information or strong priors, the latent space may suffer from rotational invariance, undermining causal interpretations.
- **Rosenbaum Sensitivity:** Synthetic cohorts often assume a closed system. Failure to account for unobserved confounders $U$ (e.g., life events) can lead to inflated confidence in synthetic "ground truths." A sensitivity analysis (measuring robustness to $\Gamma$) is mandatory for any clinical claim derived from synthetic data.
- **Persistence Gap:** Standard interpolation methods (LOCF, Mean) fail when missingness is high ($>60\%$). While DSC-Methods are more robust, they risk "Hallucinating" psychiatric crises if the jump-diffusion priors are mis-specified.

## 🔗 Related Concepts
- [[informative_missingness]]
- [[digital_phenotyping]]
- [[causal_ope]]

## 📚 Sources
- *Precision Digital Phenotyping & Causal Inference (2025-2026)* Synthesis.
- Mozannar et al. (2025): *Causal Falsification of Clinical Policies.*
