# Containerization Strategy for PhD Framework

This document outlines the containerization strategy to ensure stability, portability, and reproducibility of the research agents and ML experiments.

## 🐳 Docker Architecture

We use a **Multi-Stage Build** to optimize image size and security. This ensures that build tools (like compilers and `uv`) are not present in the final production image.

### GPU Awareness (NVIDIA)
For model training and fine-tuning, we use the **NVIDIA Container Toolkit**. The `Dockerfile` is compatible with GPU-accelerated base images.
- **Recommended Base:** `nvidia/cuda:12.4.1-runtime-ubuntu22.04` (for GPU-heavy production) or standard Python slim (for CPU-based research agents).
- **Run with GPU:** `docker run --gpus all ...`

## ☁️ GCP Deployment (Vertex AI & GKE)

The framework is designed for seamless deployment to Google Cloud Platform using **Vertex AI Custom Training** or **Google Kubernetes Engine (GKE)**.

### 1. Vertex AI Custom Training
Vertex AI is the preferred method for running heavy training jobs (e.g., fine-tuning).
- **Artifact Registry:** Push images to `[LOCATION]-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY]/[IMAGE]`.
- **Custom Job:** Use the `google-cloud-aiplatform` SDK to launch jobs with specific machine types and GPUs (e.g., `n1-standard-8` with 1x `NVIDIA_TESLA_T4`).
- **Data Integration:** Mount GCS buckets for large clinical datasets.

### 2. GKE (Google Kubernetes Engine)
For long-running, autonomous agents, deploy as a K8s Deployment.
- **Node Pools:** Use GPU-enabled node pools for faster inference.
- **Interoperability:** Use K8s Secrets to manage API keys for agents.

## 🛠️ Makefile Commands

To improve interoperability and discovery, we use a `Makefile` to wrap complex Docker and execution commands.

| Command | Description |
| :--- | :--- |
| `make build` | Builds the Docker image. |
| `make shell` | Launches an interactive shell inside the container. |
| `make test-run` | Runs the `example_run.py` to verify tracking. |
| `make ingest-paper` | Runs the `wiki_refiner.py` for a specific paper path. |
| `make mlflow-ui` | Starts the MLflow UI locally. |

## 📦 Deployment Principles

1.  **Immutability:** Images are tagged with the git commit hash for full traceability.
2.  **Environment Parity:** The same image used for local testing is deployed to the cloud.
3.  **Secrets Management:** Sensitive information (API keys) are passed via environment variables at runtime, never baked into the image.
