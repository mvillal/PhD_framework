# Research Lifecycle & Documentation Guide

This guide outlines the systematic process for discovering, tracking, and documenting new research within the PhD Framework.

## 1. Discovery Workflow (Snowballing)
We use a dual-direction "snowballing" technique to map the research landscape:

### Backward Snowballing (Ancestor Discovery)
- **Process:** Review the references section of a "Seed Paper" to find foundational works.
- **Criteria:** Prioritize papers cited for "Methodology" or "Clinical Grounding."
- **Action:** If a specific lab or author appears multiple times, flag them for **Lab Discovery**.

### Forward Snowballing (Descendant Discovery)
- **Process:** Use Google Scholar or Semantic Scholar to find newer papers that cite our current knowledge base.
- **Goal:** Track how a theory (e.g., "Automation Bias in Psychiatry") has evolved or been challenged.

## 2. Lab & Author Auto-Discovery
When a new high-impact laboratory is identified through references:
1.  **Initialize Lab Directory:** Create `papers/[lab_name]/`.
2.  **Create `LAB_KNOWLEDGE_BASE.md`:** Research the lab's primary mission statement and core research pillars.
3.  **Cross-Reference Tracking:** Add the lab to the central `papers/RESEARCH_INDEX.md`.

## 3. Paper Documentation Standards
Every paper must be documented in a standalone Markdown file using the naming convention: `[author]_[year]_[short_title].md`.

### 🛠️ Information Extraction
Agents MUST use the **PDF Parsing Skill** (`markitdown` / `marker-pdf`) to process the full text of PDFs before summarization. This ensures that tables, mathematical formulations, and appendix details are not lost in the synthesis.

### 📝 Markdown Template
All paper summaries must follow this structure:

```markdown
---
title: "Full Paper Title"
authors: ["Author 1", "Author 2"]
year: YYYY
lab: "Laboratory Name / Affiliation"
venue: "Conference/Journal Name"
doi: "DOI Link"
url: "Direct URL to Paper"
code: "Repository Link (if available)"
datasets: ["Dataset 1", "Dataset 2"]
tags: ["Tag 1", "Tag 2"]
---

# [Full Paper Title]

## 📋 Executive Summary
A 2-3 sentence overview of the paper's contribution and its significance for the PhD project.

## 🛠️ Core Methodology
Detailed breakdown of the mathematical framework, algorithms (e.g., SCM, Offline RL, CNN), and optimization techniques used.

## 📊 Dataset & Experimental Setup
- **Data Source:** (e.g., MIMIC-III, STAR*D, private cohort)
- **Sample Size:** (n = X patients/images)
- **Features:** Key variables and preprocessing steps.
- **Evaluation Metrics:** Mandatory extraction of **High-Signal Metrics** (AUROC, AUPRC, p-values, Bayes Factors, WIS, ESS, or NNT).

## 💡 Key Findings
- **Technical Results:** Quantitative performance metrics (e.g., "AUROC: 0.89 [95% CI: 0.85-0.93]").
- **Statistical Significance:** p-values, Bayes Factors, or posterior distribution statistics.
- **RL/Causal Metrics:** Expected Reward (V), effective sample sizes (ESS).
- **Ablation Studies:** What components were most critical?

## 🩺 Clinical Relevance & Impact
Specific applications to psychiatry or ophthalmology (e.g., "predicts flare-up 3 months early"). How does this bridge the gap to bedside care?

## 🔬 Critical Review (Antagonic Perspective)
Potential biases, limitations in generalizability, or "Local Trap" risks.
- **Scientific Contradictions (ContraCrow):** Explicitly list findings that contradict other papers in the Wiki (e.g., "Contradicts Doshi-Velez 2021 regarding discount regularization effects").

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** 2-3 key references to explore next.
- **Descendant Discovery:** Search patterns for forward snowballing.
```

