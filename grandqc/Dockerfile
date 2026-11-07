# GrandQC - https://github.com/cpath-ukk/grandqc
# Tissue and multi-class artifact segmentation (folds, pen marks, bubbles, out-of-focus, ...)
# for quality control of H&E whole-slide images (PyTorch, segmentation_models_pytorch).
#
# Usage (scripts use ./models relative to the script folder, so cd first):
#   cd /opt/grandqc/01_WSI_inference_OPENSLIDE_QC     # .svs/.ndpi/.tiff via OpenSlide
#   cd /opt/grandqc/02_WSI_inference_OME_TIFF_QC      # OME-TIFF
#   python wsi_tis_detect.py --slide_folder <in> --output_dir <out>
#   python main.py --slide_folder <in> --output_dir <out> --mpp_model 1.5 --create_geojson Y
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
# timm-efficientnet-b0 ImageNet encoder weights are cached here at build time
ENV TORCH_HOME=/opt/torch

# No releases upstream; pin commit
ARG GRANDQC_COMMIT="002688d74a4ac86dfbb816a96df8461d6080f88a"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git wget curl ca-certificates build-essential \
      python3.10 python3.10-dev python3.10-venv \
      libopenslide0 libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.10

RUN git clone https://github.com/cpath-ukk/grandqc.git /opt/grandqc && \
    cd /opt/grandqc && \
    git checkout "${GRANDQC_COMMIT}"

# torch 2.0.1 as pinned upstream (CUDA 11.8 wheels bundle their own CUDA runtime)
RUN uv pip install --no-cache \
      torch==2.0.1+cu118 torchvision==0.15.2+cu118 \
      --index-url https://download.pytorch.org/whl/cu118

# upstream requirements.txt (torch already satisfied) + OpenSlide bindings (upstream uses conda for these)
RUN uv pip install --no-cache -r /opt/grandqc/requirements.txt && \
    uv pip install --no-cache "openslide-python==1.4.1" && \
    uv pip install --no-cache jupyterlab ipykernel papermill

# Model checkpoints (~100 MB total, Zenodo). The scripts hard-code ./models/{td,qc}/,
# so they are required to run anything; download once and share between both script folders.
#   Tissue:   https://zenodo.org/records/14507273
#   Artifact: https://zenodo.org/records/14041538
RUN mkdir -p /opt/grandqc/models/td /opt/grandqc/models/qc && \
    wget -q -O /opt/grandqc/models/td/Tissue_Detection_MPP10.pth \
        "https://zenodo.org/records/14507273/files/Tissue_Detection_MPP10.pth?download=1" && \
    for m in GrandQC_MPP1.pth GrandQC_MPP15.pth GrandQC_MPP2.pth; do \
        wget -q -O /opt/grandqc/models/qc/${m} "https://zenodo.org/records/14041538/files/${m}?download=1"; \
    done && \
    ln -s /opt/grandqc/models /opt/grandqc/01_WSI_inference_OPENSLIDE_QC/models && \
    ln -s /opt/grandqc/models /opt/grandqc/02_WSI_inference_OME_TIFF_QC/models

# The tissue-detection script builds smp.UnetPlusPlus(encoder_weights="imagenet"), which
# downloads the timm-efficientnet-b0 ImageNet weights; cache them so it runs offline.
RUN python -c "import segmentation_models_pytorch as smp; smp.UnetPlusPlus(encoder_name='timm-efficientnet-b0', encoder_weights='imagenet', classes=2, activation=None)" && \
    chmod -R a+rX ${TORCH_HOME}

RUN python -c "import torch, openslide, segmentation_models_pytorch, rasterio, zarr; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
