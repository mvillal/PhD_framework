---
title: "How machine-learning recommendations influence clinician treatment selections: the example of antidepressant selection"
authors: ["Jacobs et al."]
year: 2021
lab: "Harvard / Doshi-Velez Lab (Collaborative)"
venue: "Translational Psychiatry"
doi: "10.1038/s41398-021-01224-x"
code: "https://github.com/fairlearn/fairlearn (Mitigation Standard)"
datasets: ["STAR*D", "Clinician-RCT-220"]
tags: ["Antidepressant Bias", "Automation Bias", "Clinical Fairness", "Human-AI Interaction", "Decision Support"]
---

# How machine-learning recommendations influence clinician treatment selections

## 📋 Executive Summary
Jacobs et al. (2021) investigate the "Human-in-the-loop" dynamics of antidepressant selection using machine learning. Through a randomized study with 220 clinicians, the paper explores whether AI recommendations improve treatment accuracy and how clinicians respond to incorrect or biased AI advice. The findings serve as a major cautionary tale for psychiatric AI, revealing that current ML decision support can inadvertently worsen clinical performance through **Automation Bias** without providing a net accuracy gain.

## 🛠️ Core Methodology
- **Randomized Controlled Trial (RCT) with Clinicians:** Clinicians were presented with psychiatric cases (based on STAR*D) and asked to select the best antidepressant, with or without AI assistance.
- **Intervention Types:** Tested "AI recommendation only" vs. "AI recommendation + explanation."
- **Fairness Assessment:** Analyzed whether AI tools propagated historical biases found in psychiatric datasets across different demographic subgroups.

## 📊 Dataset & Experimental Setup
- **Dataset:** Derived from the **STAR*D** (Sequenced Treatment Alternatives to Relieve Depression) trial.
- **Participants:** 220 psychiatrists and general practitioners.
- **Primary Metric:** Treatment selection accuracy and "adherence" to AI recommendations.

## 💡 Key Findings
- **No Accuracy Improvement:** AI recommendations did **not** significantly improve clinician accuracy compared to the unassisted baseline.
- **Automation Bias:** When the AI was wrong, clinician accuracy plummeted. Clinicians often deferred to the tool even when their own clinical judgment was initially correct.
- **Ineffectiveness of Explanations:** Providing an "interpretable explanation" for the AI's choice did **not** mitigate the drop in accuracy when the AI was wrong. Explanations may have actually *increased* over-reliance by providing a false sense of security.
- **Disparate Impact:** The paper highlights the risk that biased algorithms will lead clinicians to make biased prescribing decisions, potentially widening mental health disparities.

## 🩺 Clinical Relevance & Impact
The study emphasizes that **Interpretability is not enough**. For psychiatric AI to be safe, it must not only be accurate but must also be designed to **encourage critical thinking** rather than passive deference. This led to the development of "Reflection-based AI" and "Learning to Defer" (L2D) paradigms.

## 🔬 Critical Review (Antagonic Perspective)
The study uses STAR*D data, which is itself over a decade old and may not reflect current prescribing habits or drug availability. Furthermore, the "accuracy" metric assumes there is a single "best" antidepressant for every patient, which is a subject of debate in personalized psychiatry.

## 🔗 Discovery & Next Steps
- **Implementation:** Utilize `fairlearn` to audit clinical models for **Equalized Odds** and **Demographic Parity** to prevent the bias propagation identified by Jacobs.
- **Concept Link:** Foundational to [Automation Bias](../concepts/automation_bias.md) and [Learning to Defer](../concepts/learning_to_defer.md).
