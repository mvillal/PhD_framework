# Dyadic RL (Li & Murphy, 2024)

## 📄 Definition
**Dyadic Reinforcement Learning** is a Bayesian Hierarchical RL framework designed for mHealth interventions that involve two or more interlinked actors (e.g., patient and caregiver, or patient and Digital Navigator). It optimizes for **Relationship Cohesion** (Relatedness) rather than just individual health metrics.

## 🛠️ Core Methodology
- **Joint Reward Functions:** $R_{joint} = w_1(R_{patient}) + w_2(R_{caregiver}) + w_3(\text{Interaction Quality})$.
- **State Space:** Includes digital markers of social interaction, such as communication density, Bluetooth proximity, and shared activity goals.
- **Hierarchical Policy:** A top-level policy manages the "Relationship State," while lower-level contextual bandits handle individual-level prompts.

## 🔬 SDT Integration
- **Relatedness:** The model explicitly rewards actions that increase the frequency and quality of interactions between the dyad.
- **Competence:** The "Caregiver" policy is trained to provide "Autonomy-Supportive" feedback that builds the patient's competence rather than fostering dependency.

## 🩺 Clinical Applications
- **Adolescent Bipolar Monitoring:** Helping parents and teens navigate mood swings using shared digital markers [[Huang et al. (2025)](../../sources/onnela/huang_2025_adolescent_bipolar_monitoring.md)].
- **Elderly Care:** Supporting aging-in-place by optimizing the "Caregiver Burden" vs. "Patient Safety" trade-off.

## 🔗 Related Concepts
- [[behavioral_theories]]
- [[offline_rl]]
- [[digital_phenotyping]]
