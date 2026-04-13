# Doshi-Velez Lab (Data to Actionable Knowledge - DtAK)

**Principal Investigator:** Finale Doshi-Velez (Harvard SEAS)
**Primary Lab Affiliation:** Harvard John A. Paulson School of Engineering and Applied Sciences

## Core Research Timeline & Key Contributors

### 2019 - Foundational Clinical RL
- **Gottesman et al. (2019):** Established the "Guidelines for Clinical Reinforcement Learning," introducing FQE and Batch RL safety protocols.

### 2020 - Critical Assessment of Generalizability
- **Futoma et al. (2020):** Challenged the "Myth of Generalizability," identifying that models often learn local practice patterns over universal biology.

### 2021-2023 - Human-AI Trust & Bias
- **Jacobs et al. (2021):** Revealed that XAI (Feature Importance, Example-based, Rule-based) can inadvertently increase automation bias in antidepressant selection.
- **Jacobs et al. (2023):** Identified "Human-Labeling Bias," where clinicians inherently trust recommendations attributed to human peers over AI.

### 2022 - Causal Off-Policy Evaluation
- **Parbhoo et al. (2022):** Introduced SCM-based Causal OPE and "Causal Transportability" to reliably evaluate policies across different patient populations (HIV/Sepsis).

### 2024 - Algorithmic Regularization & Fidelity
- **Jiang et al. (2024):** Developed state-action-specific discount regularization to handle low-data regimes in offline RL.
- **Trella et al. (2024):** Proposed real-time algorithm fidelity monitoring for online mHealth trials (Oralytics).

### 2025-2026 - Continuous-Time & Strategic Modeling
- **Hang et al. (2025):** Introduced LSGP for suicide forecast in patients with sparse data by "borrowing strength" from similar cohorts.
- **Fischer et al. (2025):** Quantified clinician preferences for trajectory monitoring over prescriptive treatment suggestions.
- **Huyuk et al. (2025):** Developed "Strategic Link Scores" to explain long-term sequential dependencies in clinical actions.
- **Lu et al. (2026):** Implemented Neural SDEs for continuous-time suicide risk modeling with compact state space constraints (0-10 scales).

## Research Pillars Summary

### 1. Clinical RL Safety (Deadly Triad, OPE)
Focuses on the challenges of applying Reinforcement Learning in clinical settings, emphasizing robust Off-Policy Evaluation (OPE) and handling the "Deadly Triad".

### 2. Human-AI Interaction (Automation Bias, XAI)
Investigates the human factors of clinical AI, studying "Automation Bias" and developing XAI techniques that provide meaningful, strategically-linked insights.

### 3. Causal Inference in EHR
Leverages EHR data to perform causal inference, utilizing SCMs to identify treatment effects that are transportable across different clinical sites.

### 4. The Myth of Generalizability
Emphasizes local validation over global metrics, recognizing that clinical data is heavily influenced by administrative and practice patterns.

### 5. Continuous-Time Risk Modeling (Neural SDEs)
Utilizes Neural SDEs to model risk trajectories in continuous time, particularly for high-frequency psychiatric monitoring (EMA).

### 6. mHealth and Real-Time RL Monitoring
Develops frameworks to monitor the fidelity and safety of autonomous agents in mobile health settings.
