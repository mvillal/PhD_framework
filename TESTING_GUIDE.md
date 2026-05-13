# Testing Standards & Stochastic Validation

This guide outlines the standards for testing the PhD Framework, specifically addressing non-deterministic components like LLMs and probabilistic models.

## 🏗️ The Testing Pyramid

We follow a three-layered testing approach:

1.  **Unit Tests:** Verify core DDD entities and business rules in isolation.
2.  **Integration Tests:** Verify that adapters (MLflow, Repositories) correctly implement the Ports.
3.  **Behavioral/Eval Tests:** Verify the quality and reliability of stochastic research workflows.

---

## 🎲 Testing Non-Deterministic Systems

### 1. LLM Frameworks (Wiki-Refiner)
For LLM-driven agents, we do not use exact-match assertions. Instead, we use:

- **Property-Based Testing:** Use the `Hypothesis` library to verify that generated outputs always follow a specific schema (e.g., "The output is always valid JSON").
- **Semantic Similarity:** Compare generated summaries against a "Golden Dataset" using cosine similarity thresholds (>0.85).
- **Mocks for Logic:** Always mock LLM API calls in unit tests to ensure the "scaffold" logic (parsing, logging, state transitions) is 100% deterministic.

### 2. Probabilistic Models (Bayesian ML)
For Bayesian models (Pyro/PyMC), we use statistical validation:

- **Posterior Predictive Checks (PPC):** Verify that the model can recreate the observed data distribution.
- **Convergence Checks:** Monitor R-hat and Effective Sample Size (ESS) in CI for critical models.
- **Deterministic Seeds:** ALWAYS set and log global random seeds for reproducibility, but test across multiple seeds to ensure robustness.

---

## 🤱 The Object Mother Pattern

To ensure test data is consistently available and maintainable, use the `mothers/` directory.

- **Purpose:** Centralizes the creation of complex entities (`Run`, `Metric`) with sensible defaults.
- **Usage:**
  ```python
  from tests.mothers.entity_mother import RunMother
  run = RunMother.completed_run()
  ```

## 🛠️ Performance Guardrails
- **CI Speed:** Unit and Integration tests should run in <10 seconds.
- **Evals Scope:** Behavioral/Eval tests (e.g., running real LLM prompts) should be triggered manually or only on PRs to the `main` branch to control costs.
