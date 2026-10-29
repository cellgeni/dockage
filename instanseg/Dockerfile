# InstanSeg - https://github.com/instanseg/instanseg
# PyTorch cell and nucleus instance segmentation for fluorescence and brightfield
# (incl. whole-slide) microscopy images. Python API + `inference` CLI.
# Pretrained models (e.g. "fluorescence_nuclei_and_cells", "brightfield_nuclei") are
# downloaded from GitHub releases on first use (cached under INSTANSEG_BIOIMAGEIO_PATH).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG INSTANSEG_VERSION="0.1.2"

LABEL org.opencontainers.image.source="https://github.com/instanseg/instanseg"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_PREFERENCE=only-system
ENV MPLCONFIGDIR=/tmp
# Defaults point inside site-packages (read-only under Singularity); override with a
# mounted path to keep downloaded models between runs.
ENV INSTANSEG_BIOIMAGEIO_PATH=/tmp/instanseg/bioimageio_models
ENV INSTANSEG_TORCHSCRIPT_PATH=/tmp/instanseg/torchscripts
ENV INSTANSEG_MODEL_PATH=/tmp/instanseg/models

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      python3.10 python3.10-dev python3.10-venv \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.10

# torch 2.5.1 is the last release with cu121 wheels.
RUN uv pip install --no-cache \
      torch==2.5.1+cu121 \
      torchvision==0.20.1+cu121 \
      --extra-index-url https://download.pytorch.org/whl/cu121

# [io] extra: bioio/ome-tiff, tiffslide, slideio, rasterio, geojson for WSI and
# OME-TIFF reading + GeoJSON export. The [full] (training) extra is not installed:
# it pulls tkinterdnd2, tensorboard, hyperopt and an unqualified `cucim` package.
RUN uv pip install --no-cache \
      "torch==2.5.1+cu121" "torchvision==0.20.1+cu121" \
      "instanseg-torch[io]==${INSTANSEG_VERSION}" \
      jupyterlab ipykernel papermill ipywidgets \
      --extra-index-url https://download.pytorch.org/whl/cu121 \
      --index-strategy unsafe-best-match

RUN python -c "from instanseg import InstanSeg; import torch; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