## 4. Tracking & Synchronization
- **`papers/RESEARCH_INDEX.md`**: The source of truth for what has been read. It must be updated immediately after a new paper is added.
- **`KNOWLEDGE_BASE.md`**: High-level synthesis across labs. Update this when a new "Domain Layer" (e.g., Neural SDEs) becomes significant.
- **`doc-sync-skill`**: Use this skill to ensure all indices and READMEs reflect the new additions.

## 5. Agent-Based Research Workflows

To ensure scientific rigor and autonomous orchestration, the framework employs formalized agent interaction patterns.

### 🔄 The ReAct Pattern (Reason + Act)
All execution-focused agents (Coding Tasks, Data Scientist, Experiment Orchestrator) MUST follow the ReAct loop:
1.  **Thought:** Analyze the research specification (Wiki) and the current workspace state.
2.  **Action:** Execute a specific tool (e.g., `run_shell_command`, `write_file`).
3.  **Observation:** Review the tool's output or environment changes.
4.  **Response:** Iterate based on the observation until the goal is achieved.

### 🛡️ Adversarial Debate & Review
Before any new model architecture or clinical workflow is finalized, the framework triggers a multi-agent debate:
- **Expert Statistician:** Challenges the methodological assumptions (Methodology).
- **Data Ethicist:** Reviews for privacy risks and algorithmic fairness (Privacy/Ethics).
- **Clinical Translator:** Evaluates clinical actionability and utility (Utility).
- **Antagonic Researcher:** Audits for logical consistency against the existing Wiki.

### ⛓️ Skill Chaining (The Ingest Pipeline)
The process of adding new research follows a strict hand-off chain:
`Literature Researcher (Discovery)` -> `Compression (Distillation)` -> `Wiki Maintainer (Orchestration)` -> `Antagonic Researcher (Consistency Audit)`.

### 🧪 Agentic Science & Autonomous Discovery (2026 Standards)
The framework adopts state-of-the-art autonomous discovery patterns:
- **STORM (Multi-Perspective Discovery):** For new domains, agents simulate a "Writer-Expert" dialogue to discover diverse research angles before drafting.
- **PaperQA2 (RCS Synthesis):** High-fidelity retrieval using **Reranking and Contextual Summarization (RCS)** to prevent context pollution.
- **The AI Scientist (Autonomous Loops):** For experimental phases, agents are permitted to define their own protocols in "template-free" mode if verified by the **Expert Statistician**.
- **LLM OS (Orchestration):** The framework operates as an "LLM OS," where the Wiki is the permanent File System, the Context Window is RAM, and agents are specialized processes orchestrated by the **Wiki Maintainer**.
- **RLVR Verification (Verifiable Rewards):** Before finalizing any clinical model, agents must identify a "Verifiable Reward" (e.g., code correctness, mathematical proof, or historical alignment) to ground the reasoning trace.
- **ContraCrow Logic:** Dedicated audit for finding "Gaps of Ignorance" (contradictions across thousands of sources).

## 6. Publication Standards & Target Venues

To ensure high-impact dissemination, the framework supports automated adaptation to specific target venues and reporting standards.

### 🏛️ Supported Venues
- **NeurIPS (Machine Learning):** Focuses on technical novelty, mathematical rigor, and the mandatory NeurIPS Checklist.
- **The Lancet Psychiatry (Clinical):** Focuses on clinical utility, safety, and the "Research in Context" panel.
- **Nature Medicine (Translational):** Focuses on bridging technical innovation with significant clinical impact.

### 📋 International Reporting Standards
The `scientific-writer` agent enforces compliance with the following AI-specific reporting extensions:
- **CONSORT-AI / SPIRIT-AI:** For clinical trials and protocols.
- **TRIPOD-AI:** For prediction model development and validation.
- **STARD-AI:** For diagnostic accuracy studies.

Detailed guidelines for each are maintained in `papers/guides/publications/`.

## 8. Advanced Research Architectures and Staging

To manage high-impact, journal-tier research projects, agents must adhere to the following advanced architectural patterns. These patterns ensure that the PhD framework remains scalable and that individual research projects are self-contained and reproducible.

