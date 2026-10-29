# DELiVR - VR-enabled, deep-learning based cFos (and microglia) inference pipeline for whole mouse brains
# https://github.com/erturklab/delivr_cfos  (paper: https://www.nature.com/articles/s41592-024-02245-2)
# Light-sheet brain volumes -> masking (ilastik) -> 3D U-Net cell detection (MONAI/PyTorch, GPU)
# -> atlas alignment (mBrainAligner) -> Allen CCF3 region assignment -> visualisation.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

# No releases upstream: pin the latest master commit
ARG DELIVR_COMMIT="51ef796da883ace0afbbf589630b0e756dd3c6d3"
# ilastik version used in the paper / upstream Docker image
ARG ILASTIK_VERSION="1.4.0b8"

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

# System libs follow upstream misc_files/Dockerfile; git-lfs is needed for the model/atlas files
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git git-lfs wget ca-certificates bzip2 build-essential \
      python3.10 python3.10-dev \
      ffmpeg libsm6 libxext6 libgl1 libglib2.0-0 libtiff5 libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.10

# Clone to /delivr so the default config.json paths (/delivr/ilastik/, ./models/...) work.
# models/ holds the U-Net weights (inference_weights.tar), ilastik random-forest project and
# the Allen CCF3 annotation (~150 MB, git-lfs) - they are part of the pipeline, so they are pulled here.
RUN git lfs install --system && \
    git clone https://github.com/erturklab/delivr_cfos.git /delivr && \
    cd /delivr && \
    git checkout "${DELIVR_COMMIT}" && \
    git lfs pull && \
    rm -rf .git

# Upstream pins (requirements.txt, torch 2.0.1+cu117 wheels bundle their own CUDA runtime)
# plus the extras installed in upstream's Dockerfile (more-itertools, imagecodecs, matplotlib).
# statsmodels for statistics/; brainrender (visualisation script) is not installed.
RUN sed -i '/--find-links/d' /delivr/requirements.txt && \
    uv pip install --no-cache --torch-backend=cu117 \
      -r /delivr/requirements.txt \
      more-itertools \
      imagecodecs==2023.3.16 \
      matplotlib \
      statsmodels \
      jupyterlab ipykernel papermill

# ilastik (used for ventricle/artifact masking)
RUN mkdir -p /delivr/ilastik && \
    wget -q -O /tmp/ilastik.tar.bz2 "https://files.ilastik.org/ilastik-${ILASTIK_VERSION}-Linux.tar.bz2" && \
    tar -xjf /tmp/ilastik.tar.bz2 -C /delivr/ilastik --strip-components=1 && \
    rm /tmp/ilastik.tar.bz2

# NOT included (no scriptable download / Windows-only parts):
#  * TeraConverter (TeraStitcher-portable 1.11.10, SharePoint download) -> mount at /delivr/teraconverter/
#  * mBrainAligner + its Linux libs (Google Drive) -> mount and set atlas_alignment.mBrainAligner_location
# Run: cd /delivr && python __main__.py /path/to/config.json  (copy and edit /delivr/config.json)
ENV PYTHONPATH="/delivr"
WORKDIR /delivr

RUN python -c "import torch, monai, pytorch_lightning, cc3d, tifffile; print('torch', torch.__version__, 'monai', monai.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
