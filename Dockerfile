# Use a specialized uv image for the builder stage
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

# Set the working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy only the dependency files first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies into a virtual environment
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# --- Runtime Stage ---
FROM python:3.13-slim-bookworm

# Set the working directory
WORKDIR /app

# Install runtime system dependencies (e.g., for PDF processing or MLflow)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Create a non-privileged user
RUN useradd -m research
USER research

# Copy the virtual environment from the builder
COPY --from=builder /app/.venv /app/.venv

# Copy the source code and artifacts
COPY src /app/src
COPY papers /app/papers
COPY .gemini /app/.gemini
COPY example_run.py /app/example_run.py

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"
ENV MLFLOW_TRACKING_URI="sqlite:///mlflow.db"

# Default command (can be overridden)
CMD ["python", "example_run.py"]
