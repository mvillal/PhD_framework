# Behavioral Theories in Digital Health

## 📄 Definition
Behavioral theories provide the framework for understanding *why* and *how* individuals interact with digital health interventions. In the context of ML in Psychiatry, these theories guide feature engineering and the interpretation of [[digital_phenotyping]] data.

## 🛠️ Core Frameworks
- **Self-Determination Theory (SDT):** Focuses on autonomy, competence, and relatedness. Key for understanding intrinsic motivation in long-term app engagement.
- **Fogg Behavior Model:** Asserts that behavior ($B$) happens when Motivation ($M$), Ability ($A$), and a Prompt ($P$) converge: $B = MAP$.
- **Health Belief Model (HBM):** Predicts health behaviors by focusing on perceived threat and net benefits.
- **Transtheoretical Model (Stages of Change):** Categorizes users into stages (Pre-contemplation to Maintenance), essential for personalizing RL-based intervention timing.

## 🔬 Computational Application
- **Feature Engineering:** Mapping "Frequency of Use" to *Habit Formation* constructs.
- **Reward Function Design:** Using SDT to design [[offline_rl]] reward functions that prioritize patient autonomy over simple compliance.
- **Latent State Modeling:** Using theories of change to define the hidden states in HMMs or RNNs.

## ⚠️ Adversarial Critique: The SDT Proxy Problem
While theoretically sound, the digital implementation of SDT constructs faces several "High-Fragility" assumptions:
- **Construct Drift (Autonomy):** GPS "regularity" is often a proxy for **socioeconomic constraint** (e.g., rigid work shifts) or surveillance rather than self-determined routine.
- **The Valence Gap (Relatedness):** High communication frequency (call/text logs) is valence-blind and may represent social anxiety or conflict rather than healthy cohesion.
- **The Local Trap:** Optimizing for "Digital Relatedness" can lead to **Digital Dependency**, where a user engages perfectly with an app while their real-world social life deteriorates.

## 🩺 Clinical Relevance
Understanding the behavioral "Mechanism of Action" is critical for FDA/regulatory approval of Digital Therapeutics (DTx).

## 🔬 Critical Review (Adversarial Perspective)
- **Construct Drift:** High risk that digital markers measure environmental constraints (socioeconomic status, shift work) rather than psychological states (e.g., GPS regularity $\neq$ Autonomy).
- **The Valence Gap:** Communication density (call/text logs) is valence-blind; high frequency can indicate conflict or anxiety rather than healthy "Relatedness."
- **Celerity Bias:** Premature implementation of SDT-informed RL before validating the causal link between sensor proxies and internal psychological states.
- **The Local Trap:** Optimizing for "Digital Engagement" may foster app dependency while real-world functional recovery remains stagnant.

## 🔗 Related Concepts
- [[engagement_validation]]
- [[digital_phenotyping]]
- [[learning_to_defer]]
