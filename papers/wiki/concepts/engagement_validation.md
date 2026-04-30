# Engagement Validation

## 📄 Definition
**Engagement Validation** is the process of ensuring that digital interactions (app opens, clicks, sensor data) are meaningful indicators of therapeutic progress or clinical state. It seeks to distinguish between "Surface Engagement" (mechanical use) and "Effective Engagement" (use that leads to clinical benefit).

## 🛠️ Key Metrics
- **Effective Engagement:** The minimum level of engagement required to achieve a clinical outcome.
- **Micro-engagement:** High-frequency, low-effort interactions (e.g., checking a notification).
- **Engagement Breadth:** The variety of app features used (correlates with cognitive load and interest).
- **The "Cliff" Effect:** Sudden drops in engagement that may signal relapse, recovery, or technical fatigue ([[informational_missingness]]).

## 🔬 Validation Methodologies
- **Digital Working Alliance Inventory (DWAI):** A 6-item scale adapted from the traditional Bordin (1979) model. It measures **Bond, Task, and Goal** alignment between the patient and the digital tool [[Henson & Torous (2019)](../../sources/doshi-velez/henson_2019_dwai_validation.md)].
- **Psychometric Convergence:** Correlating digital usage patterns with validated scales like the *User Engagement Scale (UES)* or PHQ-9.
- **Lineage:**
    - **Progenitor:** Bordin (1979) - Tripartite Alliance Model.
    - **Ancestor:** Working Alliance Inventory (WAI) - Horvath & Greenberg (1989).
    - **Digital Branch:** mARM (Berry et al., 2018) and DWAI (Torous, 2019).
- **N-of-1 Cross-Validation:** Using individual-level causal models to see if a change in engagement precedes a change in symptom severity.
- **Ecological Validity:** Ensuring that digital behavior reflects real-world functioning (e.g., GPS mobility correlating with social engagement).

## 🩺 Clinical Challenges
- **The Engagement-Outcome Paradox:** In some cases, *decreased* engagement may signal recovery (the patient no longer needs the app).
- **Digital Exhaustion:** Over-monitoring leading to decreased compliance and skewed data.
- **Celerity Bias:** A premature rush to optimize "Engagement" using RL reward functions before the digital markers are validated against ground-truth functional outcomes.

## 🔗 Related Concepts
- [[digital_phenotyping]]
- [[behavioral_theories]]
- [[n_of_1_modeling]]
