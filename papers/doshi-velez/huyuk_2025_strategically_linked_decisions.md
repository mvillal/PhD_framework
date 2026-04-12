# Strategically Linked Decisions in RL (Huyuk et al., 2025)

## Summary
Introduces "Strategic Link Scores" to explain the long-term dependencies of sequential clinical actions, helping clinicians understand how current decisions serve as prerequisites for future goals.

## Methodology
- **Strategic Link Scores:** A novel metric that quantifies the relationship between a current action and its necessity for achieving a distal treatment objective.
- **Sequential Decision-Making:** Focuses on the temporal structure of treatment, moving beyond immediate rewards to long-term strategy.

## Relevance
- **Psychiatry:** Highly relevant for psychiatric treatment where current interventions (e.g., stabilizing a patient's mood) are often prerequisites for long-term goals (e.g., starting intensive psychotherapy).
- **Explainable AI (XAI):** Provides a more clinically intuitive way to explain the reasoning behind an RL agent's recommendations.

## Key Findings
- **Understanding Dependencies:** Strategic Link Scores help clinicians see the "why" behind a sequence of actions, improving trust and alignment between the AI and the human expert.
- **Prerequisite Identification:** Identifies which actions are critical stepping stones for future success, even if they don't provide an immediate benefit.
