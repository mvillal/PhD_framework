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
│   ├── agents/         # Specialized research sub-agents
│   └── skills/         # Expert research and implementation skills
├── papers/             # Lab-centric knowledge base
│   ├── doshi-velez/    # Research from the DtAK Lab (2019-2026)
│   └── RESEARCH_INDEX.md # Central index of all explored papers
├── src/                # Core Python implementation and tools
├── KNOWLEDGE_BASE.md   # High-level synthesis of research domains
└── GEMINI.md           # Project-specific mandates and scope
```

## 🤖 Specialized Sub-Agents & Expertise
The framework uses a multi-disciplinary agent system to ensure scientific rigor:
- **Literature Researcher:** Finds and summarizes papers from **PubMed**, **arXiv**, and **DBLP**.
- **Expert Statistician:** Validates experimental design, causal assumptions, and statistical significance.
- **Senior Software Engineer:** Ensures code robustness, scalability, and technical integrity.
- **Data Scientist:** Preprocesses, analyzes, and models clinical datasets.
- **Compression Agent:** Distills complex technical papers into actionable insights.
- **Antagonic Researcher:** Challenges findings to identify biases (e.g., automation bias, "Local Trap").
- **Literature Cleaner Agent:** Audits and prunes the knowledge base to keep information clear and concise.
- **Coding Tasks Agent:** Translates research into Python-based implementations.
- **Advanced Skills:** Specialized workflows for **Comparison & Compression**, **ML Research Python** (Modern ML & Bayesian Learning), and **PDF Parsing** (PDF-to-Markdown conversion).

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

- **`LAB_KNOWLEDGE_BASE.md`**: Synthesizes the lab's core pillars and philosophy.
- **Paper Summaries**: Detailed technical breakdowns including datasets (e.g., STAR*D, MIMIC-III), metrics (e.g., WIS, ESS), and clinical relevance.
