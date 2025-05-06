# Start with a Python base image
FROM python:3.11-slim


# non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"


# Update and install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN pip install uv

# Create a new environment with uv and install packages
RUN uv venv "${VENV_PATH}" && \
    uv pip install --no-cache-dir \
    anndata==0.11.4 \
    scanpy==1.11.1 \
    celltypist==1.6.3 \
    jupyterlab \
    notebook \
    tqdm \
    ipywidgets \
    papermill

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
