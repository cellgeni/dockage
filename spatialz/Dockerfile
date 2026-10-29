# SpatialZ - https://github.com/senlin-lin/SpatialZ (docs: https://spatialz-tutorial.readthedocs.io)
# Builds dense 3D spatial transcriptomics atlases by synthesising virtual slices between
# measured 2D sections (optimal-transport based, torch-accelerated).
# SpatialZ is not a package: SpatialZ.py / Synthesize.py are cloned to /opt/SpatialZ and put on PYTHONPATH.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# No release tags upstream - pin a commit.
ARG SPATIALZ_COMMIT="e1b5ed01e933729149e08399febca08db16ced14"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
ENV PYTHONPATH="/opt/SpatialZ"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# libgl1/libgomp1/libx11-6 etc. are needed at import time by open3d.
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
        libgl1 libegl1 libgomp1 libglib2.0-0 libx11-6 libusb-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upstream targets Python 3.9.19 (not in Ubuntu 22.04 apt) - use a uv-managed interpreter.
RUN uv python install 3.9 && \
    uv venv "${VENV_PATH}" --python 3.9

# torch pinned as upstream (1.13.0+cu117 wheels bundle their own CUDA libs and run on
# current drivers); remaining pins taken from upstream requirements.txt / Dockerfile.
RUN uv pip install --no-cache \
        torch==1.13.0+cu117 \
        --extra-index-url https://download.pytorch.org/whl/cu117 \
        --index-strategy unsafe-best-match

RUN uv pip install --no-cache \
        numpy==1.22.2 \
        pandas==2.0.0 \
        anndata==0.9.1 \
        scikit-learn==1.2.2 \
        scipy==1.10.1 \
        pot==0.9.3 \
        SOMENDER==1.1 \
        open3d==0.18.0 \
        scanpy==1.9.3 \
        squidpy==1.2.3 \
        palettable scikit-misc plotly matplotlib tqdm \
        jupyterlab ipykernel papermill

RUN git clone https://github.com/senlin-lin/SpatialZ.git /opt/SpatialZ && \
    cd /opt/SpatialZ && git checkout "${SPATIALZ_COMMIT}" && \
    chmod -R 755 /opt/SpatialZ && \
    python -c "import torch, ot, MENDER, SpatialZ; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
