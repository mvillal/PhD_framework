---
title: "Liquid-biopsy proteomics combined with AI identifies cellular drivers of eye aging and disease in vivo"
authors: ["Wolf et al.", "Vinit B. Mahajan (Corresponding)"]
year: 2023
lab: "Mahajan Lab, Stanford University"
venue: "Cell"
doi: "10.1016/j.cell.2023.09.012"
code: "TEMPO Platform"
datasets: ["Aqueous Humor (AH)", "Vitreous Humor (VH)", "scRNA-seq Ocular Map"]
tags: ["Proteomics", "Liquid Biopsy", "Molecular Aging", "Oculomics", "TEMPO"]
---

# Molecular Ocular Aging & Liquid Biopsy AI

## 📋 Executive Summary
Wolf, Mahajan, et al. (2023) introduce the **TEMPO** (*Tracing Expression of Multiple Protein Origins*) platform, which uses AI to perform "virtual single-cell analysis" in living humans. Since direct tissue biopsy of the eye is impossible, they analyzed proteins in ocular fluids and mapped them back to single-cell transcriptomic signatures. This allowed them to build an **AI Proteomic Clock** that measures the "molecular age" of the eye and identifies cellular drivers of diseases like Diabetic Retinopathy and Uveitis.

## 🛠️ Core Methodology
- **TEMPO Framework:** Integrates **liquid biopsy proteomics** (~6,000 proteins) with **single-cell RNA-seq** from 57 ocular cell types.
- **AI Aging Clock:** Trained a model on a subset of 26 proteins to predict chronological age from ocular fluid samples.
- **Accelerated Aging Analysis:** Used the clock to identify "molecular aging gaps"—where the eye's molecular age exceeds the patient's chronological age.

## 📊 Dataset & Experimental Setup
- **Samples:** Aqueous humor and vitreous humor from hundreds of patients with various ocular conditions.
- **Validation:** Compared molecular age across Diabetic Retinopathy (DR), Uveitis, and Retinitis Pigmentosa.

## 💡 Key Findings
- **Accelerated Aging:** Diabetic Retinopathy was found to accelerate the eye's molecular age by up to **30 years** at the cellular level.
- **Cellular Transition:** Identified that the specific cell types driving disease progress change as the condition advances (e.g., from vascular to inflammatory cells).
- **Neurological Link:** Identified protein markers for **Parkinson’s Disease** in the eye fluid that were previously only seen post-mortem in the brain.

## 🩺 Clinical Relevance & Impact
The study transforms ocular diagnostics from "anatomy-based" to "molecular-based." It enables **Precision Clinical Trials** where the success of a drug can be measured by its ability to "reverse" the molecular aging of specific cell types in a living patient.

## 🔬 Critical Review (Antagonic Perspective)
While powerful, the mapping from fluid proteins to single cells depends on the "completeness" of the reference scRNA-seq map. If a rare or pathological cell state is not in the map, its proteomic signal may be misattributed to a similar healthy cell type.

## 🔗 Discovery & Next Steps
- **Implementation:** Explore using the TEMPO logic for other "inaccessible" organs like the brain via cerebrospinal fluid.
- **Concept Link:** Updates [Oculomics](../concepts/oculomics.md) and [Objective Inflammation Grading](../concepts/objective_inflammation_grading.md).
