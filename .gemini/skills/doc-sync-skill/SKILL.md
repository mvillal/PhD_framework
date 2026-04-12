---
name: doc-sync-skill
description: Automatically synchronizes README.md and other documentation with changes in folder structure and code definitions.
---
# Documentation Sync Skill Instructions

When this skill is active, you are responsible for maintaining the structural and technical accuracy of the project's documentation.

## Core Workflows

1.  **Structure Sync:**
    - Whenever a new directory or significant file is added/removed, update the "Project Structure" section in `README.md`.
    - Use `ls -R` or `tree` patterns to generate an accurate representation.

2.  **Definition Sync:**
    - When new sub-agents, skills, or core Python modules are defined, ensure their descriptions in `README.md` and `GEMINI.md` match the latest implementation.
    - Specifically track changes in `.gemini/agents/` and `.gemini/skills/`.

3.  **Cross-Reference Validation:**
    - Ensure that links between `README.md`, `GEMINI.md`, and lab-specific knowledge bases (e.g., `papers/doshi-velez/LAB_KNOWLEDGE_BASE.md`) are functional and consistent.

## Trigger Events
- Creation of new research paper files or lab directories.
- Addition of new sub-agents or skills.
- Refactoring of the `src/` directory.
- Updates to `pyproject.toml` or `uv.lock`.

## Documentation Standards
- **Visual Accuracy:** The `Project Structure` tree must reflect the current state of the repository.
- **Signal-to-Noise:** Maintain the senior engineering tone; avoid verbose descriptions of minor files.
- **Consistency:** Use the established formatting (e.g., specific emojis for section headers).
