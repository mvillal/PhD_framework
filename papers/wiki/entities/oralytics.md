---
title: "Oralytics Clinical Trial"
type: "Entity"
category: "Clinical Trial / mHealth"
tags: ["Mobile Health", "Online RL", "Contextual Bandits", "Algorithm Fidelity"]
---

# Oralytics Clinical Trial

## 📋 Overview
Oralytics is a mobile oral health intervention clinical trial utilizing online Reinforcement Learning (RL) to provide personalized push notifications to participants, aimed at improving oral hygiene behaviors.

## 🔬 Role in Research
- **Online RL Safety:** Used as the primary case study for developing "Algorithm Fidelity" frameworks, which monitor the safety and validity of autonomous agents in real-time [[Trella & Doshi-Velez (2024)](../../sources/doshi-velez/trella_2024_online_rl_fidelity.md)].
- **Contextual Bandits:** Employs Thompson-Sampling-based contextual bandits to determine the optimal timing and content of interventions for each participant.

## 📊 High-Signal Metrics & Characteristics
- **Architecture:** Personalization via Thompson Sampling contextual bandits.
- **Monitoring Framework:** Introduced **Algorithm Fidelity**, a two-component framework (Safety and Validity) to ensure the agent adheres to clinical and scientific constraints during autonomous deployment [[Trella & Doshi-Velez (2024)](../../sources/doshi-velez/trella_2024_online_rl_fidelity.md)].

## 🔗 Related Sources
- [Trella & Doshi-Velez (2024): Algorithm Fidelity in Online RL](../../sources/doshi-velez/trella_2024_online_rl_fidelity.md)
