# Rethinking Discount Regularization (Jiang et al., 2024)

## Summary
This paper introduces state-action-specific discounting in Reinforcement Learning (RL) as a form of regularization to prevent overfitting, particularly in low-data regimes common in clinical settings.

## Methodology
- **State-Action-Specific Discounting:** Unlike traditional RL which uses a global discount factor ($\gamma$), this approach adapts the discount factor based on specific state-action pairs.
- **Overfitting Prevention:** Aims to mitigate the "deadly triad" and other overfitting issues in offline RL by regularizing the value function.

## Relevance & Data
- **Sepsis (MIMIC-III):** Demonstrated on the MIMIC-III dataset for sepsis treatment, preventing agents from ignoring long-term survival in favor of short-term physiological fixes.
- **mHealth:** Applicable to mobile health interventions where data for specific individuals may be sparse.

## Key Findings
- **Improved Policy Robustness:** State-action-specific discounting leads to more robust policies that generalize better to unseen clinical scenarios.
- **Long-Term Survival Focus:** By carefully regularizing the discount factor, the agent is incentivized to prioritize long-term outcomes (e.g., patient survival) over immediate, potentially misleading rewards.
