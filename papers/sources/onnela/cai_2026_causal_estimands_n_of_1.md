---
title: "Causal estimands and identification of time-varying effects in non-stationary time series from N-of-1 mobile device data"
authors: ["Xuekui Cai", "J.P. Onnela"]
year: 2026
lab: "Onnela Lab, Harvard T.H. Chan School of Public Health"
venue: "Biostatistics"
doi: "TBD"
code: "Beiwe Platform"
datasets: ["N-of-1 Mobile Device Data"]
tags: ["Causal Inference", "N-of-1 Modeling", "Non-stationary Time Series", "Digital Phenotyping"]
---

# Causal estimands and identification of time-varying effects in non-stationary time series from N-of-1 mobile device data

## 📋 Executive Summary
This paper addresses the fundamental statistical challenge of causal inference in digital phenotyping: identifying how an intervention affects a single individual over time (N-of-1). It defines causal estimands for time-varying effects in non-stationary time series, providing a rigorous framework for personalized clinical monitoring using mobile devices.

## 🛠️ Core Methodology
- **N-of-1 Causal Framework:** Moving beyond population-level averages to individual-level causal effects.
- **Time-Varying Effects:** Modeling how the impact of an intervention (e.g., medication) changes as the patient's underlying state evolves.
- **Handling Non-stationarity:** Statistical techniques to account for the fact that behavioral data (GPS, activity) changes with time and context.

## 📊 Dataset & Experimental Setup
- **Data Source:** Passive sensor data and EMA surveys collected via the **Beiwe** platform.
- **Simulation and Pilot Data:** Demonstration of the framework on simulated N-of-1 datasets with known causal structures.

## 💡 Key Findings
- **Estimation of Individual Effects:** Shows that it is possible to identify causal effects within a single person's time series under specific identification conditions.
- **Non-stationarity Bias:** Failing to account for non-stationarity in digital phenotyping leads to significant bias in estimating treatment effects.

## 🩺 Clinical Relevance & Impact
Provides the statistical foundation for **Precision Psychiatry**, allowing clinicians to quantify the actual impact of a treatment on a specific patient's behavior and symptom trajectory.

## 🔬 Critical Review (Antagonic Perspective)
The framework assumes that all relevant confounders are captured within the time series data, which is rarely true in clinical practice (e.g., unrecorded life events). Furthermore, the computational cost of estimating these effects for every patient in a large clinic might be prohibitive.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Robins et al. (2000) on marginal structural models.
- **Descendant Discovery:** Real-time adaptive interventions based on N-of-1 causal estimates.
