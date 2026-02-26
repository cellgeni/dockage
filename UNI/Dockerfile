FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONNOUSERSITE=1
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV UV_PYTHON_INSTALL_DIR="/usr/local/share/uv"

COPY --from=ghcr.io/astral-sh/uv:0.9.1 /uv /uvx /bin/

RUN apt-get update && apt-get install -y \
        git curl ca-certificates procps build-essential \
        libglib2.0-0 libsm6 libxext6 libxrender1 \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python 3.10

# Install PyTorch with CUDA 12.1 support first for GPU-enabled UNI usage
RUN uv pip install --index-url https://download.pytorch.org/whl/cu121 \
        torch torchvision

# Install UNI from source
RUN git clone https://github.com/mahmoodlab/UNI.git /opt/UNI && \
    cd /opt/UNI && \
    uv pip install -e .

# Standard notebook tooling
RUN uv pip install jupyterlab ipykernel papermill

WORKDIR /opt/UNI

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
