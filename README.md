# PhD Framework: ML in Psychiatry

A systematic research and development environment dedicated to Machine Learning applications in Psychiatry. This framework leverages the Gemini CLI to orchestrate literature reviews, synthesize findings, and implement experimental models.

## 🎯 Core Objectives
- **Systematic Literature Review:** Automated discovery and summarization of high-impact research (e.g., Doshi-Velez lab, DtAK).
- **Knowledge Base Construction:** Building a domain-layered, lab-centric knowledge base for training LLMs and informing experiments.
- **Causal & Interpretable ML:** Focusing on Reinforcement Learning (RL), Structural Causal Models (SCMs), and Explainable AI (XAI) in clinical settings.
- **Clinical Validation:** Bridging the gap between technical metrics (AUROC, OPE) and clinical utility (e.g., suicide risk forecasting, antidepressant selection).

## 📂 Project Structure
```text
.
├── .gemini/            # Gemini CLI configuration
│   ├── agents/         # Specialized research sub-agents (e.g., Wiki Maintainer)
│   └── skills/         # Expert research skills (e.g., LLM-Wiki, PDF Parsing)
├── papers/             # Research Knowledge Base (LLM-Wiki)
│   ├── sources/        # Lab-centric paper summaries (Source of Truth)
│   │   ├── doshi-velez/ # Research from the DtAK Lab (2019-2026)
│   │   └── uveitis/     # Research on clinical ophthalmology & ML
│   ├── wiki/           # Compiled Wiki (Concepts, Entities, Synthesis)
│   │   ├── concepts/   # Interlinked technical concept pages
│   │   └── entities/   # Dedicated pages for labs, authors, and datasets
│   └── RESEARCH_INDEX.md # Central index of all explored papers
├── src/                # Core Python implementation and tools
├── KNOWLEDGE_BASE.md   # High-level synthesis of research domains
├── RESEARCH_GUIDE.md   # Systematic discovery & documentation standards
└── GEMINI.md           # Project-specific mandates and scope
```

## 🤖 Specialized Sub-Agents & Expertise
The framework uses a multi-disciplinary agent system to ensure scientific rigor:
- **Literature Researcher:** Specialized in finding, reading, and summarizing academic papers on ML in psychiatry.
- **Wiki Maintainer:** (Formerly Literature Cleaner) Compiles raw paper summaries into an interlinked, compounding **LLM-Wiki**.
- **Expert Statistician:** Provides rigorous statistical validation; acts as a "Socratic gadfly" to challenge assumptions and experimental designs.
- **Senior Software Engineer:** Ensures robust, scalable research implementations using Domain-Driven Design (DDD) and Hexagonal Architecture.
- **Data Scientist:** Specialized in exploratory analysis, preprocessing, and modeling of heterogeneous psychiatric data.
- **Compression Agent:** Distills complex technical papers into concise, high-signal entries and actionable insights.
- **Antagonic Researcher:** Challenges findings, identifies biases, and provides counter-arguments to ensure scientific rigor.
- **Coding Tasks Agent:** Translates research into production-grade Python-based ML implementations.

### 🛠️ Research Skills
- **LLM-Wiki:** Implements the stateful ingestion, linking, and synthesis workflows of the LLM-Wiki framework.
- **Research Skill:** Expert PhD-level management of the research lifecycle, following systematic discovery (snowballing) workflows.
- **ML Research Python:** Specialized workflows for modern ML (PyTorch), Bayesian learning (Pyro/BlackJax), and Causal Inference.
- **PDF Parsing:** High-fidelity conversion of PDF research papers into Markdown using `markitdown` and `marker-pdf`.
- **Literature Comparison:** Specialized workflows for comparing, contrasting, and synthesizing different papers and lab philosophies.
- **KB Compression:** Distills large amounts of research data into concise, high-signal knowledge base entries.
- **Doc Sync:** Automatically synchronizes documentation with changes in folder structure and code definitions.

## 🚀 How to Leverage
### 1. Researching New Labs
To research a new lab or domain, use the `research-skill`:
```bash
# Example directive
"Research the most recent papers by the [Lab Name] and organize them into the papers/ directory."
```

### 2. Synthesizing Knowledge
The framework automatically maintains a `RESEARCH_INDEX.md` and `LAB_KNOWLEDGE_BASE.md` for each lab. Use these to:
- Identify "Decision Points" for Reinforcement Learning.
- Evaluate the "Myth of Generalizability" for a specific hospital dataset.
- Implement "Cognitive Forcing Functions" in clinician-AI interfaces.

### 3. Implementation
Translate findings into code using the `coding-tasks` agent:
```bash
# Example directive
"Based on the Gottesman et al. (2019) paper in our knowledge base, implement a Batch RL evaluation script using MIMIC-III data."
```

## 📜 Documentation Standards
All research follows a **Lab-Centric** organization pattern. For a detailed guide on discovery (snowballing), lab auto-discovery, and paper naming conventions, see **[RESEARCH_GUIDE.md](RESEARCH_GUIDE.md)**.

- **`LAB_KNOWLEDGE_BASE.md`**: Synthesizes the lab's core pillars, overarching philosophy, and primary mission.
- **YAML-Headed Summaries**: Mandatory use of the structured Markdown template for every paper (Metadata, Methodology, Findings, Clinical Impact).
- **PDF-to-Markdown Parsing**: Mandatory use of the **PDF Parsing Skill** (`markitdown`, `marker-pdf`) to ensure high-fidelity extraction of tables, formulas, and appendices before summarization.
