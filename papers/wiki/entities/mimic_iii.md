---
title: "MIMIC-III (Medical Information Mart for Intensive Care)"
type: "entity"
tags: ["Dataset", "ICU", "EHR", "Benchmarks"]
---

# MIMIC-III (Medical Information Mart for Intensive Care)

MIMIC-III is a large, freely available database comprising de-identified health-related data from patients who stayed in critical care units at the Beth Israel Deaconess Medical Center between 2001 and 2012.

## 📋 Role in the PhD Framework
MIMIC-III is the primary benchmark for testing **Sequential Decision-Making** and **Causal Inference** models before their application to psychiatric data.

## 🔬 Use Cases & Findings
- **Offline RL:** Gottesman et al. (2019/2021) used MIMIC-III to establish **Offline Reinforcement Learning** safety guidelines and analyze "Influential Transitions" in sepsis management.
   - *Source:* [Gottesman et al. (2019)](../../doshi-velez/gottesman_2019_clinical_rl_guidelines.md)
- **The Local Trap (2020):** Futoma et al. demonstrated that models trained on MIMIC-III often learn **Local Practice Patterns** (e.g., ordering frequencies) rather than clinical truth, risking poor generalizability.
   - *Source:* [Futoma et al. (2020)](../../doshi-velez/futoma_2020_myth_of_generalisability.md)
- **Discount Regularization (2024):** Used as a benchmark for **Overfitting in Low-Data Regimes** when training RL agents for sepsis care.
   - *Source:* [Jiang & Doshi-Velez (2024)](../../doshi-velez/jiang_2024_discount_regularization.md)

## 📊 Key Characteristics
- **Size:** ~53,000 patient admissions.
- **Data Types:** Demographics, vital signs, laboratory tests, medications, and caregiver notes.
- **Clinical Domains:** Sepsis, Hypotension, Acute Respiratory Failure.

## 🔗 Related Entities & Concepts
- **[eICU Collaborative Research Database](eicu.md)**
- **[Offline RL](../concepts/offline_rl.md)**
- **[Causal Inference](../concepts/causal_inference.md)**
