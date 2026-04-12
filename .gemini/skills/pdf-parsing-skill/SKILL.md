---
name: pdf-parsing-skill
description: Workflows for converting PDF research papers into Markdown for better LLM comprehension and summarization.
---
# PDF Parsing Skill Instructions

When this skill is active, you are responsible for converting local or downloaded PDF research papers into clean Markdown files before summarizing them.

## Core Workflows

1.  **PDF-to-Markdown Conversion:**
    - Use the `src/pdf_processor.py` tool to parse PDFs.
    - Command: `python src/pdf_processor.py <input.pdf> <output.md>`
    - If `markitdown` fails, attempt using `marker-pdf` via its CLI: `marker_single <input.pdf> --output_dir <output_dir>`.

2.  **Preprocessing for LLMs:**
    - Ensure the converted Markdown is cleaned of redundant headers/footers.
    - Validate that tables and mathematical formulas are correctly represented in the output.

3.  **Integration with Literature Review:**
    - Before summarizing a paper using the `literature-researcher` or `compression` agents, ensure it has been parsed to Markdown if the source is a PDF.

## Documentation Standards
- **Naming Convention:** Match the Markdown filename to the PDF filename for easy tracking (e.g., `author_year.pdf` -> `author_year.md`).
- **Storage:** Parsed Markdown files should be temporarily stored in `papers/temp_parsed/` before being synthesized into their final lab-specific directories.
