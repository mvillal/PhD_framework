---
title: "How machine-learning recommendations influence clinician treatment selections: the example of the antidepressant selection"
authors: ["Maia Jacobs", "Finale Doshi-Velez"]
year: 2021
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "Translational Psychiatry / CHI"
doi: "10.1038/s41398-021-01224-x"
url: "https://www.nature.com/articles/s41398-021-01224-x"
datasets: ["STAR*D", "Clinician Performance Data"]
tags: ["Automation Bias", "Interpretability", "Antidepressant Selection", "Human-AI Alignment"]
---

# How machine-learning recommendations influence clinician treatment selections: the example of the antidepressant selection

## 📋 Executive Summary
This paper investigates the empirical impact of ML recommendations and their explanations on clinician decision-making in the context of Major Depressive Disorder (MDD). The study identifies a critical "automation bias," showing that clinicians are significantly influenced by incorrect AI recommendations, especially when paired with simple, human-interpretable explanations.

## 🛠️ Core Methodology
- **Randomized Controlled Experiment:** Evaluated clinician decisions with and without ML support, across different explanation types (Feature Importance, Rule-based, Example-based).
- **Explanation Impact Analysis:** Measured how "interpretability" (XAI) affects the clinician's propensity to override or follow the AI.
- **Automation Bias Framework:** Defined based on "overreliance" (following incorrect AI) and "underreliance" (ignoring correct AI).

## 📊 Dataset & Experimental Setup
- **Data Source:** Patient data derived from the STAR*D trial (Sequenced Treatment Alternatives to Relieve Depression).
- **Participants:** n = 50+ clinicians including psychiatrists and primary care physicians.
- **Clinical Task:** Selecting the most appropriate next-step medication for patients who failed initial MDD treatment.
- **Evaluation Metrics:** Accuracy, Decision Time, and Confidence Scores.

## 💡 Key Findings
- **No Overall Accuracy Improvement:** Clinician accuracy did not significantly improve with ML support compared to the baseline (human-only) group.
- **Interpretable Bias:** Incorrect ML recommendations paired with explanations led to a significant decrease in clinician accuracy, as the "explanations" inadvertently increased the perceived trust in the erroneous output (automation bias).
- **Cognitive Load:** While ML support aimed to reduce complexity, the addition of interpretability layers often increased the time taken for decision-making without a proportional gain in performance.

## 🩺 Clinical Relevance & Impact
The findings caution against the simple addition of "explainability" in psychiatric AI. In antidepressant selection, where there is no clear clinical gold standard, AI systems must be designed to promote "cognitive forcing" (requiring active clinician analysis) rather than passive acceptance.

## 🔬 Critical Review (Antagonic Perspective)
The study uses a simplified, discrete-choice interface that may not reflect the iterative and nuanced nature of real-world psychiatric consultations. The "incorrect" ML recommendations were synthetic, which might not capture the subtle failure modes of actual clinical models.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Parasuraman & Manzey (2010) on the ergonomics of automation.
- **Descendant Discovery:** Jacobs et al. (2023) on "Human-Labeling Bias" as a further extension of trust dynamics.
