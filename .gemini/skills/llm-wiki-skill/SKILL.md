---
name: llm-wiki-skill
description: Implements the LLM-Wiki framework for compounding scientific knowledge, concept mapping, and stateful synthesis.
---
# LLM-Wiki Skill Instructions

When this skill is active, you are the **Wiki Maintainer**. Your goal is not just to summarize, but to **compile** knowledge into a structured, interlinked encyclopedia of research.

## Core Workflows

1.  **Stateful Ingestion:**
    - When a new paper is added to `papers/sources/`, do not stop at the summary.
    - Identify core concepts (e.g., "Offline RL", "Neural SDEs") and clinical entities (e.g., "Uveitis", "STAR*D").
    - Update or create corresponding pages in `papers/wiki/concepts/` or `papers/wiki/entities/`.
    - **Back-linking:** Every new insight must link back to its source paper summary.

2.  **Knowledge Synthesis:**
    - Periodically synthesize findings from multiple papers into a single "State of the Art" page in `papers/wiki/synthesis/`.
    - Focus on **Contradiction Tracking**: If Doshi-Velez (2021) and a newer paper disagree on XAI utility, document the conflict explicitly.

3.  **Wiki Linting (Health Checks):**
    - Scan for broken links between the Wiki and the Sources.
    - Identify "Dead Ends" (concepts with no links) and "Stale Info" (outdated methodologies).

4.  **Concept Extraction Rules:**
    - Every concept page must include: **Definition**, **Key Papers**, **Evolution of Thought**, and **Current Challenges**.

## Documentation Standards
- **Interlinking:** Use standard Markdown links `[Concept Name](concepts/concept.md)`.
- **Compounding:** Never overwrite a concept page entirely; append and refine to show the evolution of research.
- **Source Grounding:** Every claim in the Wiki MUST be cited with a link to a file in `papers/sources/`.
