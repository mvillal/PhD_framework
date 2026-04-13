---
title: "AI for Mental Health: Understanding Clinician Expectations and Priorities"
authors: ["Fischer et al.", "Finale Doshi-Velez"]
year: 2025
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "BMC Psychiatry"
doi: "10.1186/s12888-025-06957-3"
url: "https://bmcpsychiatry.biomedcentral.com/articles/10.1186/s12888-025-06957-3"
datasets: ["EMA", "Clinician Survey"]
tags: ["Human-Centered AI", "Computational Psychiatry", "Clinician Expectations", "Monitoring vs. Prescription"]
---

# AI for Mental Health: Understanding Clinician Expectations and Priorities

## 📋 Executive Summary
This study quantifies clinician expectations and priorities for AI integration in mental health, revealing a significant preference for tools that support continuous monitoring and trajectory forecasting over prescriptive treatment recommendations. It provides a roadmap for "clinician-driven" AI development that prioritizes professional autonomy and diagnostic support.

## 🛠️ Core Methodology
- **Human-Centered Survey Design:** A structured survey of 53 clinicians evaluating 13 potential AI use cases across three domains: monitoring, prescription, and interpretability.
- **Preference Ranking:** Analysis of clinician priorities for model types (e.g., forecasting symptom trajectories vs. selecting specific medications).
- **Sociotechnical Lens:** Examination of how AI fits into time-constrained clinical workflows and the importance of data source transparency.

## 📊 Dataset & Experimental Setup
- **Data Source:** Survey data from 53 clinicians; EMA (Ecological Momentary Assessment) proxy data.
- **Features:** Evaluation of data inputs including self-reports, third-party observations, and high-frequency sensor data.
- **Evaluation Metrics:** Likert-scale preference scores and qualitative rankings of AI "usefulness" vs. "disruption."

## 💡 Key Findings
- **Monitoring > Prescription:** Clinicians strongly favor tools that forecast symptom trajectories (monitoring) over those that suggest specific treatments (prescription).
- **Data Value:** Self-reports and EMA-derived sleep patterns were identified as the most high-signal inputs for psychiatric modeling.
- **Interpretability:** While valued, interpretability was ranked lower than predictive reliability and the ability of the model to flag rare event risks.

## 🩺 Clinical Relevance & Impact
The findings suggest that psychiatric AI should evolve as a "second opinion" for monitoring complex patient trajectories rather than an autonomous prescription agent. This ensures that AI bridges the gap to bedside care by enhancing, rather than replacing, clinical judgment.

## 🔬 Critical Review (Antagonic Perspective)
The preference for monitoring over prescription may reflect "status quo bias" or a defensive posture against algorithmic replacement. Over-relying on monitoring tools without prescriptive guidance might lead to "information overload" for clinicians without providing actionable solutions.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Jacobs et al. (2021) on automation bias in antidepressant selection.
- **Descendant Discovery:** Longitudinal studies on the actual clinical adoption of monitoring vs. prescriptive AI tools.
