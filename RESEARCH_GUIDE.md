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
Every paper must be documented in a standalone Markdown file using the following naming convention: `[author]_[year]_[short_descriptive_title].md`.

### Required Sections:
- **Title & Metadata:** Full title, all authors, year, and venue (e.g., NeurIPS, Nature Medicine).
- **Core Methodology:** Specific algorithms, causal assumptions (SCMs), or RL frameworks.
- **Dataset Details:** Explicitly mention clinical datasets (MIMIC-III, STAR*D) and sample sizes.
- **Key Findings:** High-signal results and statistical significance.
- **Clinical Impact:** How this directly affects psychiatric practice or patient outcomes.
- **References for Discovery:** A "Next Steps" section listing 2-3 papers from the references for future research.

## 4. Tracking & Synchronization
- **`papers/RESEARCH_INDEX.md`**: The source of truth for what has been read. It must be updated immediately after a new paper is added.
- **`KNOWLEDGE_BASE.md`**: High-level synthesis across labs. Update this when a new "Domain Layer" (e.g., Neural SDEs) becomes significant.
- **`doc-sync-skill`**: Use this skill to ensure all indices and READMEs reflect the new additions.

## 5. From Paper to Implementation
1.  **Verification:** Use the `antagonic-researcher` to find critiques of the paper.
2.  **Feasibility:** Check if the paper provides a repository or enough technical detail for the `coding-tasks` agent.
3.  **Drafting:** Create an entry in `src/` for experimental implementation if the methodology is actionable.
