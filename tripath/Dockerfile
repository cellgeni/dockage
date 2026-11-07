# TriPath - https://github.com/mahmoodlab/TriPath
# Weakly-supervised deep learning on 3D pathology volumes (OTLS / microCT):
# 3D tissue segmentation & patching, feature extraction, MIL training/inference.
# Script-based repo (no package): code lives in /opt/TriPath, run e.g.
#   python /opt/TriPath/extract_features.py ...  (cd /opt/TriPath/preprocess for patching)
# Licence: CC BY-NC-ND 4.0 (non-commercial academic use).
# Pretrained encoder weights (timm / torchvision / pytorchvideo) are fetched at runtime.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG TRIPATH_COMMIT="76e30b5f20cf3811e6b7de1bcdc2cbf1166edc78"

LABEL org.opencontainers.image.source="https://github.com/mahmoodlab/TriPath"

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
ENV PYTHONPATH="/opt/TriPath"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      python3.10 python3.10-dev python3.10-venv \
      libopenslide0 libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python 3.10: the pinned requirements (pandas 1.4.3, h5py 3.9.0, scikit-survival 0.21.0,
# torch 2.0.1) have no wheels beyond 3.10/3.11.
RUN uv venv ${VENV_PATH} --python python3.10

RUN git clone https://github.com/mahmoodlab/TriPath.git /opt/TriPath && \
    cd /opt/TriPath && \
    git checkout "${TRIPATH_COMMIT}"

# Upstream requirements.txt is fully pinned (torch 2.0.1 from PyPI bundles CUDA 11.7 libs).
# numpy<2 added because pandas 1.4.3 / scikit-survival 0.21 are built against numpy 1.x.
RUN uv pip install --no-cache \
      -r /opt/TriPath/requirements.txt \
      "numpy<2" \
      setuptools \
      jupyterlab papermill

RUN python -c "import torch, monai, openslide, sksurv, pytorchvideo; print('torch', torch.__version__)" && \
    chmod -R a+rX /opt/TriPath

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
