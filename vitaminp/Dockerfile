# VitaminP - https://github.com/idso-fa1-pathology/VitaminP
# ViT-based whole-cell / nucleus segmentation for H&E and multiplex IF whole-slide images.
# Pretrained weights (yasinmdanderson/vitaminp-weights on Hugging Face) are NOT baked in:
# vitaminp.load_model() downloads them to ~/.cache/vitaminp on first use.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG VITAMINP_VERSION="0.3.2"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    HDF5_USE_FILE_LOCKING=FALSE \
    NUMBA_CACHE_DIR=/tmp

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
        libgl1 libglib2.0-0 libgeos-dev libgomp1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python 3.11

# torch for CUDA 12.1 (upstream image uses torch 2.1 / cu121)
RUN uv pip install \
        torch==2.4.1 torchvision==0.19.1 \
        --index-url https://download.pytorch.org/whl/cu121

# vitaminp[wsi] + the extra runtime imports used by the package that are not declared
# in setup.py (cv2, skimage, timm, zarr, cupy, wandb, huggingface_hub).
# numpy<2 as recommended upstream (OpenCV / NumPy 2 conflict).
RUN uv pip install \
        "vitaminp[wsi]==${VITAMINP_VERSION}" \
        "numpy<2" \
        opencv-python-headless==4.9.0.80 \
        scikit-image==0.22.0 \
        timm==0.9.16 \
        "zarr<3" numcodecs \
        imagecodecs \
        openslide-bin \
        huggingface-hub \
        cupy-cuda12x \
        wandb \
        jupyterlab ipykernel papermill

RUN python -c "import torch, vitaminp, cv2, openslide; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
