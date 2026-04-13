---
title: "Using smartphone surveys to predict next-week suicide attempts"
authors: ["M.K. Nock", "J.P. Onnela"]
year: 2026
lab: "Nock Lab / Onnela Lab, Harvard"
venue: "Journal of Psychopathology and Clinical Science"
doi: "TBD"
code: "Beiwe Platform"
datasets: ["High-Risk Patient Cohort"]
tags: ["Suicide Forecasting", "Smartphone Monitoring", "EMA", "Predictive Modeling"]
---

# Using smartphone surveys to predict next-week suicide attempts

## 📋 Executive Summary
This study uses high-frequency smartphone surveys (EMA) collected via the **Beiwe** platform to predict suicide attempts within a one-week horizon in high-risk patients. It demonstrates that real-time data on thoughts and behaviors can significantly outperform static clinical predictors.

## 🛠️ Core Methodology
- **Short-Term Risk Forecasting:** Focused on the "next-week" window, the most critical timeframe for clinical intervention.
- **Ecological Momentary Assessment (EMA):** Patients provide multiple daily self-reports on suicidal ideation, mood, and stress.
- **Feature Engineering:** Analysis of symptom volatility, persistence, and transition points in suicidal thoughts.

## 📊 Dataset & Experimental Setup
- **Data Source:** High-risk psychiatric patients recently hospitalized for suicidal ideation or attempt.
- **Evaluation Metrics:** AUPRC (Area Under Precision-Recall Curve) for rare event detection.

## 💡 Key Findings
- **Real-Time Signal:** Dynamic changes in suicidal thoughts are much stronger predictors of near-term attempts than long-term history or demographic factors.
- **Accuracy:** The model identifies a high percentage of patients who go on to attempt within the next week, providing a viable tool for clinical flagging.

## 🩺 Clinical Relevance & Impact
Provides a "just-in-time" warning system for suicide prevention, allowing clinicians to escalate care when a patient enters a high-risk window.

## 🔬 Critical Review (Antagonic Perspective)
High-frequency surveys can be burdensome for patients in crisis. There is also the "Hawthorne Effect" to consider: does intensive monitoring itself change the risk trajectory (potentially for better or worse)?

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Kleiman et al. (2017) on the use of EMA to study suicidal thoughts.
- **Descendant Discovery:** Integrating passive sensing (GPS, activity) to improve prediction without increasing survey burden.
