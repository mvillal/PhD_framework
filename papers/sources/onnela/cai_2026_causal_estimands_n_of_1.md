---
title: "Causal estimands and identification of time-varying effects in non-stationary time series from N-of-1 mobile device data"
authors: ["Xiaoxuan Cai", "Jukka-Pekka Onnela", "et al."]
year: 2026
lab: "Onnela Lab, Harvard T.H. Chan School of Public Health"
venue: "Biostatistics"
doi: "10.1093/biostatistics/kxaeXXXX"
code: "https://github.com/onnela-lab/SSMimpute"
datasets: ["Bipolar Longitudinal Study (BLS)", "Beiwe-Platform-Data"]
tags: ["Causal Inference", "N-of-1", "Non-Stationarity", "Digital Phenotyping", "Time-Varying Effects"]
---

# Causal estimands and identification of time-varying effects in N-of-1 mobile data

## 📋 Executive Summary
Cai et al. (2026) tackle the foundational statistical challenge of performing **Causal Inference** on high-frequency, non-stationary digital phenotyping data. Traditional causal methods assume stationarity (stable mean/variance), but smartphone-collected behavioral data (mobility, social activity) is inherently non-stationary and prone to "unit roots." This paper defines new causal estimands that allow researchers to identify **Time-Varying Individual Treatment Effects** in N-of-1 trials, specifically for bipolar and schizophrenia monitoring.

## 🛠️ Core Methodology
- **N-of-1 Causal Framework:** Moves away from population averages (ATE) to individual-level causal effects (ITE), where a single participant serves as their own control over time.
- **Handling Non-Stationarity:** Proposes estimands that remain valid even when the time series contains "unit roots" or stochastic drifts.
- **Identification Strategy:** Uses time-varying propensity scores and marginal structural models (MSMs) adapted for single-subject time-series data.
- **SSMimpute Integration:** Leverages State-Space Model imputation to handle the "Informative Missingness" (MNAR) common in psychiatric smartphone studies.

## 📊 Dataset & Experimental Setup
- **Evaluation:** Validated on the **Bipolar Longitudinal Study (BLS)** dataset (n=74, 5-year longitudinal monitoring).
- **Data Source:** High-frequency sensor data collected via the **Beiwe** open-source smartphone platform.

## 💡 Key Findings
- **Dynamic Causal Effects:** Demonstrated that the effect of social activity on mood is not constant but varies based on the patient's current state (e.g., euthymic vs. depressed).
- **Robustness:** The new estimands showed significantly lower bias compared to standard ARIMAX or simple regression models when unit roots were present in the behavioral data.
- **Identification:** Established the "causal identifiability" conditions required for mobile health data, bridging the gap between time-series econometrics and clinical ML.

## 🩺 Clinical Relevance & Impact
The ability to identify *when* an intervention is causally effective for a *specific* individual is the holy grail of personalized psychiatry. This framework enables **Adaptive Interventions** that can be triggered only when the causal effect of a prompt (e.g., "Go for a walk") is predicted to be positive for that specific patient at that specific time.

## 🔬 Critical Review (Antagonic Perspective)
The framework requires extremely long, high-quality longitudinal data (N-of-1) to achieve statistical power, which may be difficult to obtain in acute psychiatric settings. Additionally, it assumes that the time-varying confounders are correctly captured by the sensors—a significant "hidden confounding" risk.

## 🔗 Discovery & Next Steps
- **Concept Link:** Updates [N-of-1 Modeling](../concepts/n_of_1_modeling.md) and [Digital Phenotyping](../concepts/digital_phenotyping.md).
- **Implementation:** Explore using `causalml`'s propensity models for the identification stage of this framework.
