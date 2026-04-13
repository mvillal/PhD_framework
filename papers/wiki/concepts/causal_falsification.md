# Causal Falsification

## 📄 Definition
**Causal Falsification** is a statistical framework for auditing and rejecting causal claims or decision policies learned from observational data. It uses high-fidelity, unbiased data (e.g., from randomized controlled trials) to "falsify" models that may be compromised by hidden confounding or administrative bias.

## 🛠️ Key Methodologies
- **RCT-to-EHR Auditing:** Using small-scale RCT data as a "ground truth" to test the validity of policies learned from large-scale EHR datasets (e.g., MIMIC-III).
- **Policy Rejection:** Statistical tests designed to identify when a policy's estimated value is significantly different from its actual performance in a controlled setting (Mozannar & Sontag, 2025).

## 🩺 Clinical Relevance
- **Safeguarding AI Deployment:** Preventing the deployment of "shortcut-learning" models in life-critical settings like oncology and sepsis.
- **Improving Trust:** Providing clinicians with a rigorous "safety certificate" for an AI recommendation.

## ⚠️ Critical Challenges
- **The Data Bottleneck:** Causal Falsification requires high-fidelity, unbiased data (often from Randomized Controlled Trials) to audit observational policies. In data-sparse domains like psychiatry or for rare clinical conditions, the required "audit data" may be non-existent or insufficient for robust falsification.
- **Transportability Assumptions:** The method assumes the RCT cohort is sufficiently representative of the observational population [[Mozannar & Sontag (2025)](../../sources/sontag/mozannar_2025_causal_falsification.md)].


## 🔗 Related Concepts
- [[offline_rl]]
- [[causal_ope]]
- [[automation_bias]]
