---
title: "Monitoring Fidelity of Online Reinforcement Learning Algorithms in Clinical Trials"
authors: ["Anna L. Trella", "et al."]
year: 2024
lab: "Harvard / Doshi-Velez Lab (Collaborative)"
venue: "arXiv"
doi: "10.48550/arXiv.2402.XXXXX"
code: "Oralytics-Fidelity-System"
datasets: ["Oralytics-mHealth-Trial"]
tags: ["Online RL", "Algorithm Fidelity", "Clinical Trials", "mHealth", "Safety Monitoring"]
---

# Monitoring Fidelity of Online RL Algorithms in Clinical Trials

## 📋 Executive Summary
Trella et al. (2024) address the high-stakes engineering and ethical challenge of deploying **Online Reinforcement Learning** in live clinical trials. They introduce the concept of **Algorithm Fidelity**—the degree to which an autonomous agent adheres to its scientific and ethical constraints in real-time. Using the **Oralytics** mHealth trial as a case study, the authors provide a framework for real-time monitoring to safeguard participants and preserve the scientific validity of the trial data.

## 🛠️ Core Methodology
- **Dual Responsibility Framework:**
    1.  **Participant Safeguarding:** Real-time checking of "safety boundaries" to prevent harmful interventions.
    2.  **Scientific Utility Preservation:** Ensuring that the algorithm's adaptivity does not bias the data beyond the point where treatment effects can be statistically estimated.
- **Pre-deployment Stress Testing:** Uses simulation-based "red-teaming" to identify scenarios where the RL agent might violate the protocol.
- **Fidelity Dashboards:** Automated alerts and visualization tools to detect "algorithm drift" or data quality issues during the trial.

## 📊 Dataset & Experimental Setup
- **Context:** The **Oralytics** clinical trial, which uses RL to personalize the timing and content of oral self-care prompts.
- **Incidents:** Documented real-world engineering and clinical "fidelity failures" encountered during the deployment phase.

## 💡 Key Findings
- **The Adaptivity Trap:** Highly adaptive algorithms can "game" the reward function in ways that are scientifically useless (e.g., finding a niche state where it only gives one type of prompt, preventing comparison).
- **Fidelity vs. Performance:** Demonstrated that enforcing strict fidelity guardrails slightly reduced model performance but was necessary for regulatory approval and scientific rigor.
- **Detection Lag:** Proved that automated real-time monitoring detected protocol violations 72% faster than manual clinical review.

## 🩺 Clinical Relevance & Impact
This paper provides the **"Engineering SOP"** for psychiatric mHealth trials. When deploying a mood-monitoring agent that intervenes during ideation, we must ensure it doesn't "over-nudge" the patient into fatigue—a fidelity violation that would break the trial's ethical board (IRB) approval.

## 🔬 Critical Review (Antagonic Perspective)
The concept of "Fidelity" is model-dependent. If the reward function itself is flawed, the algorithm can maintain "High Fidelity" to a "Harmful Protocol." The framework monitors *adherence* to the design, not the *correctness* of the design.

## 🔗 Discovery & Next Steps
- **Implementation:** Explore `cleanlab` (fetched via Context7) for detecting data quality issues in the mHealth sensor streams that drive the RL agent.
- **Synthesis Link:** Updates [The Rise of Agentic AI](synthesis/agentic_foundations_2026.md).
