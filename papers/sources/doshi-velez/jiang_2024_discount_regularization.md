---
title: "Rethinking Discount Regularization: New Interpretations, Unintended Consequences, and Solutions for Regularization in RL"
authors: ["Nan Jiang", "Finale Doshi-Velez"]
year: 2024
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "JMLR / ICML"
doi: "10.48550/arXiv.2403.01353"
url: "http://jmlr.org/papers/v25/24-0087.html"
datasets: ["Clinical Simulators", "Medical Cancer Simulator"]
tags: ["Offline RL", "Discount Regularization", "Robustness", "Clinical Decision Support"]
---

# Rethinking Discount Regularization: New Interpretations, Unintended Consequences, and Solutions for Regularization in RL

## 📋 Executive Summary
This paper identifies a critical "unintended consequence" of standard discount regularization in offline RL—it regularizes *more* on state-action pairs where *more* data is available, the opposite of what is needed in clinical settings. The authors propose state-action-specific discount regularization to ensure that regularization is strongest in data-sparse regions, improving the safety of learned clinical policies.

## 🛠️ Core Methodology
- **Discount Regularization Analysis:** Mathematical proof showing that standard discount factors ($\gamma$) provide higher regularization (shorter planning horizons) in states with higher density in the behavior policy.
- **State-Action-Specific Discounting:** Introduction of a spatially-varying discount factor $\gamma(s, a)$ that inversely scales with the density of the training data.
- **Certainty Equivalence RL:** Applications of the framework within certainty-equivalence-based RL algorithms to handle uneven data coverage.

## 📊 Dataset & Experimental Setup
- **Data Source:** Validated with a medical cancer simulator and synthetic healthcare-inspired benchmarks.
- **Features:** State-action trajectories representing treatment histories and patient outcomes.
- **Evaluation Metrics:** Policy value (V), performance in low-data regimes, and robustness to state-space shifts.

## 💡 Key Findings
- **Standard Failure Mode:** Standard $\gamma$ regularization fails in clinical RL because it becomes overly "myopic" in well-sampled states while failing to regularize enough in high-risk, low-data states.
- **Improved Robustness:** The proposed $\gamma(s, a)$ framework consistently results in more robust policies that perform better in data-sparse regions of the clinical state space.
- **Interpretability:** Provides a direct link between data uncertainty and the effective planning horizon of the RL agent.

## 🩺 Clinical Relevance & Impact
Critically addresses the "data coverage" problem in clinical datasets like MIMIC-III or psychiatric EHRs. By ensuring stronger regularization in rare or atypical patient cases, this framework prevents the RL agent from making high-risk recommendations based on insufficient evidence.

## 🔬 Critical Review (Antagonic Perspective)
Implementing spatially-varying discount factors requires an accurate density estimation of the behavior policy, which is itself difficult in high-dimensional state spaces. If the density estimate is wrong, the regularization might be misapplied, potentially leading to suboptimal "safe" policies.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Petrik & Russell (2019) on robust MDPs.
- **Descendant Discovery:** Integrating state-action-specific regularization with continuous-time Neural SDEs (Lu et al., 2026).
