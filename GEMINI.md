# PhD Framework: ML in Psychiatry

This repository is dedicated to the research and development of Machine Learning applications in Psychiatry. It serves as a knowledge base and experimentation environment for PhD research.

## Core Mandates
- **Field Focus:** Machine Learning applied to Psychiatry.
- **Key Research Domains:** Sequential Decision-Making in Psychiatry, Continuous-Time Risk Forecasting, and Human-AI Alignment in Clinical Settings.
- **Featured Lab:** Data to Actionable Knowledge Lab (DtAK), Harvard SEAS (led by Finale Doshi-Velez).
- **Technology Stack:** Python (managed by `uv`), Gemini CLI for research orchestration.
- **Methodology:** Systematic literature review, distillation of information, and rigorous challenge of hypotheses.
- **LLM-Wiki Paradigm:** Implement a stateful, compounding knowledge base where the LLM acts as a "Wiki Maintainer," compiling raw sources into interlinked concept and entity pages.
    - **index.md:** Content-oriented catalog of all wiki entries for efficient navigation.
    - **log.md:** Chronological, append-only record of all research operations (ingest, query, lint).
- **Documentation Integrity:** Always keep `README.md`, the LLM-Wiki (`index.md`, `log.md`), and repository structure documentation in sync with codebase changes using the `doc-sync-skill`.

## Specialized Sub-Agents & Skills

- **Literature Researcher:** Focuses on finding, reading, and summarizing relevant academic papers.
- **Wiki Maintainer Agent:** (Formerly Literature Cleaner) Responsible for compiling raw sources into the `papers/wiki/` structure, ensuring interlinking, and tracking research evolution.
- **Compression Agent:** Distills complex information into key takeaways and core insights.
- **Adversarial Knowledge Auditor:** (Formerly Antagonic Researcher) Proactively stress-tests the Wiki's integrity, evaluating findings against Celerity Bias, Innovation Stagnation, and The Local Trap.
- **Scientific Writer Agent:** Transforms research findings, statistical analyses, and engineering logs into publication-ready academic text following the IMRaD format.
- **Coding Tasks Agent:** Specialized in Python-based ML implementations for psychiatric data analysis.
- **Expert Statistician Agent:** Validates experimental design, causal assumptions, and uncertainty quantification (Bayesian credible intervals). Specialized in Bayesian Non-parametrics and Causal Transportability.
- **Senior Software Engineer Agent:** Ensures code integrity, scalability, and reproducibility of research implementation using DDD and Hexagonal Architecture.
- **Data Scientist Agent:** Preprocesses, analyzes, and models clinical datasets (MIMIC-III, eICU, EMA). Specialized in Informative Missingness and Deep Generative Modeling.
- **LLM-Wiki Skill:** Implements the workflows for stateful ingestion, linking, and synthesis of research knowledge.
- **Documentation Sync Skill:** Automatically synchronizes `README.md` and other documentation with changes in folder structure and code definitions.

## Project Structure
- `src/`: Core Python code and research tools.
- `.gemini/agents/`: Definitions for specialized research sub-agents.
- `notebooks/`: Exploratory data analysis and research experiments.
- `papers/`: Local knowledge base and notes on literature.
