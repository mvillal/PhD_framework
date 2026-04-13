---
title: "Learning to Defer (L2D)"
concept_type: "Human-AI Collaboration"
tags: ["L2D", "Uncertainty", "Automation Bias", "Sequential Decision-Making"]
sources: ["../../sources/doshi-velez/joshi_2021_learning_to_defer.md", "../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md"]
---

# Learning to Defer (L2D)

## 📋 Definition
**Learning to Defer (L2D)** is a framework for human-AI collaboration where an AI system learns to either make a prediction itself or "defer" the decision to another agent. In the 2026 clinical landscape, it is critical to distinguish between two primary forms of deferral:

1.  **Safety-Critical Deferral (Human-in-the-Loop):** The model identifies cases where its uncertainty is high or where the clinical cost of an error is unacceptable, yielding control to a human expert [[Joshi et al. (2021)](../../sources/doshi-velez/joshi_2021_learning_to_defer.md)]. This is a **Safety Mechanism**.
2.  **Information-Retrieval Deferral (Knowledge Grounding):** The model identifies a knowledge gap and "defers" to an external search tool or clinical database to retrieve factual information before responding ([[Med-Gemini]] / DeepMind). This is a **Retrieval Mechanism**.

## 🛠️ Key Technical Components
- **Sequential Deferral**: Unlike static deferral, Sequential L2D (Joshi et al., 2021) accounts for how uncertainty propagates over time in a patient's trajectory, deciding whether to defer now or in the future.
- **Bayesian Uncertainty Quantification**: Deferral is often triggered by high epistemic (model) or aleatoric (data) uncertainty.
- **Automation Bias Mitigation**: Research (Jacobs et al., 2021) shows that clinicians are prone to "automation bias," following incorrect AI recommendations even when explanations are provided. L2D systems aim to prevent this by explicitly stepping back when confidence is low.

## 🩺 Clinical Relevance
- **Safety in High-Risk Settings**: Essential for psychiatric interventions where the cost of a "false positive" or "false negative" intervention (e.g., suicide risk alerts) is high.
- **Cognitive Forcing**: L2D can be designed to require active clinician analysis (cognitive forcing) rather than passive acceptance of AI scores.

## 🔗 Related Concepts
- [Automation Bias](automation_bias.md)
- [Neural Stochastic Differential Equations (Neural SDEs)](neural_sdes.md)
