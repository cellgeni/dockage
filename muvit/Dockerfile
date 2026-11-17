# MuViT - https://github.com/weigertlab/muvit (PyPI: muvit)
# Multi-resolution vision transformers for microscopy (CVPR 2026): a ViT encoder that fuses
# crops at several physical resolutions, plus multi-resolution MAE pre-training (Lightning).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG MUVIT_VERSION="0.1.0"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV MPLCONFIGDIR=/tmp
ENV TORCHINDUCTOR_CACHE_DIR=/tmp/torchinductor
# wandb is a hard dependency; keep it offline unless the user opts in (WANDB_MODE=online).
ENV WANDB_MODE=offline

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# muvit requires Python 3.11-3.13 (not in Ubuntu 22.04 apt) - use a uv-managed interpreter.
RUN uv python install 3.12 && \
    uv venv "${VENV_PATH}" --python 3.12

# torch 2.5.1 is the newest cu121 build (x-transformers' deps need torch >= 2.5).
RUN uv pip install --no-cache \
        torch==2.5.1 torchvision==0.20.1 \
        --index-url https://download.pytorch.org/whl/cu121

# muvit leaves its deps unpinned and imports x-transformers internals
# (x_transformers.x_transformers.Attention/FeedForward/RotaryEmbedding), so pin
# x-transformers to the release current when muvit 0.1.0 was published (2026-02-28).
RUN uv pip install --no-cache \
        "muvit==${MUVIT_VERSION}" \
        x-transformers==2.16.1 \
        jupyterlab ipykernel papermill && \
    python -c "import muvit, torch, lightning; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
