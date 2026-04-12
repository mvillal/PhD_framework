---
title: "Strategically Linked Decisions: Explaining Long-Term Dependencies in RL"
authors: ["Alihan Huyuk", "Finale Doshi-Velez"]
year: 2025
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "AIStats / Preprint"
doi: "Forthcoming/Preprint"
url: "Forthcoming"
code: "N/A"
datasets: ["Simulated Clinical Environment"]
tags: ["Strategic Link Scores", "XAI", "RL", "Sequential Decisions"]
---

# Strategically Linked Decisions: Explaining Long-Term Dependencies in RL

## 📋 Executive Summary
Clinicians often struggle to understand why an RL agent recommends a seemingly "suboptimal" immediate action. This paper introduces **Strategic Link Scores**, which quantify how a current decision (e.g., "stabilize mood") is a necessary prerequisite for a future, high-value goal (e.g., "successful psychotherapy"), making the agent's long-term strategy transparent.

## 🛠️ Core Methodology
- **Strategic Link Scores:** A new XAI metric that decomposes the Q-value into "direct reward" and "strategic links" to future states.
- **Prerequisite Identification:** Formalizing the concept of a "bottleneck" action that must be taken to unlock a later beneficial treatment phase.
- **Temporal Credit Assignment:** Explaining how a decision at time $t$ influences the feasibility and reward of actions at time $t+k$.

## 📊 Dataset & Experimental Setup
- **Data Source:** Simulated clinical environments with complex, **long-term dependencies**.
- **Sample Size:** Synthetic cohorts with multi-stage treatment requirements.
- **Features:** Patient states, prerequisite flags, and distal outcome rewards.
- **Evaluation Metrics:** Clinician understanding (survey), alignment between link scores and expert intuition.

## 💡 Key Findings
- **Technical Results:** Strategic Link Scores successfully identified "hidden" dependencies that standard feature importance methods (like SHAP) missed.
- **Long-Term Logic:** The model could explain that "Action A is recommended NOT for immediate gain, but because it is the only way to enable Action B later."
- **Ablation Studies:** Showed that without link scores, clinicians often rejected the RL's "best" policy because it looked "incorrect" in the short-term.

## 🩺 Clinical Relevance & Impact
Crucial for psychiatric "stepped care" models. For example, a clinician might not see why an AI suggests a specific low-intensity intervention first; the Link Score can explain that this intervention is necessary to build the patient's "readiness" for more intensive work later.

## 🔬 Critical Review (Antagonic Perspective)
The method assumes the RL agent has actually *learned* a strategic policy. If the agent is just overfitting to noise, the Strategic Link Scores will provide a "plausible-sounding" explanation for a fundamentally flawed strategy (hallucinated strategy).

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Parbhoo et al. (2022)](parbhoo_2022_causal_ope.md) for causal grounding of these links.
- **Descendant Discovery:** [Fischer et al. (2025)](fischer_2025_clinician_expectations.md) for confirming that clinicians value this type of trajectory-based explanation.
