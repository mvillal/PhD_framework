---
title: "Monitoring Fidelity of Online Reinforcement Learning in Clinical Trials"
authors: ["Anna Trella", "Kelly W. Zhang", "Finale Doshi-Velez", "Susan A. Murphy"]
year: 2024
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS / Murphy Lab"
venue: "Biostatistics / arXiv"
doi: "https://arxiv.org/abs/2406.01732"
url: "https://arxiv.org/abs/2406.01732"
code: "N/A"
datasets: ["Oralytics Trial"]
tags: ["mHealth", "Algorithm Fidelity", "Safe RL", "Online Trials"]
---

# Monitoring Fidelity of Online Reinforcement Learning in Clinical Trials

## 📋 Executive Summary
As RL agents are increasingly used in "online" clinical trials (like mobile health apps), there is a need to ensure they follow their intended logic. This paper proposes a "Real-time Algorithm Fidelity" framework to monitor agent behavior and detect deviations before they harm participants or invalidate trial results.

## 🛠️ Core Methodology
- **Algorithm Fidelity Framework:** A set of diagnostic tools to compare the agent's *actual* actions with its *theoretically expected* behavior.
- **Real-Time Monitoring:** Sequential testing procedures to detect "policy drift" or unexpected behavior due to non-stationary patient data.
- **Constraint Verification:** Ensuring the agent respects "hard" safety constraints (e.g., maximum frequency of push notifications).

## 📊 Dataset & Experimental Setup
- **Data Source:** **Oralytics mHealth trial** data (focused on encouraging oral hygiene behaviors).
- **Sample Size:** Participants in an active mobile health intervention.
- **Features:** Time of day, past engagement, user state (e.g., "at home"), and reward (brushing duration).
- **Evaluation Metrics:** Fidelity Score, Cumulative Regret, and Safety Violation Rate.

## 💡 Key Findings
- **Technical Results:** Successfully identified "silent failures" where the RL agent became stuck in a repetitive, non-optimal action loop.
- **Safety:** Provided a mathematical "kill-switch" trigger for when the agent's fidelity drops below a predefined threshold.
- **Clinical Impact:** Demonstrated that monitoring fidelity is as crucial as monitoring patient vitals in an AI-driven trial.

## 🩺 Clinical Relevance & Impact
In psychiatry, mHealth apps for mood tracking or CBT (Cognitive Behavioral Therapy) often use RL. This framework ensures that the app doesn't become "annoying" or "counter-productive" by sending too many alerts, maintaining patient therapeutic alliance.

## 🔬 Critical Review (Antagonic Perspective)
Fidelity is measured against the agent's *own* logic. If the agent's logic is fundamentally flawed but the agent is "faithful" to it, this framework will not detect the clinical error. It monitors *fidelity*, not *clinical correctness*.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Murphy (2003)] for Micro-Randomized Trials (MRTs).
- **Descendant Discovery:** [Lu et al. (2026)](lu_2026_neural_sdes_suicide_risk.md) for modeling the continuous-time states these apps monitor.
