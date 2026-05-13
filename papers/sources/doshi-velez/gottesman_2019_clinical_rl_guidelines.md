---
title: "Guidelines for reinforcement learning in healthcare"
authors: ["Gottesman et al."]
year: 2019
lab: "Harvard / Doshi-Velez Lab (Contextual)"
venue: "Nature Medicine"
doi: "10.1038/s41591-019-0667-3"
code: "https://github.com/pytorch/rl (Modern Standard)"
datasets: ["MIMIC-III", "eICU", "Sepsis-3"]
tags: ["Reinforcement Learning", "Clinical Guidelines", "Off-Policy Evaluation", "OPE", "Safety"]
---

# Guidelines for reinforcement learning in healthcare

## 📋 Executive Summary
Gottesman et al. (2019) provide a seminal roadmap for the application of Reinforcement Learning (RL) to healthcare. Recognizing the high stakes of clinical decision-making, the authors move beyond simple optimization to establish a rigorous framework for **Off-Policy Evaluation (OPE)**, safety, and clinical grounding. The core message is that "evaluation is harder than optimization" in healthcare, and a model's success on historical data (EHR) does not guarantee safety in prospective clinical practice.

## 🛠️ Core Methodology
- **Problem Formulation:** Frames clinical treatments as sequential decision-making tasks (POMDPs) where the "state" is partially observable through EHR data.
- **Off-Policy Evaluation (OPE):** Emphasizes the use of **Importance Sampling (IS)** and **Doubly Robust** estimators to evaluate a new policy using historical clinician data.
- **Safety Constraints:** Advocates for "clinically reasonable" policy bounds to prevent the model from suggesting extreme or dangerous actions.
- **Unmeasured Confounding Analysis:** Discusses how "hidden" clinician knowledge (not in the EHR) can bias RL agents.

## 📊 Dataset & Experimental Setup
- **Benchmark:** Sepsis management using the **MIMIC-III** dataset.
- **Evaluation Metrics:** Focused on **Effective Sample Size (ESS)** for OPE and the distribution of importance weights to detect policy divergence.

## 💡 Key Findings
- **The "U-Curve" Pitfall:** Identified a critical failure mode where RL agents appear to outperform humans by suggesting "no treatment" for the most terminal patients, failing to realize these patients would die regardless of action.
- **Reward Hacking:** Warned against optimizing for proxy clinical markers (e.g., blood pressure) which may improve in the short term while patient survival decreases.
- **Need for Shadow Mode:** Proposed that deployment should begin with "shadow testing," where AI recommendations are recorded but not acted upon, to validate against human clinician outcomes.

## 🩺 Clinical Relevance & Impact
These guidelines have become the standard for "Safe Clinical RL." They ensure that researchers account for **Informative Missingness** (the fact that a test was ordered is a state signal) and **Clinician Intent**. In psychiatry, this applies to titrating antidepressants or managing crisis interventions where sequential timing is critical.

## 🔬 Critical Review (Antagonic Perspective)
The guidelines' heavy focus on "clinically reasonable" bounds may prevent the discovery of **Super-Human Policies**—counter-intuitive treatments that clinicians currently miss. Furthermore, OPE remains statistically "brittle" in high-dimensional state spaces typical of long-term psychiatric care.

## 🔗 Discovery & Next Steps
- **Implementation:** Utilize `torchrl`'s `D4RLExperienceReplay` for offline RL experiments as a starting point for clinical OPE.
- **Synthesis Link:** Foundational to [The State of Clinical RL (2026)](synthesis/state_of_clinical_rl_2026.md).
