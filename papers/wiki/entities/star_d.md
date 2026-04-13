---
title: "STAR*D (Sequenced Treatment Alternatives to Relieve Depression)"
type: "Entity"
category: "Dataset / Trial"
tags: ["Psychiatry", "MDD", "Antidepressants", "Trial Data"]
---

# STAR*D (Sequenced Treatment Alternatives to Relieve Depression)

## 📋 Overview
The STAR*D trial is one of the largest and longest-running clinical trials for Major Depressive Disorder (MDD), aimed at evaluating the effectiveness of various treatment strategies for patients who do not respond to an initial antidepressant. It has become a foundational dataset for machine learning applications in psychiatric treatment selection.

## 🔬 Role in Research
- **Antidepressant Selection Bias:** Used as the primary patient data source for investigating "automation bias" in AI-assisted treatment selection, demonstrating that clinicians are susceptible to incorrect AI recommendations [[Jacobs & Doshi-Velez (2021)](../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md)].
- **Predictive Modeling:** STAR*D data is frequently used to train models aimed at personalizing treatment sequences for depression, although the lack of a control group in later stages presents challenges for causal inference.

## 📊 High-Signal Metrics & Characteristics
- **Scope:** Multi-site trial (outpatient settings) with several levels of treatment sequences.
- **Clinician Impact:** Research using STAR*D has shown that incorrect ML recommendations can significantly decrease clinician accuracy in selecting the correct level of care [[Jacobs & Doshi-Velez (2021)](../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md)].

## 🔗 Related Sources
- [Jacobs & Doshi-Velez (2021): Automation Bias in Antidepressant Selection](../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md)
- [Jacobs & Doshi-Velez (2023): Human-Labeling Bias](../../sources/doshi-velez/jacobs_2023_human_labeling_bias.md)
