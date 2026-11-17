# DISSECT - https://github.com/zenglab-pku/DISSECT (PyPI: dissect-st)
# Diffusion-based cell segmentation integrating spatially resolved transcriptomics
# (Xenium, Stereo-seq, CosMx, Visium HD): diffusion-model (detectron2) nucleus/membrane
# detection refined with transcript gradient fields.
#
# Model weights are NOT baked in (Google Drive only):
#   https://drive.google.com/file/d/1Y9_YCJzhUPEQBDAdKVyrKplI1vpD4qiO/view
# Pass them via dissect.segmentation(..., weights_file=...). The upstream model config is
# copied to /opt/dissect/config.yaml (config_file=...).
#
# -devel base: detectron2 compiles CUDA extensions.
FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

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
# build detectron2 CUDA ops for common HPC GPUs (V100, T4, A100, A10/RTX30, L4/L40, H100)
ENV FORCE_CUDA=1
ENV TORCH_CUDA_ARCH_LIST="7.0;7.5;8.0;8.6;8.9;9.0"

ARG DISSECT_VERSION="0.5.4"
# repo commit matching the 0.5.4 release (used only for config.yaml)
ARG DISSECT_COMMIT="b75071ac66f6fb238e049f14c2a0e59661be1c40"
# detectron2 has no recent releases; pin a commit
ARG DETECTRON2_COMMIT="247691a1c292654867deb35cabb27f18d75a1363"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential ninja-build \
      python3.10 python3.10-dev python3.10-venv \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# dissect-st needs anndata>=0.11.3 / scikit-image>=0.25.2 -> Python >= 3.10
RUN uv venv ${VENV_PATH} --python python3.10

# README: torch/torchvision from the CUDA 12.1 index
RUN uv pip install --no-cache \
      torch==2.3.1+cu121 torchvision==0.18.1+cu121 \
      --extra-index-url https://download.pytorch.org/whl/cu121 && \
    echo -e "torch==2.3.1\ntorchvision==0.18.1" > /opt/torch-constraints.txt

# detectron2 from source against the installed torch
RUN uv pip install --no-cache setuptools wheel ninja && \
    git clone https://github.com/facebookresearch/detectron2.git /opt/detectron2 && \
    cd /opt/detectron2 && \
    git checkout "${DETECTRON2_COMMIT}" && \
    uv pip install --no-cache --no-build-isolation --constraint /opt/torch-constraints.txt /opt/detectron2

# dissect-st's PyPI metadata omits most runtime deps; add the ones imported by the package
# (environment.yml + imports: fvcore, timm, shapely, numba, psutil, opencv, joblib, polars)
RUN uv pip install --no-cache --constraint /opt/torch-constraints.txt \
      "dissect-st==${DISSECT_VERSION}" \
      fvcore timm shapely numba psutil joblib polars tifffile opencv-python-headless tqdm \
      jupyterlab ipykernel papermill

RUN mkdir -p /opt/dissect && \
    curl -fsSL -o /opt/dissect/config.yaml \
      "https://raw.githubusercontent.com/zenglab-pku/DISSECT/${DISSECT_COMMIT}/config.yaml"

RUN python -c "import torch, detectron2, dissect; from dissect import segmentation; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
