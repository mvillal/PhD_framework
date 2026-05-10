---
title: "Using smartphone surveys to predict next-week suicide attempts"
authors: ["Matthew K. Nock", "Jukka-Pekka Onnela", "et al."]
year: 2026
lab: "Nock Lab / Onnela Lab, Harvard University"
venue: "Journal of Psychopathology and Clinical Science"
doi: "10.1037/abnXXXXX"
code: "https://github.com/onnela-lab/beiwe"
datasets: ["Beiwe-Digital-Phenotyping-600", "Smartphone-EMA-Suicide"]
tags: ["Suicide Prediction", "Digital Phenotyping", "EMA", "Sleep Disturbance", "Resistance to Ideation"]
---

# Predicting Next-Week Suicide Risk via Smartphone

## 📋 Executive Summary
Nock, Onnela, et al. (2026) report the results of a landmark longitudinal study using high-frequency smartphone data to predict suicide attempts within a **one-week window**. Traditional clinical assessments often fail because they occur at discrete intervals and rely on patient self-disclosure. By using the **Beiwe** platform to collect both active surveys (EMA) and passive sensor data (GPS, accelerometer), the researchers identified distinct "digital signatures" of acute suicide risk, moving psychiatry toward **Just-in-Time Adaptive Interventions (JITAIs)**.

## 🛠️ Core Methodology
- **Multi-Modal Phenotyping:** Combined active EMA (mood, ideation) with passive background data (mobility, sleep architecture, typing dynamics).
- **Temporal Forecasting:** Used machine learning models to analyze the **"Resistance to Ideation"**—measuring not just how intense a thought is, but how capable the patient feels of resisting it.
- **Sleep & Agitation Analysis:** Leveraged accelerometer data to detect late-night physical agitation as a proxy for sleep disturbance and clinical "pre-relapse."

## 📊 Dataset & Experimental Setup
- **Cohort:** 600 high-risk individuals followed for 6 months post-discharge from psychiatric emergency departments.
- **Ground Truth:** Clinical confirmation of suicide attempts within the monitoring window.

## 💡 Key Findings
- **The "Resistance" Signal:** Diminished ability to resist suicidal thoughts was a stronger predictor of a next-week attempt than the absolute intensity of the thoughts themselves.
- **Sleep Disturbance:** Disturbed sleep (detected via passive sensors) was a primary catalyst for reduced cognitive control and increased acute risk.
- **Superior Precision:** The smartphone-based models identified attempts that clinical interviews missed—80% of those who made attempts in the study had denied intent in their most recent clinician contact.

## 🩺 Clinical Relevance & Impact
The study transforms the smartphone into a **"Clinical Smoke Detector."** Instead of waiting for a crisis appointment, clinicians can be alerted the moment a patient's digital phenotype shifts into a "low resistance / high agitation" state, enabling preemptive interventions like telehealth check-ins or automated safety plans.

## 🔬 Critical Review (Antagonic Perspective)
The framework's effectiveness depends on the patient **continuing to use the phone**. If a patient stops charging the device or deletes the app during a period of high risk, the "smoke detector" goes silent. This **Informative Missingness** is a critical causal confounder that requires explicit modeling (as addressed in Cai et al. 2026).

## 🔗 Discovery & Next Steps
- **Implementation:** Explore using `nixtla` foundation models for detecting the "pre-relapse" anomalies identified in this study.
- **Concept Link:** Updates [Digital Phenotyping](../concepts/digital_phenotyping.md) and [N-of-1 Modeling](../concepts/n_of_1_modeling.md).
