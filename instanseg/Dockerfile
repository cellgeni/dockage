# InstanSeg - https://github.com/instanseg/instanseg
# PyTorch cell and nucleus instance segmentation for fluorescence and brightfield
# (incl. whole-slide) microscopy images. Python API + `inference` CLI.
# Pretrained models (e.g. "fluorescence_nuclei_and_cells", "brightfield_nuclei") are
# downloaded from GitHub releases on first use (cached under INSTANSEG_BIOIMAGEIO_PATH,
# default ~/.cache/instanseg/bioimageio_models - see the .pth hook below).
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

# InstanSeg's INSTANSEG_{BIOIMAGEIO,TORCHSCRIPT,MODEL}_PATH defaults point inside
# site-packages (read-only under Singularity). Fixed /tmp paths are unsafe on shared hosts
# (Singularity binds the host /tmp: cross-user ownership clashes, and a cached instanseg.pt
# is loaded unverified). This .pth hook runs at interpreter start-up and, only for variables
# the user has not set, defaults them to the per-user ${XDG_CACHE_HOME:-~/.cache}/instanseg/.
COPY instanseg_user_paths.pth ${VENV_PATH}/lib/python3.10/site-packages/
RUN python -c "import os; p = os.environ['INSTANSEG_MODEL_PATH']; assert p.startswith(os.path.expanduser('~')), p; print(p)" && \
    INSTANSEG_MODEL_PATH=/custom python -c "import os; assert os.environ['INSTANSEG_MODEL_PATH'] == '/custom'"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
