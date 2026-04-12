---
title: "How Much Should You Trust Your Explanation? Understanding the Impact of Interpretability on Automation Bias"
authors: ["Maia Jacobs", "Melanie F. Pradier", "Thomas H. McCoy", "Roy H. Perlis", "Finale Doshi-Velez"]
year: 2021
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "CHI Conference on Human Factors in Computing Systems"
doi: "https://doi.org/10.1145/3411764.3445100"
url: "https://doi.org/10.1145/3411764.3445100"
code: "N/A"
datasets: ["STAR*D"]
tags: ["XAI", "Automation Bias", "Psychiatry", "Clinician Trust"]
---

# How Much Should You Trust Your Explanation? Understanding the Impact of Interpretability on Automation Bias

## 📋 Executive Summary
This paper investigates how different AI explanation types influence clinician decision-making in antidepressant selection. Using clinical vignettes from the STAR*D trial, it demonstrates that while explanations are intended to build trust, they often inadvertently increase automation bias, making clinicians more likely to follow incorrect AI recommendations.

## 🛠️ Core Methodology
The study employed a randomized experiment with three distinct types of eXplainable AI (XAI) presentations:
- **Feature Importance:** Highlights specific patient features (e.g., symptom severity, age) that most influenced the model's prediction.
- **Example-based:** Presents similar historical patient cases from the dataset that align with the current prediction.
- **Rule-based:** Provides the explicit logic or decision trees used by the model to reach its conclusion.

## 📊 Dataset & Experimental Setup
- **Data Source:** Clinical vignettes derived from the **STAR*D** (Sequenced Treatment Alternatives to Relieve Depression) trial.
- **Sample Size:** **220 clinicians** (psychiatrists and primary care physicians).
- **Features:** Patient demographics, symptom profiles, and treatment history.
- **Evaluation Metrics:** Selection accuracy, clinician confidence, and rate of automation bias (following incorrect AI).

## 💡 Key Findings
- **Technical Results:** Clinicians followed incorrect AI recommendations significantly more often when an explanation was provided compared to no explanation.
- **Statistical Significance:** Automation bias was pervasive across all XAI types, with no significant difference between feature importance, example-based, or rule-based methods in mitigating error detection.
- **Ablation Studies:** The presence of *any* explanation tended to override clinician skepticism, even when the AI's logic was flawed.

## 🩺 Clinical Relevance & Impact
Highlights a critical safety gap in clinical AI deployment: explanations can act as a "veneer of transparency" that masks model errors. In psychiatry, where treatment selection (like antidepressants) is complex, this study warns that current XAI methods may lead to suboptimal patient care if not paired with better error-detection mechanisms.

## 🔬 Critical Review (Antagonic Perspective)
The study uses vignettes rather than real-time clinical encounters, which may not fully capture the high-stakes environment of bedside care. Furthermore, the "correct" treatment was established by a panel of 5 experts, which itself may be subject to consensus bias.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Gottesman et al. (2019)](gottesman_2019_clinical_rl_guidelines.md) for foundational clinical RL challenges.
- **Descendant Discovery:** [Jacobs et al. (2023)](jacobs_2023_human_labeling_bias.md) for follow-up on human-labeling bias and trust.
