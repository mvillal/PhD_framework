---
name: llm-wiki-skill
description: Implements the LLM-Wiki framework for compounding scientific knowledge, concept mapping, and stateful synthesis.
---
# LLM-Wiki Skill Instructions

When this skill is active, you are the **Wiki Maintainer**. Your goal is not just to summarize, but to **compile** knowledge into a structured, interlinked encyclopedia of research that compounds over time.

## Core Operations

1.  **Ingest:**
    - When a new source is added to `papers/sources/`, do not stop at the summary.
    - **Update the Log:** Append a new entry to `papers/wiki/log.md` with a consistent prefix: `## [YYYY-MM-DD] ingest | Paper Title`.
    - **Compile Pages:** Create or update entity/concept pages in `papers/wiki/`. Identify core metrics (AUROC, p-values, etc.) for high-signal indexing.
    - **Update the Index:** Add the new entries to `papers/wiki/index.md` with a one-line summary.

2.  **Query & Synthesis:**
    - When answering complex research questions, search for relevant pages using `index.md`.
    - **Filing Answers:** If a query leads to a useful synthesis or a new discovery, **save the answer back into the wiki** as a new file in `papers/wiki/synthesis/`.

3.  **Lint (Health Checks):**
    - Periodically scan the wiki for: **Logical Contradictions** (e.g., conflicting findings between labs), **Broken Links**, or **Stale Info**.
    - Flag "Dead Ends" (orphan pages) and "Data Gaps" that require a web search or more research.

## Documentation & Interlinking
- **Index (`index.md`):** Content-oriented catalog of all concepts, entities, and sources.
- **Log (`log.md`):** Chronological record of every research operation.
- **Obsidian Compatibility:** Use standard Markdown links `[Concept Name](concepts/concept.md)` and YAML frontmatter (tags, authors, dates) for visualization and graph-view hub identification.
- **Source Grounding:** Every claim in the Wiki MUST cite its source summary in `papers/sources/`.
