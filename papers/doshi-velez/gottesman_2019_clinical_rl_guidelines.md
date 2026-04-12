---
title: "Guidelines for Reinforcement Learning in Healthcare"
authors: ["Omer Gottesman", "Fredrik Johansson", "Matthieu Komorowski", "Aldo Faisal", "David Sontag", "David Dagan", "Finale Doshi-Velez"]
year: 2019
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "Nature Medicine"
doi: "https://doi.org/10.1038/s41591-018-0330-y"
code: "https://github.com/dtak/clinical-rl-guidelines"
datasets: ["MIMIC-III", "eICU"]
tags: ["Offline RL", "Critical Care", "Sepsis", "Batch RL", "OPE"]
---

# Guidelines for Reinforcement Learning in Healthcare

## 📋 Executive Summary
A landmark paper establishing a rigorous framework for applying Offline (Batch) Reinforcement Learning to clinical data. It addresses the unique challenges of healthcare, such as the inability to explore in real-time, and provides a roadmap for ensuring safety and reliability in treatment policy estimation.

## 🛠️ Core Methodology
- **Batch RL (Offline RL):** Training algorithms on fixed, historical datasets without active environment interaction.
- **FQE (Fitted Q-Evaluation):** An off-policy evaluation method used to estimate the value of a target policy.
- **Influence Functions:** Used alongside FQE to identify which specific transitions in the historical data are most influential to the estimated policy value, aiding in trust and debugging.
- **Deadly Triad Mitigation:** Strategies to handle the combination of function approximation, bootstrapping, and off-policy learning.

## 📊 Dataset & Experimental Setup
- **Data Source:** **MIMIC-III** (Beth Israel Deaconess Medical Center) and **eICU** (Multi-center) databases.
- **Sample Size:** Tens of thousands of ICU patient stays.
- **Features:** Vital signs, lab results, medications (vasopressors, IV fluids), and demographics.
- **Evaluation Metrics:** Policy Value (V), Weighted Importance Sampling (WIS), and Effective Sample Size (ESS).

## 💡 Key Findings
- **Technical Results:** Demonstrates that naive RL application can lead to "unrealistic" policies that deviate dangerously from clinical practice.
- **Statistical Significance:** Use of ESS and WIS provides bounds on the reliability of OPE estimates, crucial for clinical safety.
- **Methodological Impact:** Standardized the use of "batch-constrained" approaches to keep AI recommendations within the manifold of human clinician behavior.

## 🩺 Clinical Relevance & Impact
Provides the foundation for "Safe RL" in sepsis management, specifically optimizing the timing of vasopressors and fluids. The framework ensures that AI recommendations are not just mathematically optimal but clinically plausible and safely evaluable.

## 🔬 Critical Review (Antagonic Perspective)
The guidelines rely heavily on the quality of historical data; if the data itself contains systemic biases (e.g., racial disparities in care), the RL agent may learn to replicate or even amplify these biases under the guise of "optimizing" outcomes.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Sutton & Barto (2018)] for general RL theory.
- **Descendant Discovery:** [Parbhoo et al. (2022)](parbhoo_2022_causal_ope.md) for causal extensions to OPE.
