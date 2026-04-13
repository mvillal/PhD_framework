import sys
import os
import re
import argparse
from pathlib import Path
from markitdown import MarkItDown

# Constants for project structure
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers" / "sources"

def process_pdf(pdf_path: str, output_path: str = None):
    """
    Converts a PDF file to Markdown using MarkItDown.
    """
    md = MarkItDown()
    try:
        result = md.convert(pdf_path)
        content = result.text_content
        
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully converted {pdf_path} to {output_path}")
        else:
            # Print to stdout if no output path provided
            print(content)
            
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        sys.exit(1)

def update_paper(file_path: Path, lab_name: str):
    """
    Updates a paper's markdown file with metadata and a standardized template.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract info
    title_match = re.search(r'^# (.*?)(?:\s\((.*?),\s(\d{4})\))?$', content, re.MULTILINE)
    if title_match:
        full_title = title_match.group(1)
        author_str = title_match.group(2) if title_match.group(2) else "TBD"
        year = title_match.group(3) if title_match.group(3) else "TBD"
    else:
        full_title = "TBD"
        author_str = "TBD"
        year = "TBD"

    # Try to extract authors and year from filename if not in title
    if year == "TBD":
        filename = file_path.name
        parts = filename.split('_')
        if len(parts) >= 2:
            author_from_file = parts[0].capitalize()
            year_from_file = parts[1]
            if year_from_file.isdigit():
                year = year_from_file
                author_str = f"{author_from_file} et al."

    # Extract sections
    sections = {}
    current_section = None
    for line in content.split('\n'):
        if line.startswith('## '):
            current_section = line[3:].strip()
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)

    for k in sections:
        sections[k] = '\n'.join(sections[k]).strip()

    # Map sections to new template
    summary = sections.get('Summary', 'TBD')
    methodology = sections.get('Methodology', 'TBD')
    # Merge Dataset, Datasets, and some of Methodology if needed
    dataset_info = sections.get('Dataset', sections.get('Datasets', 'TBD'))
    findings = sections.get('Findings', sections.get('Key Findings', 'TBD'))
    relevance = sections.get('Relevance', 'TBD')
    
    # Specific mappings for some papers
    if 'Core Philosophy' in sections:
        relevance += '\n\n' + sections['Core Philosophy']
    if 'Expert Ground Truth' in sections:
        methodology += '\n\nExpert Ground Truth: ' + sections['Expert Ground Truth']
    if 'XAI Types Tested' in sections:
        methodology += '\n\nXAI Types: ' + sections['XAI Types Tested']
    if 'Metrics' in sections:
        dataset_info += '\n\nMetrics: ' + sections['Metrics']
    if 'Models' in sections:
        methodology += '\n\nModels: ' + sections['Models']

    # YAML Metadata
    authors_list = [author_str] if author_str != "TBD" else []
    
    # Heuristic for authors in some cases
    heuristic_authors = {
        "Agrawal et al.": ["Agrawal et al."],
        "Haggag et al.": ["Haggag et al."],
        "Mahajan et al.": ["Mahajan et al."],
        "Mohammadi et al.": ["Mohammadi et al."],
        "Umer et al.": ["Laraib Umer", "Umer Asgher", "Yasar Ayaz"],
        "Zhou et al.": ["Zhou et al."],
        "Fischer et al.": ["Fischer et al."],
        "Futoma et al.": ["Futoma et al."],
        "Gottesman et al.": ["Gottesman et al."],
        "Hang et al.": ["Hang et al."],
        "Huyuk et al.": ["Huyuk et al."],
        "Jacobs et al.": ["Jacobs et al."],
        "Jiang et al.": ["Jiang et al."],
        "Lu et al.": ["Lu et al."],
        "Parbhoo et al.": ["Parbhoo et al."],
        "Trella et al.": ["Trella et al."]
    }

    for key, val in heuristic_authors.items():
        if key in content:
            authors_list = val
            break

    # Infer Venue/DOI/Code if possible (mostly TBD for now)
    venue = "TBD"
    if "Nature" in content: venue = "Nature"
    if "Sensors" in content: venue = "Sensors (2021)"
    if "Scientific Reports" in content: venue = "Scientific Reports (2025)"
    
    new_content = f"""---
title: "{full_title}"
authors: {authors_list}
year: {year}
lab: "{lab_name}"
venue: "{venue}"
doi: "TBD"
code: "TBD"
datasets: ["TBD"]
tags: ["TBD"]
---

# {full_title}

## 📋 Executive Summary
{summary}

## 🛠️ Core Methodology
{methodology}

## 📊 Dataset & Experimental Setup
{dataset_info}

## 💡 Key Findings
{findings}

## 🩺 Clinical Relevance & Impact
{relevance}

## 🔬 Critical Review (Antagonic Perspective)
TBD

## 🔗 Discovery & Next Steps
TBD
"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def run_update_papers():
    # Lab Mapping
    doshi_velez_lab = "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
    uveitis_labs = {
        "agrawal_2025_oasis_uveitis_recurrence.md": "Singapore National Eye Centre (SNEC)",
        "haggag_2021_oct_vitreous_haze_grading.md": "BioImaging Laboratory, University of Louisville",
        "mahajan_2023_molecular_aging_proteomics.md": "Stanford Mahajan Lab",
        "mohammadi_2026_uwf_inflammation_detection.md": "Byers Eye Institute, Stanford University",
        "umer_2025_toxoplasmosis_activity_yolo.md": "National Center of Artificial Intelligence (NCAI), Pakistan",
        "zhou_2023_retfound_foundation_model.md": "UCL / Moorfields Eye Hospital (UK)"
    }

    print(f"Starting paper update process...")
    print(f"Project Root: {PROJECT_ROOT}")

    # Process Doshi-Velez
    dv_dir = PAPERS_DIR / "doshi-velez"
    if dv_dir.exists():
        print(f"Processing Doshi-Velez lab papers in {dv_dir}...")
        count = 0
        for f in dv_dir.iterdir():
            if f.suffix == '.md' and f.name != 'LAB_KNOWLEDGE_BASE.md':
                update_paper(f, doshi_velez_lab)
                count += 1
        print(f"Updated {count} papers for Doshi-Velez lab.")
    else:
        print(f"Warning: Doshi-Velez directory not found at {dv_dir}")

    # Process Uveitis
    uv_dir = PAPERS_DIR / "uveitis"
    if uv_dir.exists():
        print(f"Processing Uveitis papers in {uv_dir}...")
        count = 0
        for f in uv_dir.iterdir():
            if f.name in uveitis_labs:
                update_paper(f, uveitis_labs[f.name])
                count += 1
        print(f"Updated {count} papers for Uveitis labs.")
    else:
        print(f"Warning: Uveitis directory not found at {uv_dir}")

    print("Paper update process completed.")

def main():
    parser = argparse.ArgumentParser(description="PhD Framework Utilities")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: update-papers
    subparsers.add_parser("update-papers", help="Update paper source metadata and template")

    # Command: process-pdf
    pdf_parser = subparsers.add_parser("process-pdf", help="Convert PDF to Markdown")
    pdf_parser.add_argument("pdf_path", help="Path to the PDF file")
    pdf_parser.add_argument("--output", "-o", help="Optional output path for Markdown file")

    args = parser.parse_args()

    if args.command == "update-papers":
        run_update_papers()
    elif args.command == "process-pdf":
        process_pdf(args.pdf_path, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
