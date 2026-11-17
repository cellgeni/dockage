# TIAToolbox - computational pathology toolbox
# https://github.com/TissueImageAnalytics/tiatoolbox  (docs: https://tia-toolbox.readthedocs.io)
# WSI reading, stain normalisation, tiling, and deep-learning models (nucleus segmentation, patch classification, foundation-model features) (PyTorch, GPU).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

ARG TIATOOLBOX_VERSION=2.1.3

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

# libgl1/libglib2.0-0 for opencv-python; openslide comes from the openslide-bin wheel
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git ca-certificates \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# tiatoolbox 2.1.x requires python >= 3.11 and torch >= 2.5
RUN uv venv ${VENV_PATH} --python 3.12

# torch pinned in the same resolve so it is not upgraded to a non-cu121 build.
# Pretrained model weights are downloaded on first use (to ~/.tiatoolbox or TIATOOLBOX_HOME), not at build time.
RUN uv pip install --no-cache --torch-backend=cu121 \
      torch==2.5.1 torchvision==0.20.1 \
      "tiatoolbox==${TIATOOLBOX_VERSION}" \
      jupyterlab ipykernel papermill

RUN tiatoolbox --help > /dev/null && \
    python -c "import tiatoolbox, torch, importlib.metadata as m; print('tiatoolbox', m.version('tiatoolbox'), 'torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
