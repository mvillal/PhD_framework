# Research Wiki Log

This is a chronological, append-only record of all research operations (ingests, queries, linting) performed within the PhD Framework.

## [2026-05-11] Statistical Review | Clinical DLP Framework & SAP
- Refined the experimental design for the **Clinical DLP (Data Loss Prevention) Framework**.
- Authored **Statistical Analysis Plan (SAP)** focusing on **MNAR Causal Assumptions**, **Bayesian Credible Intervals**, and **Causal Transportability**.
- Added path $Y_t^* \rightarrow M_t$ to the missingness DAG to account for behavioral shifts in paranoid/depressive episodes.
- Defined **Synthetic Reliability Score (SRS)** based on Bayesian posterior predictive checks for synthetic cohort validation.
- Updated Wiki Index with the new SAP synthesis page.

## [2026-05-11] Project Initiation | Synthetic Cohorts & Data Loss Prevention
- Initialized new research project: **Clinical Framework for Synthetic Cohorts and Data Loss Prevention in Digital Phenotyping**.
- Focus: Addressing **Informative Missingness** (MNAR) in longitudinal smartphone data and creating privacy-preserving **Synthetic Clinical Cohorts**.
- Ingested core methodology from Cai et al. (2026) regarding **N-of-1 Causal Estimands** and SSMimpute.
- Cross-referenced with Nock et al. (2026) regarding **Digital Smoke Detectors** and the risk of "silent" devices during high-risk periods.
- Created Concept pages: [[informative_missingness]], [[data_loss_prevention_clinical]], and [[synthetic_clinical_cohorts]].
- Updated Wiki Index and linked new concepts to [[onnela_lab]] and [[torous_lab_digital_psychiatry]].

## [2026-05-10] ingest | Source Backlog Clearance | 25 Papers Refined
- Successfully executed a multi-batch refinement phase, populating all "TBD" source files in the repository.
- **Clinical RL & Sequential Planning:** Populated Rathnam (2024), Zhang (2021), Trella (2024), Huyuk (2025), and Gottesman (2019).
- **Oculomics & Uveitis:** Populated Zhou (2023), Mortimer (2025), Agrawal (2025), Mohammadi (2026), Mahajan (2023), Haggag (2021), and Umer (2025).
- **Psychiatric Digital Phenotyping:** Populated Nock (2026), Schultebraucks (2025), Hang (2025), and Cai (2026).
- **Human-AI Alignment & Bias:** Populated Fischer (2025), Jacobs (2021/2023), Joshi (2021), Havasi (2022), and Parbhoo (2022).
- **Causal Inference:** Populated Demirel/Hussain/Sontag (2025) and Mozannar (2025).
- Fetched 15+ implementation patterns using **Context7** across PyTorch, MONAI, YOLOv11, Fairlearn, and DoWhy.
- Updated Wiki synthesis on **The Rise of Agentic Foundations**, **State of Clinical RL**, and **Precision Digital Phenotyping**.

## [2026-05-10] ingest | Agentic Foundations & Autoresearcher Trends
- Researched latest trends (2025-2026) in AI-assisted medical research.
- Fetched implementation patterns for LangGraph and AutoGen using Context7.
- Authored Synthesis: [Agentic Foundations & Autoresearcher Frameworks in Clinical AI (2024-2026)](synthesis/agentic_foundations_2026.md).
- Updated Wiki Log with orchestration patterns (Human-in-the-loop, Self-RAG).

## [2026-05-10] ingest | Digital Phenotyping & Wiki-Refiner Prototype
- Implemented **Wiki-Refiner** prototype in `.gemini/agents/refiner_scripts/wiki_refiner.py` using LangGraph patterns.
- Researched 2026 trends in **Digital Phenotyping** and **Causal Inference** for psychiatry.
- Fetched longitudinal modeling patterns (TimeGPT, CausalML) using Context7.
- Authored Synthesis: [Precision Digital Phenotyping & Causal Inference in Psychiatry (2025-2026)](synthesis/digital_phenotyping_causal_2026.md).
- Integrated concepts of **Uplift Modeling** and **Causal Transportability** into the framework.

## [2026-05-02] Adversarial Audit | SDT-Digital Biomarker Integrity
- **Audit Focus:** Clinical validity of passive digital biomarkers as proxies for SDT.
- **Signal:** CRITICAL WARNING.
- **Findings:**
    - Identified **Construct Drift** in GPS (Autonomy) and Communication (Relatedness) metrics.
    - Flagged **Celerity Bias** in the "Composite SDT Reward" modeling used by subagents.
    - Warned against **The Local Trap** where digital engagement is optimized at the expense of real-world functional recovery.
- **Action:** Updated [[behavioral_theories]] and [[engagement_validation]] with formal critiques.

## [2026-04-29] synthesis | Autoresearcher Frameworks 2026
- Analyzed and ingested latest 2024-2026 trends in autonomous scientific discovery.
- Identified PaperQA2, STORM, AI Scientist v2, and Sc(AI)Mitra as core integration targets.
- Defined roadmap for "Agentic Science" in psychiatry research.

## [2026-04-29] ingest | Andrej Karpathy (2024-2026) Paradigms
- Compiled Concept: [LLM OS & Agentic Engineering](concepts/llm_os_agentic_engineering.md).
- Integrated RLVR (Verifiable Rewards) and "Thinking" model logic into the research workflow.
- Mapped LLM OS components (Kernel, RAM, File System) to the PhD Framework architecture.

## [2026-04-27] Research Expansion | Behavioral Science & Engagement Validation
- Initialized new subagent: [Behavioral Scientist](../../.gemini/agents/behavioral-scientist.md).
- Created Concept pages: [Engagement Validation](concepts/engagement_validation.md), [Behavioral Theories](concepts/behavioral_theories.md).
- Updated Wiki Index to reflect the transition into behavioral digital phenotyping.

## [2026-04-13] ingest | Digital Phenotyping & Systemic Expansion
- Expanded knowledge base with 10+ new sources from MIT, DeepMind, Stanford, Harvard, and UCL.
- Created Concept pages: [Digital Phenotyping](concepts/digital_phenotyping.md), [N-of-1 Modeling](concepts/n_of_1_modeling.md), [Agentic AI](concepts/agentic_ai.md), [Causal Falsification](concepts/causal_falsification.md), [Oculomics](concepts/oculomics.md), [Circuit Biotypes](concepts/circuit_biotypes.md).
- Created Entity pages: [Sontag Lab (MIT)](entities/sontag_lab_mit.md), [DeepMind Clinical AI](entities/deepmind_clinical_ai.md), [Onnela Lab](entities/onnela_lab.md), [Stanford PMHW](entities/stanford_pmhw.md).
- Authored Synthesis: [The Rise of Agentic and Foundation-Based Clinical AI (2024-2026)](synthesis/agentic_foundations_2026.md).

## [2026-04-12] ingest | Complete | All 23 sources compiled into concepts, entities, and synthesis
- Finalized Concept pages: Neural SDEs, Ophthalmic Foundation Models, Objective Inflammation Grading, L2D, CBMs.
- Created Synthesis pages: State of Clinical RL, Shift in Uveitis AI.
- Updated Wiki Index with all entities and concepts.

## [2026-04-12] Initialize | LLM-Wiki Framework
- Created `papers/wiki/` structure.
- Initialized `index.md` and `log.md`.
- Compiled initial Concept: [Offline RL](concepts/offline_rl.md).
- Compiled initial Entity: [MIMIC-III](entities/mimic_iii.md).
