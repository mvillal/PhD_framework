# Causal Off-Policy Evaluation (Parbhoo et al., 2022)

## Summary
Introduces a framework for more robust Off-Policy Evaluation (OPE) by incorporating causal inference to improve generalizability and identifiability across different patient populations.

## Datasets
- **Sepsis Simulator:** A synthetic but clinically-grounded environment for simulating sepsis treatment.
- **ACTG 175 HIV Data:** Observational data from the AIDS Clinical Trials Group study 175.

## Methodology
- **SCMs (Structural Causal Models):** Representing clinical processes with structural equations to capture underlying causal relationships.
- **Multiply-Robust Estimators:** Combining multiple models (e.g., outcome regression and propensity scoring) to provide more reliable policy value estimates even if some components are misspecified.
- **Causal Transportability/do-calculus:** Applying Pearl's do-calculus to formalize how policies can be transferred (transported) from one population to another.

## Metrics
- **Policy Value V:** The expected reward associated with following a particular treatment policy.
- **Identifiability:** Determining if a causal effect can be uniquely estimated from the available data.

## Clinical Findings
- **Predicting Policy Performance:** Demonstrated that incorporating causal structures allows for more accurate predictions of how a policy will perform in new subpopulations (e.g., different demographics or clinical settings).
- **Transportability:** Successfully showed how treatment policies for HIV can be adapted and evaluated for different patient cohorts.
