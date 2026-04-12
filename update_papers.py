import os
import re

def update_paper(file_path, lab_name):
    with open(file_path, 'r') as f:
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
        filename = os.path.basename(file_path)
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
    if "Agrawal et al." in content: authors_list = ["Agrawal et al."]
    if "Haggag et al." in content: authors_list = ["Haggag et al."]
    if "Mahajan et al." in content: authors_list = ["Mahajan et al."]
    if "Mohammadi et al." in content: authors_list = ["Mohammadi et al."]
    if "Umer et al." in content: authors_list = ["Laraib Umer", "Umer Asgher", "Yasar Ayaz"]
    if "Zhou et al." in content: authors_list = ["Zhou et al."]
    if "Fischer et al." in content: authors_list = ["Fischer et al."]
    if "Futoma et al." in content: authors_list = ["Futoma et al."]
    if "Gottesman et al." in content: authors_list = ["Gottesman et al."]
    if "Hang et al." in content: authors_list = ["Hang et al."]
    if "Huyuk et al." in content: authors_list = ["Huyuk et al."]
    if "Jacobs et al." in content: authors_list = ["Jacobs et al."]
    if "Jiang et al." in content: authors_list = ["Jiang et al."]
    if "Lu et al." in content: authors_list = ["Lu et al."]
    if "Parbhoo et al." in content: authors_list = ["Parbhoo et al."]
    if "Trella et al." in content: authors_list = ["Trella et al."]

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
    with open(file_path, 'w') as f:
        f.write(new_content)

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

# Process Doshi-Velez
dv_dir = "/home/mvillal/Documents/Github/PhD_framework/papers/doshi-velez/"
for f in os.listdir(dv_dir):
    if f.endswith('.md') and f != 'LAB_KNOWLEDGE_BASE.md':
        update_paper(os.path.join(dv_dir, f), doshi_velez_lab)

# Process Uveitis
uv_dir = "/home/mvillal/Documents/Github/PhD_framework/papers/uveitis/"
for f in os.listdir(uv_dir):
    if f in uveitis_labs:
        update_paper(os.path.join(uv_dir, f), uveitis_labs[f])
