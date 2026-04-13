---
title: "Identifying Decision Points for Safe and Interpretable Reinforcement Learning"
authors: ["Zhang et al.", "Finale Doshi-Velez"]
year: 2021
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "NeurIPS Workshop on AI for Health"
doi: "10.48550/arXiv.2101.03309"
url: "https://arxiv.org/abs/2101.03309"
tags: ["Decision Points", "Safe RL", "Interpretable RL", "Clinical Trajectories"]
---

# Identifying Decision Points for Safe and Interpretable Reinforcement Learning

## 📋 Executive Summary
Clinical trajectories often contain long periods where the choice of action is either obvious or has minimal impact on the outcome. This paper proposes a method to identify **Decision Points**—states where the choice of action is both critical and supported by diverse data—to simplify and secure RL applications in healthcare.

## 🛠️ Core Methodology
- **Decision Point Identification:** Uses state-space discretization and analysis of action-value variances to find points in a trajectory where decisions truly matter.
- **Interpretability Constraints:** Limits the RL agent's active decision-making to these points, keeping the rest of the trajectory under standard care or fixed protocols.
- **Safe RL:** By focusing on high-evidence decision points, the risk of taking "hallucinated" or low-confidence actions in sparse data regions is reduced.

## 📊 Dataset & Experimental Setup
- Applied to hypotension treatment in intensive care settings (MIMIC-III).

## 💡 Key Findings
- Clinical trajectories can be significantly compressed into a few critical decision points without loss of performance.
- Focusing on decision points makes the RL agent's logic more transparent to clinicians.
- Improves safety by preventing the model from acting in states where it lacks sufficient evidence.

## 🩺 Clinical Relevance & Impact
Making psychiatric RL agents safer by limiting actions to points where clinical evidence is strongest. In psychiatry, this could mean identifying specific moments in a patient's history where a medication change or intervention is most likely to be effective, rather than continuous, low-confidence adjustments.

## 🔬 Critical Review (Antagonic Perspective)
Identifying decision points depends on the quality of the historical behavior policy. If clinicians historically made consistent, but wrong, decisions in a certain region, the RL agent might fail to identify those as "decision points" due to low action variance in the data.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Gottesman et al. (2019) for general clinical RL guidelines.
- **Descendant Discovery:** Integrating decision point identification with the Strategic Link Scores (Hüyük & Doshi-Velez, 2025).
