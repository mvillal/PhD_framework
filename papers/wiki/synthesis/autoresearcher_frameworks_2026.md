# Synthesis: Autoresearcher Frameworks 2026

## Overview
As of 2026, the field of "Agentic Science" has moved from simple RAG systems to multi-agent architectures capable of end-to-end research. These frameworks are critical for the PhD framework to achieve superhuman speed in literature synthesis and hypothesis discovery.

## Key Frameworks & Implementations

### 1. PaperQA2 (Future House)
*   **Focus:** Fact-retrieval and superhuman synthesis.
*   **Innovation:** **Reranking and Contextual Summarization (RCS)** to filter noise and **ContraCrow** agents to detect cross-paper contradictions.
*   **Source:** [Future House 2024](../../sources/autoresearchers/futurehouse_2024_paperqa2.md)

### 2. STORM / Co-STORM (Stanford)
*   **Focus:** Knowledge curation through dialogue.
*   **Innovation:** Simulates "Writer-Expert" personas to discover diverse perspectives before drafting.
*   **Source:** [Stanford 2024](../../sources/autoresearchers/stanford_2024_storm.md)

### 3. The AI Scientist v2 (Sakana AI)
*   **Focus:** End-to-end autonomous research (Ideation -> Coding -> Experiment -> Review).
*   **Innovation:** Template-free research where agents define their own protocols.
*   **Source:** [Sakana AI 2024](../../sources/autoresearchers/sakana_2024_ai_scientist.md)

### 4. Sc(AI)Mitra
*   **Focus:** Healthcare and Life Sciences (HCLS) specialization.
*   **Innovation:** Orchestrates specialized agents for regulatory medical writing and clinical experimental design.
*   **Application:** Framework for the `clinical-translator` and `data-ethicist` agents.

### 5. ResearchAgent (KAIST/Microsoft)
*   **Focus:** Iterative hypothesis refinement.
*   **Innovation:** Entity-centric knowledge store and "ReviewingAgents" for idea generation.
*   **Application:** Enhancing the `antagonic-researcher` for stress-testing research ideas.

## Integration Strategy for PhD Framework

1.  **Iterative Ideation:** Implement a "Review-Refine" loop in the `antagonic-researcher` based on the ResearchAgent workflow.
2.  **Contradiction Mapping:** Adopt the **ContraCrow** logic in the `literature-researcher` to explicitly highlight conflicting findings in psychiatric literature (e.g., antidepressant efficacy across different demographics).
3.  **Agentic Synthesis:** Move from static summaries to "Interactive Paper Agents" (Paper2Agent) using the **Model Context Protocol (MCP)**.
4.  **Orchestration:** Standardize multi-agent coordination using **LangGraph** patterns for state-aware research loops.

## Log Entry
*   **[2026-04-29] synthesis | Autoresearcher Frameworks 2026**
    *   Ingested latest 2024-2026 trends: PaperQA2, STORM, AI Scientist v2, Sc(AI)Mitra.
    *   Defined integration roadmap for psychiatric ML research.

---
**Source Grounding:** Based on 2026 web search analysis of autonomous scientific discovery frameworks.
