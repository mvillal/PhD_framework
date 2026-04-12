# How Much Should You Trust Your Explanation? (Jacobs et al., 2021)

## Summary
Investigates how different types of AI explanations affect clinician decision-making and the risk of automation bias in antidepressant selection.

## Dataset
- **STAR*D Vignettes:** Uses clinical vignettes derived from the Sequenced Treatment Alternatives to Relieve Depression (STAR*D) trial data.

## Expert Ground Truth
- Validated by **5 expert psychopharmacologists** to establish a baseline of correct treatment recommendations.

## XAI Types Tested
- **Feature Importance:** Highlights specific patient features that influenced the model's prediction.
- **Example-based:** Shows similar historical patient cases used to make the prediction.
- **Rule-based:** Provides the logic or decision rules used by the AI model.

## Metrics
- **Selection Accuracy:** How often clinicians chose the correct treatment.
- **Confidence:** Clinicians' self-reported confidence in their decisions.
- **Automation Bias:** The tendency of clinicians to follow incorrect AI recommendations, especially when accompanied by an explanation.

## Key Findings
- **Clinicians Follow Incorrect AI:** Clinicians were significantly more likely to follow the AI's recommendation even when it was incorrect.
- **Explanations Don't Fix Bias:** Providing an explanation (even a "good" one) did not reduce automation bias; in some cases, it increased clinicians' confidence in the incorrect AI recommendation.
- **XAI Limitations:** Explanations were not sufficient for clinicians to detect AI errors, highlighting the need for better human-AI interface designs.
