---
title: "Large language models for the mental health community: framework for translating code to care"
authors: ["Malgaroli et al.", "Katharina Schultebraucks (Corresponding)"]
year: 2025
lab: "Computational Psychiatry Program, NYU Grossman School of Medicine"
venue: "The Lancet Digital Health"
doi: "10.1016/S2589-7500(25)XXXXX"
code: "N/A"
datasets: ["NYU-Computational-Psychiatry-Repository"]
tags: ["LLMs", "Translational Psychiatry", "Digital Phenotyping", "Human-Machine Collaboration", "Diagnostic Markers"]
---

# LLMs for Mental Health: Code to Care Framework

## 📋 Executive Summary
Malgaroli, Schultebraucks, et al. (2025) propose a comprehensive "sociocultural–technical framework" for the clinical translation of Large Language Models (LLMs) in psychiatry. While LLMs show promise in analyzing clinical narratives and digital phenotyping data, their deployment is often hindered by the "Translation Gap." This paper provides five key pillars—ranging from global clinical repositories to cultural integration—to ensure LLMs move from research code to effective clinical care.

## 🛠️ Core Methodology
- **Sociocultural–Technical Approach:** Emphasizes that LLMs are not just software but part of a complex social system involving patients, clinicians, and diverse cultural contexts.
- **Pillar 1: Global Clinical Repository:** Advocates for large-scale, diverse datasets to prevent "Digital Exclusion" and bias.
- **Pillar 2: Objective Diagnostic Markers:** Uses LLMs to analyze audio/video narratives to identify stress and PTSD biomarkers that transcend DSM-5 categories.
- **Pillar 3: Human-Machine Collaboration:** Focuses on LLMs as tools that augment clinician decision-making rather than replacing it.

## 📊 Dataset & Experimental Setup
- **Evaluation:** Built upon longitudinal trials at NYU (e.g., PREDICT study) tracking trauma survivors and healthcare worker burnout.
- **Metrics:** Focused on **Long-term Forecasting Accuracy** (up to 1 year) and clinician adoption metrics.

## 💡 Key Findings
- **PTSD Forecasting:** Narrative-based LLM markers could identify PTSD risk up to **one year** after a traumatic event with significantly higher precision than baseline clinical interviews.
- **Burnout Detection:** Digital phenotyping identified early signs of clinician burnout through shifts in language and mobility patterns before self-reporting occurred.
- **Barriers to Entry:** Identified "Trust" and "Interpretability" as the primary bottlenecks for MD adoption of LLM recommendations.

## 🩺 Clinical Relevance & Impact
The framework shifts psychiatry from "episodic diagnosis" to **Continuous, Objective Monitoring**. It introduces roles like **"Digital Navigators"** to bridge the gap between patients and AI tools, ensuring that precision psychiatry is accessible and equitable.

## 🔬 Critical Review (Antagonic Perspective)
The reliance on narrative data (audio/video) raises extreme **Privacy and Surveillance** concerns. If patients feel they are being "graded" by an AI during an emergency department visit, they may self-censor, leading to lower-quality data and biased diagnostic outcomes.

## 🔗 Discovery & Next Steps
- **Implementation:** Explore using LLMs to extract "Causal Representations" from clinical notes, linking back to Sontag's work on Causal Falsification.
- **Synthesis Link:** Directly supports [Agentic Foundations & Autoresearcher Frameworks](synthesis/agentic_foundations_2026.md).
