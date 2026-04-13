# The Rise of Agentic and Foundation-Based Clinical AI (2024-2026)

## 📄 Overview
The period between 2024 and 2026 marks a fundamental paradigm shift in clinical Machine Learning. We have moved from **Static Predictive Models** (e.g., mortality prediction) to **Agentic and Foundation-Based Systems** that can reason, gather information, and generalize across clinical domains.

## 🚀 Key Transitions

### 1. From "Static" to "Agentic" ([[amie]] & [[med_gemini]])
Traditional clinical AI provided a single output for a single input. Agentic systems like [[AMIE]] (DeepMind, 2024) introduce multi-turn dialogue, allowing the AI to "act" as a diagnostic partner. [[Med-Gemini]] (DeepMind, 2024) further enhances this by integrating **Uncertainty-Guided Search**, enabling the model to fact-check its own reasoning against the latest medical literature.

### 2. From "Black-Box" to "Causal Auditing" ([[sontag_lab_mit]])
The "credibility crisis" of clinical RL (learning biased policies from EHRs) has been addressed by [[Causal Falsification]] (Mozannar & Sontag, 2025). Instead of trusting an opaque policy, researchers can now use small-scale RCT data to audit and reject models that have learned "shortcuts" or administrative biases.

### 3. From "Symptom-Based" to "Circuit-Based" ([[stanford_pmhw]])
Psychiatry is undergoing a biological revolution led by the [[Circuit Biotypes]] model (Williams, 2024). By identifying six primary brain circuits that drive mental health symptoms, ML is now capable of **Precision Treatment Matching**, predicting which patients will respond to specific pharmacotherapies or TMS based on their fMRI-derived biotype.

### 4. From "Niche AI" to "Global Oculomics" ([[ucl_moorfields]])
Foundation models like [[Ophthalmic Foundation Models]] (2023) have evolved into **RETFound-Green** (2025). This move toward "Green AI" and on-device smartphone optimization ensures that the benefits of [[Oculomics]] (detecting systemic disease via the eye) are accessible in low-resource settings, bridging the global health equity gap.

## 🔬 Synthesis Table: Core Breakthroughs

| Year | Technology | Lab | Primary Impact |
| :--- | :--- | :--- | :--- |
| 2024 | **Circuit Biotypes** | Stanford | Biological taxonomy for precision psychiatry. |
| 2024 | **AMIE** | DeepMind | Human-level diagnostic reasoning in simulated consultations. |
| 2024 | **Med-Gemini** | DeepMind | Natively multimodal AI with autonomous web-search grounding. |
| 2025 | **Causal Falsification** | MIT | Statistical auditing to reject biased clinical policies. |
| 2025 | **RETFound-Green** | UCL | Smartphone-optimized oculomics for global health. |
| 2026 | **N-of-1 SDEs** | Harvard | Continuous-time causal monitoring for personalized mental health. |

## ⚠️ Critical Limitations & Paradoxes

### 1. The Generalizability Paradox
While [[Med-Gemini]] and other foundation models claim to "generalize across clinical domains," they must still contend with the **Myth of Generalizability** [[Futoma et al. (2020)](../../sources/doshi-velez/futoma_2020_myth_of_generalisability.md)]. Modern scale may reduce, but does not eliminate, the "Local Trap"—where models learn hospital-specific administrative shortcuts. Grounding via **Uncertainty-Guided Search** is a primary mitigation strategy, but its effectiveness in low-resource settings remains unproven.

### 2. The Agency vs. Fidelity Gap
Agentic systems like [[AMIE]] introduce a "reasoning" layer that is often decoupled from the underlying **Algorithm Fidelity** [[Trella et al. (2024)](../../sources/doshi-velez/trella_2024_online_rl_fidelity.md)]. If an agent's multi-step dialogue diverges from safe clinical policies (the "Deadly Triad" risk), the resulting diagnostic advice may be articulate but fundamentally unsafe.

### 3. The Data Bottleneck in Causal Auditing
[[Causal Falsification]] is the current gold standard for policy safety, but it faces a severe **Data Bottleneck**. It requires high-fidelity, often RCT-derived data to audit observational policies. In rare psychiatric conditions or data-sparse environments, the "Ground Truth" needed to falsify a biased model may simply not exist.

## 🩺 Conclusion
The 2026 clinical AI landscape is characterized by **Grounding, Agency, and Biological Mechanism**. The "House of Cards" era of unverified observational models is being replaced by a "Foundation of Trust" built on causal auditing and multimodal reasoning agents.
