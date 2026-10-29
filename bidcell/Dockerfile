# BIDCell - https://github.com/SydneyBioX/BIDCell
# Biologically-informed self-supervised deep learning for cell segmentation of
# subcellular spatial transcriptomics (Xenium, CosMx, MERSCOPE, Stereo-seq).
# Upstream recommends a GPU with >=12 GB VRAM.
# Cellpose "cyto" weights (nuclei step) and segmentation-models-pytorch encoder
# weights are downloaded at runtime (set CELLPOSE_LOCAL_MODELS_PATH / TORCH_HOME to
# a mounted dir to cache them).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG BIDCELL_VERSION="1.0.3"

LABEL org.opencontainers.image.source="https://github.com/SydneyBioX/BIDCell"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
ENV CELLPOSE_LOCAL_MODELS_PATH=/tmp/cellpose_models
ENV TORCH_HOME=/tmp/torch

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      python3.10 python3.10-dev python3.10-venv \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upstream README uses Python 3.10 (supports >=3.9,<3.13).
RUN uv venv ${VENV_PATH} --python python3.10

RUN uv pip install --no-cache \
      torch==2.1.2+cu121 \
      torchvision==0.16.2+cu121 \
      --extra-index-url https://download.pytorch.org/whl/cu121

# Key versions follow upstream pdm.lock: bidcell uses cellpose's `models.Cellpose`
# class (removed in cellpose 4) and imgaug 0.4.0 (breaks with numpy 2), and
# segmentation-models-pytorch 0.3.3 pins timm==0.9.2.
RUN uv pip install --no-cache \
      "torch==2.1.2+cu121" "torchvision==0.16.2+cu121" \
      "bidcell==${BIDCELL_VERSION}" \
      "numpy==1.24.4" \
      "cellpose==2.2.3" \
      "segmentation-models-pytorch==0.3.3" \
      "timm==0.9.2" \
      "imgaug==0.4.0" \
      "pandas==2.1.0" \
      "scipy==1.11.2" \
      "scikit-image==0.21.0" \
      "opencv-python==4.8.0.76" \
      "tifffile==2023.8.30" \
      "h5py==3.9.0" \
      "pydantic==2.3.0" \
      "matplotlib==3.7.2" \
      jupyterlab ipykernel papermill \
      --extra-index-url https://download.pytorch.org/whl/cu121 \
      --index-strategy unsafe-best-match

RUN python -c "from bidcell import BIDCellModel; import torch, cellpose; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
