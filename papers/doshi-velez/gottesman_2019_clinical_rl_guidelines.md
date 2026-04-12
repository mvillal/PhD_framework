# Guidelines for Clinical Reinforcement Learning (Gottesman et al., 2019)

## Summary
A comprehensive study outlining best practices and potential pitfalls for applying Offline Reinforcement Learning (RL) in clinical environments, specifically focusing on critical care.

## Datasets
- **MIMIC-III:** Medical Information Mart for Intensive Care, a large de-identified database of ICU patients.
- **eICU:** The eICU Collaborative Research Database, a multicenter dataset containing detailed clinical data from over 200 hospitals across the USA.

## Methodology
- **Offline Reinforcement Learning:** Training RL agents on historical data where interactive exploration is not possible or ethical.
- **FQE (Fitted Q-Evaluation):** Evaluating policy performance using influence functions to identify which historical transitions are most important for the policy's success.

## Models
- **BCQ (Batch-Constrained Q-learning):** A technique to prevent the agent from taking actions that are outside the range of historical clinician behavior.
- **DQN (Deep Q-Network):** A standard deep RL algorithm applied in an offline context.

## Metrics
- **V (Policy Value):** Estimated total reward of a policy.
- **WIS (Weighted Importance Sampling):** A robust estimator for off-policy evaluation that handles high-variance trajectories.
- **ESS (Effective Sample Size):** A measure of the statistical reliability of the policy evaluation.

## Clinical Findings
- **Sepsis Vasopressor Timing:** Highlights the importance of correct timing for vasopressor administration in sepsis patients.
- **Influential Transitions for Trust:** Identified specific patient transitions in the data that are most critical for building clinician trust in the AI's recommendations.
