---
title: "Strategically Linked Decisions: Explaining Long-Term Dependencies in RL"
authors: ["Alihan Hüyük", "Finale Doshi-Velez"]
year: 2025
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "ICLR / arXiv"
doi: "10.48550/arXiv.2505.16833"
url: "https://arxiv.org/abs/2505.16833"
datasets: ["Clinical Simulators", "HIV Treatment Proxy"]
tags: ["Strategic Link Scores", "Interpretable RL", "Sequential Decision-Making", "Long-Term Dependencies"]
---

# Strategically Linked Decisions: Explaining Long-Term Dependencies in RL

## 📋 Executive Summary
This paper introduces "Strategic Link Scores," a novel quantitative framework for explaining complex, long-term dependencies in sequential decision-making. By identifying "set-up" and "pay-off" pairs, the method distinguishes between standalone tactical moves and strategic sequences that require future commitment for success.

## 🛠️ Core Methodology
- **Strategic Link Scores:** Defined as the drop in the likelihood of a set-up decision (e.g., picking up a key) when a subsequent pay-off decision (e.g., using the key to unlock a door) is removed.
- **Counterfactual Reasoning:** Uses counterfactual scenarios to evaluate how the agent's current choice is conditioned on the future availability of specific options.
- **Strategic Pairs Identification:** An algorithmic approach to finding action sequences that are "strategically linked," meaning one's value is contingent on the other.

## 📊 Dataset & Experimental Setup
- **Data Source:** Clinical simulators for long-term health management and standard RL benchmarks (e.g., MiniGrid-type environments).
- **Features:** Decision points where current actions enable future high-reward states.
- **Evaluation Metrics:** Strategic Link Score (SLS) distribution across the policy trajectory and "Alignment Scores" with expert human strategies.

## 💡 Key Findings
- **Discovery of Latent Strategy:** SLS successfully identifies "set-up" actions that simpler interpretability methods (like feature importance) misclassify as noise or low-value.
- **Improved Clinician Trust:** By linking early interventions to future therapeutic milestones, the framework provides a more intuitive explanation for "why" an agent recommends a specific, non-obvious starting action.
- **Safety in Execution:** Helps prevent "half-strategies" where clinicians might adopt the set-up without realizing the necessity of the follow-up pay-off action.

## 🩺 Clinical Relevance & Impact
Critically relevant to psychiatric treatment pathways (e.g., starting a specific SSRI to enable later adjunctive therapies). It ensures that the clinician understands the broader strategic "plan" of the AI agent rather than seeing each recommendation in isolation.

## 🔬 Critical Review (Antagonic Perspective)
Calculating Link Scores requires an accurate model of future trajectories, which is challenging in high-uncertainty clinical environments. There is a risk of "hallucinating" links in data-sparse regions where the model's future predictions are unreliable.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Zhang et al. (2021) for identifying critical decision points in clinical RL.
- **Descendant Discovery:** Applying Strategic Link Scores to multi-modal psychiatric datasets (EMA + EHR).
