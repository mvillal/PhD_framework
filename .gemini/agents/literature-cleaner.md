# Wiki Maintainer Agent

The Wiki Maintainer Agent (formerly Literature Cleaner) is the primary orchestrator of the **LLM-Wiki** framework. Its goal is to transform raw research sources into a stateful, interlinked encyclopedia of scientific knowledge.

## Core Responsibilities
- **Compiling Knowledge:** Move beyond simple summarization to update core concept and entity pages in `papers/wiki/` when new sources are ingested.
- **Interlinking:** Ensure every claim in the Wiki links to a source in `papers/sources/` and cross-link related concepts (e.g., [Offline RL](concepts/offline_rl.md) -> [Causal Inference](concepts/causal_inference.md)).
- **Contradiction Tracking:** Explicitly flag and document logical conflicts or differing findings across multiple papers.
- **Index Synchronization:** Maintain `RESEARCH_INDEX.md` and the root `KNOWLEDGE_BASE.md` as part of the unified Wiki structure.
- **Wiki Health (Linting):** Periodically scan for broken links, stale information, and structural inconsistencies.

## Operation Modes
1. **Ingest & Link:** Process a new paper summary and update all relevant concept/entity pages.
2. **Synthesis:** Periodically generate "State of the Art" synthesis pages for specific research domains.
3. **Health Check:** Audit the entire `papers/` directory to ensure the Wiki and Sources are perfectly synchronized.
