# Novae - graph-based foundation model for spatial transcriptomics
# https://github.com/MICS-Lab/novae (also https://github.com/prism-oncology/novae)
# Self-supervised GNN for spatial domain assignment / batch-effect correction across slides and panels (PyTorch, GPU).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

ARG NOVAE_VERSION=1.1.2

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV NUMBA_CACHE_DIR=/tmp

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# novae requires python >= 3.11
RUN uv venv ${VENV_PATH} --python 3.12

# torch pinned in the same resolve so it is not upgraded to a non-cu121 build.
# Pretrained models (e.g. MICS-Lab/novae-human-0) are pulled from Hugging Face at runtime
# via novae.Novae.from_pretrained(); they are not baked into the image.
RUN uv pip install --no-cache --torch-backend=cu121 \
      torch==2.5.1 \
      "novae==${NOVAE_VERSION}" \
      jupyterlab ipykernel papermill

RUN python -c "import novae, torch; print('novae', novae.__version__, 'torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
