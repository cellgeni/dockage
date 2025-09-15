FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive 

SHELL ["/bin/bash", "-c"]

ARG SCIB_METRICS_VERSION="0.5.7"
ARG SCVI_TOOLS_VERSION="1.4.0"

# non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_INSTALL_DIR="/usr/local/share/uv"

# Update and install system dependencies
RUN apt-get update && apt-get install -y \
    git build-essential procps curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Create venv first
RUN uv venv "${VENV_PATH}" --python 3.13

# Install python packages
RUN uv pip install --no-cache-dir -U pip setuptools wheel && \
    uv pip install --no-cache-dir \
    jupyterlab \
    papermill \
    bbknn \
    scib-metrics==${SCIB_METRICS_VERSION} \
    scvi-tools==${SCVI_TOOLS_VERSION} \
    "jax[cuda12]"


# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
