# Slideflow - deep learning library for digital histopathology
# https://github.com/slideflow/slideflow
# WSI tile extraction, stain normalisation, model training / MIL / foundation-model feature extraction (PyTorch backend, GPU).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

ARG SLIDEFLOW_VERSION=3.0.2

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
# PyTorch backend; read slides with libvips (cuCIM/cupy not installed)
ENV SF_BACKEND=torch
ENV SF_SLIDE_BACKEND=libvips

# libvips (Ubuntu 22.04 ships 8.12, slideflow needs >=8.9, built with openslide support)
# swig + build-essential are needed to build pyrfr (dependency of smac==1.4.0)
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git wget ca-certificates build-essential swig \
      python3.10 python3.10-dev \
      libvips-dev openslide-tools libopenslide0 \
      libgl1 libglib2.0-0 libsm6 libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.10

# Pins follow upstream torch.Dockerfile (torch 2.3.1) and environment.yml
# (ConfigSpace 0.6.0 for smac 1.4.0, zarr 2.x, numpy 1.x).
# slideflow-gpl / slideflow-noncommercial add extra pretrained models (UNI, CTransPath, CLAM, ...);
# their weights are downloaded on first use, not at build time.
RUN uv pip install --no-cache --torch-backend=cu121 \
      torch==2.3.1 torchvision==0.18.1 \
      "numpy<2" \
      "ConfigSpace==0.6.0" \
      "zarr<3" \
      "slideflow[torch]==${SLIDEFLOW_VERSION}" \
      slideflow-gpl==0.0.2 \
      slideflow-noncommercial==0.0.2 \
      jupyterlab ipykernel papermill

RUN python -c "import slideflow as sf, torch; print('slideflow', sf.__version__, 'backend', sf.backend(), 'torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
