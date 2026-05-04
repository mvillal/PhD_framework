# Research Wiki Log

This is a chronological, append-only record of all research operations (ingests, queries, linting) performed within the PhD Framework.

## [2026-04-12] Initialize | LLM-Wiki Framework
- Created `papers/wiki/` structure.
- Initialized `index.md` and `log.md`.
- Compiled initial Concept: [Offline RL](concepts/offline_rl.md).
- Compiled initial Entity: [MIMIC-III](entities/mimic_iii.md).

## [2026-04-12] ingest | Complete | All 23 sources compiled into concepts, entities, and synthesis
- Finalized Concept pages: Neural SDEs, Ophthalmic Foundation Models, Objective Inflammation Grading, L2D, CBMs.
- Created Synthesis pages: State of Clinical RL, Shift in Uveitis AI.
- Updated Wiki Index with all entities and concepts.
## [2026-04-13] ingest | Digital Phenotyping & Systemic Expansion
- Expanded knowledge base with 10+ new sources from MIT, DeepMind, Stanford, Harvard, and UCL.
- Created Concept pages: [Digital Phenotyping](concepts/digital_phenotyping.md), [N-of-1 Modeling](concepts/n_of_1_modeling.md), [Agentic AI](concepts/agentic_ai.md), [Causal Falsification](concepts/causal_falsification.md), [Oculomics](concepts/oculomics.md), [Circuit Biotypes](concepts/circuit_biotypes.md).
- Created Entity pages: [Sontag Lab (MIT)](entities/sontag_lab_mit.md), [DeepMind Clinical AI](entities/deepmind_clinical_ai.md), [Onnela Lab](entities/onnela_lab.md), [Stanford PMHW](entities/stanford_pmhw.md).
- Authored Synthesis: [The Rise of Agentic and Foundation-Based Clinical AI (2024-2026)](synthesis/agentic_foundations_2026.md).

## [2026-04-27] Research Expansion | Behavioral Science & Engagement Validation
- Initialized new subagent: [Behavioral Scientist](../../.gemini/agents/behavioral-scientist.md).
- Created Concept pages: [Engagement Validation](concepts/engagement_validation.md), [Behavioral Theories](concepts/behavioral_theories.md).
- Updated Wiki Index to reflect the transition into behavioral digital phenotyping.

## [2026-04-27] Research Ingest | SDT-Informed RL & Engagement
- Conducted systematic review of SDT integration in Digital Phenotyping (2022-2026).
- Compiled Concept pages: [ENGAGE Framework](concepts/engage_framework.md) (2025), [Dyadic RL](concepts/dyadic_rl.md) (Li & Murphy, 2024).
- Updated Subagent definitions:
    - **Behavioral Scientist:** Integrated "Composite SDT Reward" modeling.
    - **Data Scientist:** Added "SDT-Informed Feature Engineering" and "Motivation Prediction."

## [2026-04-27] Adversarial Audit | SDT-Digital Proxies
- Formal Audit by `antagonic-researcher`: Identified **Construct Drift** and **Celerity Bias** in sensor-to-SDT mapping.
- Implemented Mandatory Guardrails in `behavioral-scientist` definition.
- Added Adversarial Critique to `concepts/behavioral_theories.md`.

## [2026-04-27] Research Ingest | Human-in-the-Loop Engagement
- Compiled Concept page: [Digital Navigator](concepts/digital_navigator.md).
- Researched HITL frameworks (mindLAMP, Torous Lab) for mitigating digital exhaustion.
- Integrated Digital Working Alliance (DWA) metrics into the Wiki.

## [2026-04-27] Technical Ingest | Engagement Telemetry Schemas
- Researched technical features for engagement tracking from **mindLAMP**, **RADAR-base**, and **Beiwe**.
- Created Entity page: [mHealth Engagement Schemas](entities/engagement_schemas.md) covering notification lifecycle (delivered, opened, dismissed).
- Updated Subagent definitions:
    - **Behavioral Scientist:** Added analysis of "Interaction Latency" and "Dismissal Rates."
    - **Data Scientist:** Added "Engagement Telemetry Processing" for high-resolution logs and sampling rates.

## [2026-04-27] Research | Backward Snowballing: DWAI Origins
- Traced **Digital Working Alliance Inventory (DWAI)** to foundational ancestors: Bordin (1979) and Horvath (1989).
- Compiled Seed Paper: [Henson & Torous (2019)](../sources/doshi-velez/henson_2019_dwai_validation.md).
- Documented psychometric properties and single-factor structure of the DWAI in [[engagement_validation]].
- Mapped the transition from human-human to human-computer alliance.

## [2026-05-02] Adversarial Audit | SDT-Digital Biomarker Integrity
- **Audit Focus:** Clinical validity of passive digital biomarkers as proxies for SDT.
- **Signal:** CRITICAL WARNING.
- **Findings:**
    - Identified **Construct Drift** in GPS (Autonomy) and Communication (Relatedness) metrics.
    - Flagged **Celerity Bias** in the "Composite SDT Reward" modeling used by subagents.
    - Warned against **The Local Trap** where digital engagement is optimized at the expense of real-world functional recovery.
- **Action:** Updated [[behavioral_theories]] and [[engagement_validation]] with formal critiques.

