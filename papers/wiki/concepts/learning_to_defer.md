---
title: "Learning to Defer (L2D)"
concept_type: "Human-AI Collaboration"
tags: ["L2D", "Uncertainty", "Automation Bias", "Sequential Decision-Making"]
sources: ["../../sources/doshi-velez/joshi_2021_learning_to_defer.md", "../../sources/doshi-velez/jacobs_2021_antidepressant_bias.md"]
---

# Learning to Defer (L2D)

## 📋 Definition
Learning to Defer (L2D) is a framework where an AI system is trained not only to perform a task but also to identify when it should "defer" the decision to a human expert. In clinical settings, this ensures that the AI operates within its "competence zone" and hands over complex cases to clinicians.

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
