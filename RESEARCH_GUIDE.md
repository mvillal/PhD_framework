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

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** 2-3 key references to explore next.
- **Descendant Discovery:** Search patterns for forward snowballing.
```

## 4. Tracking & Synchronization
- **`papers/RESEARCH_INDEX.md`**: The source of truth for what has been read. It must be updated immediately after a new paper is added.
- **`KNOWLEDGE_BASE.md`**: High-level synthesis across labs. Update this when a new "Domain Layer" (e.g., Neural SDEs) becomes significant.
- **`doc-sync-skill`**: Use this skill to ensure all indices and READMEs reflect the new additions.

## 5. From Paper to Implementation
1.  **Verification:** Use the `antagonic-researcher` to find critiques of the paper.
2.  **Feasibility:** Check if the paper provides a repository or enough technical detail for the `coding-tasks` agent.
3.  **Drafting:** Create an entry in `src/` for experimental implementation if the methodology is actionable.
