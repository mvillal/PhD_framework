# Automated Vitreous Haze Grading in OCT (Haggag et al., 2021)

## Summary
The study presents an automated method for grading vitreous haze using Optical Coherence Tomography (OCT) imaging, providing an objective alternative to subjective clinical grading scales.

## Methodology
- **U-Net Segmentation:** Employed a U-Net architecture to automatically segment the vitreous and the Retinal Pigment Epithelium (RPE) in OCT B-scans.
- **Intensity Ratio (VIT/RPE):** Calculated the ratio of the mean pixel intensity in the vitreous region to the mean pixel intensity of the RPE.
- **Objective Quantification:** Used the VIT/RPE ratio as a continuous metric for inflammation severity.

## Findings
- **High Accuracy:** Automated grading showed strong agreement with manual vitreous haze scores provided by expert graders.
- **Reduced Subjectivity:** Provided a reproducible metric that eliminates the variability inherent in the Standardized Uveitis Nomenclature (SUN) clinical grading.

## Relevance
- **Clinical Trial Endpoints:** Offers a more precise and objective endpoint for clinical trials investigating new uveitis treatments.
- **Precision Monitoring:** Enables subtle changes in inflammation to be detected over time, which might be missed by manual observation.
