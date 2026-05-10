# PhD Framework Management

IMAGE_NAME = phd-research-agent
TAG = $(shell git rev-parse --short HEAD 2>/dev/null || echo "latest")

.PHONY: build run run-gpu shell test-run mlflow-ui ingest-paper help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Build the Docker image using multi-stage builds
	docker build -t $(IMAGE_NAME):$(TAG) .

run: ## Run the default command in the container (CPU)
	docker run --rm -v $(PWD)/mlflow.db:/app/mlflow.db $(IMAGE_NAME):$(TAG)

run-gpu: ## Run the container with full GPU awareness (NVIDIA)
	docker run --rm --gpus all -v $(PWD)/mlflow.db:/app/mlflow.db $(IMAGE_NAME):$(TAG)

shell: ## Start an interactive shell in the container
	docker run --rm -it -v $(PWD)/mlflow.db:/app/mlflow.db $(IMAGE_NAME):$(TAG) /bin/bash

test-run: ## Run the example tracking script
	PYTHONPATH=. uv run python example_run.py

test: ## Run the full suite of unit and integration tests
	PYTHONPATH=. uv run pytest

mlflow-ui: ## Start the MLflow UI locally
	uv run mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000

ingest-paper: ## Ingest a specific paper (usage: make ingest-paper PATH=papers/sources/...)
	PYTHONPATH=. uv run python .gemini/agents/refiner_scripts/wiki_refiner.py $(PATH)

clean: ## Remove local tracking DB and virtual environment
	rm -rf mlflow.db mlruns .venv .pytest_cache
