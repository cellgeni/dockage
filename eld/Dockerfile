# ELD (Effortless Landmark Detection) - https://github.com/ekvall93/ELD
# Unsupervised deep-learning landmark detection for tissue images, used for
# 2D / 3D / multimodal tissue registration (eld-train CLI + Python API).
# No PyPI release / tags: pinned to a git commit.
# The FAN init checkpoint (checkpoint_fansoft/fan_109.pth, ~25 MB) ships in the repo;
# eld-train's default --checkpoint is the relative path checkpoint_fansoft/fan_109.pth,
# so either run from /opt/ELD or pass --checkpoint /opt/ELD/checkpoint_fansoft/fan_109.pth.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG ELD_COMMIT="79ba97bd948ff3b03ee9d76ab957184f899d62ee"

LABEL org.opencontainers.image.source="https://github.com/ekvall93/ELD"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV MPLCONFIGDIR=/tmp

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upstream docs require torch==1.9.0 / torchvision==0.10.0 (CUDA 11.1 wheels bundle
# their own CUDA runtime); those wheels only exist up to Python 3.9.
RUN uv venv ${VENV_PATH} --python 3.9

RUN git clone https://github.com/ekvall93/ELD.git /opt/ELD && \
    cd /opt/ELD && \
    git checkout "${ELD_COMMIT}"

# setup.py reads requirements.txt (torch unpinned, numpy<2, kornia 0.6.2, piqa 1.2.2,
# torchgeometry 0.1.2, tifffile 2020.9.3, opencv 4.6.0.66, torchnet 0.0.4...).
# visdom (needed by torchnet's loggers in eld-train) pinned to the last py3.9 release.
RUN uv pip install --no-cache \
      "torch==1.9.0+cu111" \
      "torchvision==0.10.0+cu111" \
      "torchaudio==0.9.0" \
      "visdom==0.2.4" \
      -e /opt/ELD \
      jupyterlab ipykernel papermill \
      --find-links https://download.pytorch.org/whl/torch_stable.html \
      --index-strategy unsafe-best-match

RUN python -c "import torch, kornia, ELD.model; print('torch', torch.__version__)" && \
    chmod -R a+rX /opt/ELD

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