### 📂 The Registry Pattern (Project Siloing)
Multi-paper research environments must use the **Registry Pattern** to prevent artifact pollution. Each major research project or paper must be isolated within its own registry.
- **Location:** `papers/registries/[project_slug]/`
- **Mandatory Silos:**
    - `manuscript/`: Self-contained LaTeX/Markdown sources. Sectioned for high-volume bypass (Modular LaTeX).
    - `data/`: Project-specific simulation outputs, synthetic cohorts, or ingested datasets.
    - `results/`: CSV metrics, JSON certification logs, and statistical significance reports.
    - `plots/`: High-resolution, publication-quality figures with reproducible scripts.
- **Enforcement:** No root-level directories (`data/`, `results/`, `plots/`) should persist after the strategy phase. All project-specific assets must be migrated to the registry.

### 📝 Modular LaTeX Workflow (Context-Efficient Writing)
For manuscripts exceeding 10 pages, agents must use a **Modular LaTeX Structure** to ensure technical depth without data loss due to context limits.
- **Architecture:** A master `.tex` file (Preamble + Abstract) that incorporates sections via `\input{section_file}`.
- **Sectioning:** `intro.tex`, `related_work.tex`, `methods.tex`, `results.tex`, `discussion.tex`.
- **Benefit:** Allows the `scientific-writer` to perform surgical, high-volume expansions on specific sections (e.g., expanding a proof in `methods.tex`) without truncating the rest of the paper.

### 🛠️ The Hardening Loop (Proving Theoretical Advantage)
Scientific rigor is established not by reporting best-case results on easy data, but by **failure-mode analysis**.
- **The Loop:** Initial Benchmarking -> Identify 'Baseline Cheat' (e.g., simple interpolation on smooth data) -> **Harden Simulation** (increase persistence, non-stationarity, MNAR intensity) -> **Architecture Upgrade** -> Verify Causal Advantage.
- **Goal:** Deliberately increase simulation difficulty until standard state-of-the-art (SOTA) baselines collapse, then prove the theoretical resilience of the proposed framework.

### ⚖️ Socio-Technical Calibration (Distributive Justice)
Clinical models must distinguish between **Pathological Signals** and **Socio-Technical Artifacts**.
- **Requirement:** Simulations must include technical covariates (battery age, device quality, connectivity jitter).
- **Audit:** The `data-ethicist` must verify that the model decouples technical dropout from clinical crisis to prevent "Digital Redlining" or algorithmic bias against low-resource populations.

### 📉 Spatiotemporal Error Distribution (SED)
Research must move beyond global aggregate metrics (AUROC/RMSE).
- **Standard:** Use **Residual Heatmaps** centered on clinical crisis events ($t=0$).
- **Metric:** Quantify the **Informational Causal Gap (ICG)**—the temporal horizon $\tau^*$ where state recovery becomes non-identifiable.

## 9. End-to-End Research Orchestration

The **Research Orchestrator Agent** is the primary entry point for complex, end-to-end scientific investigations. It is responsible for transitioning a research question from initial discovery to a certified research registry.

### 🔄 The Orchestration Lifecycle
1.  **Gap Discovery:** Invokes `literature-researcher` and `expert-statistician` to identify a specific failure mode in the current literature (e.g., "The Digital Vacuum Paradox").
2.  **Simulation Archeology:** Invokes `coding-tasks` to build a modular simulator (SDE-based) that incorporates the identified failure mechanism (MNAR).
3.  **The Hardening Phase:** Executes the **Hardening Loop** to deliberately break standard baselines and justify the need for a new framework.
4.  **Mathematical Certification:** Formalizes the mathematical proofs and transition densities via the `expert-statistician`.
5.  **Registry Assembly:** Consolidates all artifacts into the `papers/registries/[project_slug]/` structure.
6.  **Modular Synthesis:** Exports a 12-15 page journal-ready manuscript using the **Modular LaTeX Workflow**.

### 📝 Research Readiness Criteria
A project is deemed "Research Ready" when it has a confirmed theoretical advantage over 3+ hardened baselines and is documented in a modular LaTeX hub with at least 30+ high-impact references.
