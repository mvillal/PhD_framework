# The Myth of Generalizability (Futoma et al., 2020)

## Summary
A foundational paper that challenges the conventional wisdom of developing "globally generalizable" AI models in medicine, arguing that models often learn local administrative practices rather than clinical biology.

## Datasets
- **MIMIC-III:** ICU data from Beth Israel Deaconess Medical Center.
- **NYU Langone Health:** Clinical data from NYU's medical system, used for comparison and cross-validation.

## Methodology
- **LSTMs (Long Short-Term Memory Networks):** Used for modeling longitudinal clinical data.
- **Measurement Indicator Variables:** Explicitly modeling when and how clinicians choose to take measurements (e.g., ordering a lab test) as a source of information.

## Findings
- **Learning Local Practice Patterns:** AI models were found to be heavily influenced by how local clinicians and health systems order tests and record data.
- **Ordering Habits over Biology:** The "when" and "how" of clinical data collection were more predictive of outcomes than the actual patient physiology.

## Core Philosophy
- **Local Validation > Global AUROC:** A model's high Area Under the Receiver Operating Characteristic (AUROC) curve in a global dataset is less important than its performance and reliability in a local, real-world clinical context.
- **Context-Specific Models:** Recommends developing models that are specifically validated and tuned for the unique practices of each hospital or clinical setting.
