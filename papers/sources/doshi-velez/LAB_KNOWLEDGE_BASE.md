# Doshi-Velez Lab (Data to Actionable Knowledge - DtAK)

**Principal Investigator:** Finale Doshi-Velez (Harvard SEAS)
**Primary Lab Affiliation:** Harvard John A. Paulson School of Engineering and Applied Sciences

## Core Research Timeline & Key Contributors

### 2019 - Foundational Clinical RL
- **Gottesman, Futoma, Liu, & Doshi-Velez (2019):** Established the foundational "Guidelines for Clinical Reinforcement Learning," introducing FQE, Batch RL safety protocols, and robustness to unmeasured confounding.

### 2020 - Critical Assessment of Generalizability
- **Futoma, Simons, & Doshi-Velez (2020):** Challenged the "Myth of Generalizability" in *The Lancet Digital Health*, identifying that models often learn local administrative patterns over universal biology and advocating for local utility.

### 2021-2023 - Human-AI Trust & Bias
- **Jacobs & Doshi-Velez (2021):** Revealed in *Translational Psychiatry* that XAI can inadvertently increase automation bias in antidepressant selection, even when recommendations are incorrect.
- **Joshi, Parbhoo, & Doshi-Velez (2021):** Proposed "Sequential Learning-to-Defer" (SLTD) to determine when clinical RL agents should hand over control to human experts based on uncertainty propagation.
- **Zhang & Doshi-Velez (2021):** Identified critical "Decision Points" in clinical trajectories to improve the safety and interpretability of batch RL in intensive care.
- **Havasi, Parbhoo, & Doshi-Velez (2022):** Identified information leakage in Concept Bottleneck Models (CBMs) and proposed mitigation strategies to ensure reliable human-AI collaboration.
- **Maslej, Jacobs, & Doshi-Velez (2023):** Identified "Human-Labeling Bias" and algorithm aversion, where clinicians inherently trust recommendations attributed to human peers over AI.

### 2022 - Causal Off-Policy Evaluation
- **Parbhoo, Hüyük, & Doshi-Velez (2022):** Introduced SCM-based Causal OPE in *Nature Machine Intelligence* to reliably evaluate treatment optimality and transportability across different populations.

### 2024 - Algorithmic Regularization & Fidelity
- **Jiang & Doshi-Velez (2024):** Developed state-action-specific discount regularization to handle low-data regimes and unintended consequences in clinical offline RL.
- **Trella & Doshi-Velez (2024):** Proposed real-time algorithm fidelity monitoring (Safety and Validity) for online mHealth trials (Oralytics).

### 2025-2026 - Continuous-Time & Strategic Modeling
- **Hang & Doshi-Velez (2025):** Introduced Latent Similarity Gaussian Processes (LSGP) for suicide forecast in patients with sparse EMA data by "borrowing strength" from similar cohorts.
- **Fischer & Doshi-Velez (2025):** Quantified clinician preferences for trajectory monitoring over prescriptive treatment suggestions in *BMC Psychiatry*.
- **Hüyük & Doshi-Velez (2025):** Developed "Strategic Link Scores" to explain long-term sequential dependencies and "set-up/pay-off" action pairs in clinical planning.
- **Lu & Doshi-Velez (2026):** Implemented Neural SDEs on compact state spaces for continuous-time suicide risk modeling with bounded 0-10 scales.

## Research Pillars Summary

### 1. Clinical RL Safety (Deadly Triad, OPE)
Focuses on the challenges of applying Reinforcement Learning in clinical settings, emphasizing robust Off-Policy Evaluation (OPE), state-action regularization, and handling the "Deadly Triad".

### 2. Human-AI Interaction (Automation Bias, XAI)
Investigates the human factors of clinical AI, studying "Automation Bias," "Human-Labeling Bias," and developing XAI techniques like Strategic Link Scores that provide meaningful insights.

### 3. Causal Inference in EHR
Leverages EHR data to perform causal inference, utilizing SCMs to identify treatment effects that are transportable across different clinical sites and populations (HIV/Sepsis).

### 4. The Myth of Generalizability
Emphasizes local validation over global metrics, recognizing that clinical data is heavily influenced by site-specific administrative and practice patterns.

### 5. Continuous-Time Risk Modeling (Neural SDEs & GPs)
Utilizes Neural SDEs and LSGPs to model risk trajectories in continuous time, particularly for high-frequency psychiatric monitoring and rare event forecasting (Suicide Risk).

### 6. mHealth and Real-Time RL Monitoring
Develops frameworks like "Algorithm Fidelity" to monitor the safety and scientific validity of autonomous agents in online mobile health settings (Oralytics).
