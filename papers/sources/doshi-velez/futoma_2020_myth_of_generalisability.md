---
title: "The Myth of Generalisability in Clinical Machine Learning"
authors: ["Joseph Futoma", "Christopher Simons", "Finale Doshi-Velez"]
year: 2020
lab: "Data to Actionable Knowledge Lab (DtAK), Harvard SEAS"
venue: "The Lancet Digital Health"
doi: "10.1016/S2589-7500(20)30186-2"
url: "https://www.thelancet.com/journals/landig/article/PIIS2589-7500(20)30186-2/fulltext"
datasets: ["MIMIC-III", "Private Hospital EHR"]
tags: ["Generalizability", "Local Validation", "Clinical Machine Learning", "Robustness"]
---

# The Myth of Generalisability in Clinical Machine Learning

## 📋 Executive Summary
This seminal commentary challenges the traditional clinical research paradigm that demands universal geographical generalizability as the primary gold standard for validity. The authors argue that local utility—how well a model performs in its specific clinical and administrative environment—is more critical than universal mediocrity across heterogeneous sites.

## 🛠️ Core Methodology
- **Validity vs. Generalisability:** Deconstruction of the "generalizability" metric, arguing that it often conflates predictive accuracy with the stability of administrative practice patterns.
- **Local Recalibration Framework:** Advocacy for site-specific model adaptation (recalibration) to account for differences in patient demographics, hardware (e.g., MRI manufacturers), and clinical workflows.
- **Critical Review of External Validation:** Analysis of why "state-of-the-art" models often fail when transported across health systems.

## 📊 Dataset & Experimental Setup
- **Data Source:** Literature meta-analysis and case studies using MIMIC-III and EHR data from NYU and other major medical centers.
- **Sample Size:** Systematic review of hundreds of clinical ML models.
- **Evaluation Metrics:** Comparative analysis of AUROC/AUPRC across internal vs. external validation cohorts.

## 💡 Key Findings
- **Local Practice Patterns:** Models often learn site-specific administrative signatures (e.g., "how often is a labs test ordered") rather than universal biology, leading to performance drops during external validation.
- **Local Utility > Global Performance:** A model that is 95% accurate at one hospital but 70% elsewhere is more useful than a model that is 75% everywhere if the goal is local patient care.
- **Continuous Maintenance:** Models must be treated as "living software" that requires ongoing local maintenance and re-training as clinical practices evolve.

## 🩺 Clinical Relevance & Impact
In psychiatry, where data collection (e.g., EMA, clinical notes) is highly subjective and varied across institutions, the "myth of generalisability" highlights the mandatory requirement for local validation. A suicide risk model trained at one hospital cannot be safely deployed at another without rigorous local calibration.

## 🔬 Critical Review (Antagonic Perspective)
While the emphasis on local utility is pragmatic, it risks creating "data silos" where models cannot be shared, potentially disadvantageous for smaller clinics with sparse data that cannot support local re-training. A balance between global pre-training and local fine-tuning (e.g., via Transfer Learning) is needed.

## 🔗 Discovery & Next Steps
- **Ancestor Discovery:** Zech et al. (2018) on confounding by site in medical image analysis.
- **Descendant Discovery:** Research into "Federated Learning" as a potential technical solution to the generalization challenge.
