---
title: "Informative Missingness (Missing Not At Random - MNAR)"
tags: ["Causal Inference", "Digital Phenotyping", "Missing Data", "Psychiatry", "SSMimpute"]
---

# Informative Missingness

## 📖 Definition
**Informative Missingness** occurs when the reason data is missing is related to the value of the missing data itself or the patient's underlying state. In clinical psychiatry and digital phenotyping, this is often classified as **Missing Not At Random (MNAR)**. For example, a patient with depression may stop using their smartphone or answering EMA surveys because their symptoms (lethargy, social withdrawal) prevent them from engaging, making the "absence of data" a significant clinical signal.

## 🧠 Core Mechanisms
1.  **State-Dependent Engagement:** The probability of a missing data point is a function of the latent psychiatric state (e.g., mania vs. depression).
2.  **The "Silent Smoke Detector":** In suicide risk monitoring, the most critical period (acute crisis) is often characterized by a complete cessation of device interaction, rendering standard "anomaly detection" blind if it does not explicitly model the cessation itself as an informative event (Nock et al., 2026).
3.  **Clinician Intent:** In EHR data, the absence of a test or lab result is often informative (Gottesman et al., 2019). Clinicians only order tests when they suspect a specific condition, meaning the "missingness" of a lab value often implies the clinician believed the patient was stable in that regard.

## 🛠️ Statistical Mitigation
- **SSMimpute:** A State-Space Model imputation approach (Cai et al., 2026) that treats missingness as a latent process, allowing for the identification of causal effects even in non-stationary time series with unit roots.
- **Joint Modeling:** Simultaneously modeling the longitudinal outcome (e.g., mood) and the time-to-event/missingness process.
- **Neural SDEs with Compact State Spaces:** Lu et al. (2026) utilize Neural SDEs to provide continuous-time risk trajectories where the diffusion term (stochasticity) naturally expands during periods of missing sensor data, providing a formal measure of uncertainty in the absence of digital "heartbeats."
- **Multiple Imputation with Clinical Priors:** Using domain knowledge to inform the distribution of missing values rather than assuming they are missing at random (MAR).

## 🏥 Clinical Implications
Failure to account for informative missingness leads to **Survival Bias** and **Celerity Bias**, where models only learn from "successful" or "engaged" patients, potentially missing the most critical risk signals in the most vulnerable populations.

## 🔗 Related Concepts
- [[digital_phenotyping]]
- [[causal_falsification]]
- [[n_of_1_modeling]]

## 📚 Sources
- Cai et al. (2026): *Causal estimands and identification of time-varying effects in N-of-1 mobile data.*
- Nock et al. (2026): *Predicting Next-Week Suicide Risk via Smartphone.*
- Gottesman et al. (2019): *Guidelines for Reinforcement Learning in Healthcare.*
