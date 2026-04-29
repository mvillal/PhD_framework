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

## 6. From Paper to Implementation
1.  **Verification:** Use the `antagonic-researcher` to find critiques of the paper.
2.  **Clinical & Ethical Review:** 
    *   The **Clinical Translator** evaluates the model for safety (e.g., Causal Falsification) and clinical actionability.
    *   The **Data Ethicist** reviews the proposed data usage for privacy risks and algorithmic fairness.
3.  **Feasibility:** Check if the paper provides a repository or enough technical detail for the `coding-tasks` agent.
4.  **Orchestration:** The **Experiment Orchestrator** defines the experimental pipeline, ensuring tracking and reproducibility.
5.  **Drafting:** Create an entry in `src/` for experimental implementation if the methodology is actionable.
