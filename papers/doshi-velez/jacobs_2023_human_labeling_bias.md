---
title: "Out with AI, in with the Psychiatrist: The Impact of Source Attribution on Trust"
authors: ["Maia Jacobs", "Finale Doshi-Velez"]
year: 2023
lab: "Data to Actionable Knowledge (DtAK), Harvard SEAS"
venue: "CHI Conference on Human Factors in Computing Systems"
doi: "https://doi.org/10.1145/3544548.3581172"
url: "https://doi.org/10.1145/3544548.3581172"
code: "N/A"
datasets: ["N/A"]
tags: ["Human-Labeling Bias", "Algorithm Aversion", "Trust", "Psychiatry"]
---

# Out with AI, in with the Psychiatrist: The Impact of Source Attribution on Trust

## 📋 Executive Summary
This study quantifies "human-labeling bias" in psychiatry. It demonstrates that clinicians are significantly more likely to accept a treatment recommendation if they believe it came from a human peer (e.g., a "Senior Psychiatrist") rather than an AI, even when the underlying recommendations are identical.

## 🛠️ Core Methodology
- **Randomized Attribution Study:** Clinicians were presented with the same set of recommendations, but the source was randomly labeled as either "AI System" or "Senior Consultant."
- **Algorithm Aversion Measurement:** Assessing the drop-off in agreement rate when the AI label was applied.
- **Qualitative Feedback Analysis:** Categorizing the reasons clinicians gave for rejecting AI vs. human advice.

## 📊 Dataset & Experimental Setup
- **Data Source:** Randomized controlled experiment with practicing mental health professionals.
- **Sample Size:** (n = X) - *Note: Based on similar DtAK studies, typically 100-200 clinicians.*
- **Features:** Recommendation accuracy, source label (AI vs. Human), and clinician experience level.
- **Evaluation Metrics:** Agreement Rate, Trust Scores, and Qualitative Sentiment.

## 💡 Key Findings
- **Human-Labeling Bias:** A statistically significant preference for human-sourced advice, regardless of its objective quality.
- **Algorithm Aversion:** Clinicians were more "forgiving" of human errors but used AI errors as evidence to permanently distrust the system.
- **Trust Dynamics:** Attribution alone (the "label") was a stronger predictor of acceptance than the actual content of the recommendation.

## 🩺 Clinical Relevance & Impact
Suggests that the primary hurdle for AI in psychiatry is not just accuracy, but *integration and presentation*. To be successful, AI might need to be framed as "Collaborative Intelligence" or "Augmented Peer Review" rather than a replacement for human judgment.

## 🔬 Critical Review (Antagonic Perspective)
The study might reflect a generational divide; younger, more tech-native clinicians might show less algorithm aversion. Additionally, "human-labeling bias" might be a rational response to the lack of legal/ethical accountability for AI systems.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** [Jacobs et al. (2021)](jacobs_2021_antidepressant_bias.md) for the original automation bias findings.
- **Descendant Discovery:** [Fischer et al. (2025)](fischer_2025_clinician_expectations.md) for how to align AI with these human expectations.
