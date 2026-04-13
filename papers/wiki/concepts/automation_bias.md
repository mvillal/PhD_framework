---
title: "Automation Bias in Healthcare"
type: "Concept"
category: "Human-AI Interaction"
tags: ["Human Factors", "Explainable AI", "XAI", "Antidepressants", "Psychiatry"]
---

# Automation Bias in Healthcare

## 📋 Overview
Automation Bias refers to the tendency of humans (including clinicians) to favor suggestions from automated decision-making systems and to ignore contradictory information, even when the automated system is incorrect. In clinical settings, this bias can lead to "overreliance," where clinicians follow incorrect AI recommendations, potentially compromising patient safety.

## 🔬 Role in Clinical Research
- **Antidepressant Selection:** Research using **STAR*D** data demonstrated that clinicians are susceptible to automation bias when selecting antidepressants, often following incorrect AI recommendations [[Jacobs & Doshi-Velez (2021)](../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md)].
- **XAI Impact:** Ironically, the addition of simple, human-interpretable "explanations" to AI outputs can inadvertently *increase* automation bias, as the explanations make the erroneous output seem more trustworthy to the clinician [[Jacobs & Doshi-Velez (2021)](../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md)].
- **Human-Labeling Bias:** Beyond automation bias, researchers have identified a "human-labeling bias" (or algorithm aversion), where clinicians may also trust recommendations more if they believe they originated from a human peer rather than an AI [[Jacobs & Doshi-Velez (2023)](../../sources/doshi-velez/jacobs_2023_human_labeling_bias.md)].

## 📊 High-Signal Metrics & Characteristics
- **Impact:** Study results show a significant decrease in clinician decision-making accuracy when presented with incorrect ML recommendations paired with explanations.
- **Framework:** Automation bias is categorized based on "overreliance" (following incorrect AI) and "underreliance" (ignoring correct AI).

## 🔗 Related Sources
- [Jacobs & Doshi-Velez (2021): Automation Bias in Antidepressant Selection](../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md)
- [Jacobs & Doshi-Velez (2023): Human-Labeling Bias](../../sources/doshi-velez/jacobs_2023_human_labeling_bias.md)
- [Fischer & Doshi-Velez (2025): Clinician Expectations](../../sources/doshi-velez/fischer_2025_clinician_expectations.md)
