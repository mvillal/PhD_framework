---
title: "Monitoring Fidelity of Online Reinforcement Learning Algorithms in Clinical Trials"
authors: ["Trella et al.", "Finale Doshi-Velez"]
year: 2024
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "arXiv / AAAI"
doi: "10.48550/arXiv.2402.17003"
url: "https://arxiv.org/abs/2402.17003"
datasets: ["Oralytics", "mHealth Simulated Data"]
tags: ["Algorithm Fidelity", "Online RL", "Clinical Trials", "mHealth", "Oralytics"]
---

# Monitoring Fidelity of Online Reinforcement Learning Algorithms in Clinical Trials

## 📋 Executive Summary
This paper introduces the concept of "Algorithm Fidelity" for online Reinforcement Learning (RL) in mobile health (mHealth) clinical trials. Using the Oralytics trial as a case study, the authors develop a framework to monitor whether an autonomous RL agent is behaving as intended, ensuring both participant safety and the scientific validity of the trial's data.

## 🛠️ Core Methodology
- **Algorithm Fidelity Framework:** Defined by two key responsibilities: (1) safeguarding the participants (Safety) and (2) preserving the scientific utility of the data for post-trial analysis (Validity).
- **Real-Time Monitoring:** Implementation of a "Red/Yellow/Green" status system to flag anomalous algorithm behavior based on deviation from expected reward trajectories or action distributions.
- **Contextual Bandits (Oralytics):** A Thompson-Sampling-based contextual bandit that personalizes the timing and content of push notifications.

## 📊 Dataset & Experimental Setup
- **Data Source:** Deployment data from the **Oralytics** clinical trial (a mobile oral health intervention).
- **Participants:** n = 72 individuals at risk for dental disease over a 10-week monitoring period.
- **Evaluation Metrics:** Action-selection probabilities, exploration rates, and "Fidelity Violations" per participant-day.

## 💡 Key Findings
- **Real-time Detection:** Successfully identifies and flags situations where technical issues (e.g., missing data, sensor failures) cause the RL agent to behave in ways that would compromise the trial's results.
- **Safety Overrides:** Provides a principled way to temporarily override the autonomous agent without abandoning the entire trial's adaptive design.
- **Scientific Utility:** Ensures that the data collected during the adaptive trial remains usable for robust post-hoc causal evaluation (OPE).

## 🩺 Clinical Relevance & Impact
Critically important for psychiatric mHealth interventions (e.g., adaptive suicide risk notifications). By ensuring "Algorithm Fidelity," researchers can deploy autonomous agents with higher confidence that the system will not inadvertently harm the patient or produce uninterpretable clinical data.

## 🔬 Critical Review (Antagonic Perspective)
Strict fidelity monitoring might suppress the RL agent's ability to "explore" truly novel but safe strategies if those strategies are outside of narrow pre-defined bounds. There is also the risk of "monitoring fatigue" for researchers if the sensitivity of the flagging system is too high.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Klasnja et al. (2015) on microrandomized trials (MRTs).
- **Descendant Discovery:** Integrating fidelity monitoring with Neural SDE-based risk forecasting.
