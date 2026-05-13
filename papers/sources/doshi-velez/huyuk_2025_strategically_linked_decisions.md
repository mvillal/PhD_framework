---
title: "Strategically Linked Decisions in Long-Term Planning and Reinforcement Learning"
authors: ["Hüyük et al."]
year: 2025
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "arXiv / TBD"
doi: "10.48550/arXiv.2505.16833"
code: "https://github.com/ray-project/ray (Hierarchical Patterns)"
datasets: ["Synthetic-Medical-Trajectories", "Traffic-Planning-Sim"]
tags: ["Reinforcement Learning", "Strategic Link Scores", "Interpretability", "Long-Term Planning", "Hierarchical RL"]
---

# Strategically Linked Decisions in Long-Term Planning and Reinforcement Learning

## 📋 Executive Summary
Hüyük and Doshi-Velez (2025) introduce **Strategic Link Scores**, a novel interpretability metric for sequential decision-making. The core problem in clinical RL is that isolated actions may seem suboptimal unless viewed as part of a multi-step "setup and pay-off" strategy. This paper provides a mathematical framework to identify when two decisions are strategically interdependent, ensuring that AI-driven recommendations are interpreted as cohesive clinical strategies rather than disconnected steps.

## 🛠️ Core Methodology
- **Strategic Link Score (SLS):** Quantifies the dependency between a "setup" decision $a_1$ and a "pay-off" decision $a_2$. It measures the drop in the probability of $a_1$ if $a_2$ is removed from the agent's action space.
- **Counterfactual Intervention:** The score is computed by intervening on the agent's *future* possibilities to see how its *current* planning changes.
- **Strategic Mapping:** Identifies pairs or chains of linked actions in a learned policy, creating a "strategic graph" of the agent's long-term plan.

## 📊 Dataset & Experimental Setup
- **Evaluation:** Benchmarked on synthetic medical trajectories (e.g., diagnostic setup before high-value treatment) and complex planning environments like traffic simulators.
- **Comparisons:** Compared against state-importance metrics and standard reward-attribution (SHAP/LIME).

## 💡 Key Findings
- **Strategy Identification:** SLS successfully identified "setup" actions (like ordering a specific baseline test) that traditional interpretability tools flagged as "low importance" because they had no immediate reward.
- **Clinician Guardrails:** Demonstrated that link scores can prevent "cherry-picking"—warning clinicians that if they ignore the first recommended action, the subsequent "high-reward" action may no longer be viable.
- **Planning-Level Explanations:** SLS provides a higher level of abstraction than step-by-step explanations, revealing the "intent" behind a multi-step policy.

## 🩺 Clinical Relevance & Impact
In psychiatry, this is critical for **Treatment Titration**. An initial, lower-dose antidepressant might be "strategically linked" to a later, higher-dose adjuvant therapy. If a clinician ignores the setup phase, the pay-off phase might lead to toxicity or failure. SLS provides the necessary "strategic context" for safe human-AI collaboration in mental health.

## 🔬 Critical Review (Antagonic Perspective)
The score depends on the agent having a robust internal model of future rewards. If the RL agent's planning is flawed (e.g., due to poor OPE), the "strategic links" it identifies may be hallucinations of the model's own biases rather than true clinical dependencies.

## 🔗 Discovery & Next Steps
- **Implementation:** Explore Ray RLlib's **Hierarchical Environments** to model the high-level/low-level decision-making hierarchy identified by strategic links.
- **Synthesis Link:** Connects to [The State of Clinical RL (2026)](synthesis/state_of_clinical_rl_2026.md).
