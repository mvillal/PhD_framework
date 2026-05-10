---
title: "Learning-to-defer for sequential medical decision-making under uncertainty"
authors: ["Joshi et al."]
year: 2021
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "TMLR / arXiv"
doi: "10.48550/arXiv.2109.06312"
code: "https://github.com/shalmali-joshi/sequential-l2d"
datasets: ["Sepsis-Diabetes-Sim", "MIMIC-III"]
tags: ["Learning to Defer", "L2D", "Sequential Decision Making", "Human-AI Alignment", "Pre-emptive Deferral"]
---

# Learning-to-defer for sequential medical decision-making under uncertainty

## 📋 Executive Summary
Joshi et al. (2021) introduce a framework for **Sequential Learning-to-Defer (SLTD)** in medical settings. Traditional L2D is "myopic"—it only considers whether to defer a task (hand it to a human) based on the immediate prediction's reliability. However, in medicine, an AI's action now could lead the patient into a future state where neither the AI nor the human can intervene effectively. SLTD treats deferral as a sequential planning problem, allowing the AI to **pre-emptively defer** control to a human expert when long-term uncertainty becomes too high.

## 🛠️ Core Methodology
- **Sequential Formulation:** Casts L2D as an **Offline Model-Based RL** problem. The agent learns a policy $\pi(s, h)$ that decides at each step whether to act or defer.
- **Pre-emptive Deferral:** Uses the **Value of Information (VoI)** to calculate if deferring *now* is better than waiting. It defers early if delaying the deferral increases the risk of irreversible patient harm.
- **Posterior Sampling:** Accounts for environment uncertainty by sampling from a distribution of possible patient dynamics, ensuring the deferral rule is robust to noisy clinical data.

## 📊 Dataset & Experimental Setup
- **Evaluation:** Tested on a semi-synthetic **Sepsis-Diabetes simulator** where clinician availability and patient stability fluctuate.
- **Metrics:** Balanced patient outcomes (survival/stability) against "human burden" (number of deferrals).

## 💡 Key Findings
- **Superior Risk Management:** SLTD outperformed myopic baselines by identifying "points of no return" up to 12 hours before a clinical crash, deferring while a human could still intervene.
- **Resource Efficiency:** By only deferring when long-term uncertainty was high, the model reduced unnecessary clinician interruptions compared to simple uncertainty-threshold models.
- **Intentional Deferral:** Deferrals were decomposing into "informative" handovers where the model explicitly flags its lack of knowledge about specific future drug interactions.

## 🩺 Clinical Relevance & Impact
This paper is the cornerstone of **Trustworthy Clinical Collaboration**. It ensures that AI acts not just as a recommender, but as a "co-pilot" that knows its own long-term limitations. In psychiatry, this applies to titrating medications where the AI may be confident for the next week but uncertain about the 1-month relapse risk, triggering a human review early.

## 🔬 Critical Review (Antagonic Perspective)
The framework assumes we can model the "human expert" accurately. If the AI defers to a human who is fatigued or biased, the SLTD system will still record a "successful deferral" despite potentially poor outcomes. The model's reliance on "offline model-based RL" also means it is sensitive to how well the simulator reflects real clinical reality.

## 🔗 Discovery & Next Steps
- **Concept Link:** Core to [Learning to Defer](../concepts/learning_to_defer.md) and [Automation Bias](../concepts/automation_bias.md).
- **Implementation:** Explore `skrl` or `torchrl` for implementing the offline model-based RL logic for SLTD.
