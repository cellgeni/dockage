# LazySlide - https://github.com/rendeirolab/LazySlide
# Whole-slide image (WSI) analysis framework: tissue detection, tiling, pathology foundation
# model features, cell segmentation, vision-language models; results stored as SpatialData.
#
# Foundation-model weights are NOT baked in: they are downloaded on first use from
# Hugging Face into $HF_HOME (many are gated - set HF_TOKEN). Mount/override HF_HOME
# to a persistent location on the cluster.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
ENV HF_HOME=/tmp/hf_home
ENV JAVA_HOME=/usr/lib/jvm/default-java

ARG LAZYSLIDE_VERSION="0.13.0"

# default-jre-headless: Bio-Formats reader via scyjava (wsidata[bioformats])
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      libgl1 libglib2.0-0 libgomp1 default-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# LazySlide requires Python >= 3.11 (uv-managed interpreter; Ubuntu 22.04 ships 3.10)
RUN uv venv ${VENV_PATH} --python 3.12

# torch first from the CUDA 12.1 index, then everything else from PyPI
RUN uv pip install --no-cache \
      torch==2.5.1 torchvision==0.20.1 \
      --index-url https://download.pytorch.org/whl/cu121

# extras: all (scanpy, igraph) + models (transformers, open_clip, ...) + extra slide readers.
# Constrain torch so the resolver cannot swap in a newer PyPI (CUDA 13) build.
RUN echo -e "torch==2.5.1\ntorchvision==0.20.1" > /tmp/torch-constraints.txt && \
    uv pip install --no-cache --constraint /tmp/torch-constraints.txt \
      "lazyslide[all,models]==${LAZYSLIDE_VERSION}" \
      "wsidata[bioformats,tiffslide,stain,plot]" \
      spatialdata-plot marsilea \
      jupyterlab ipykernel ipywidgets papermill

RUN python -c "import importlib.metadata as m, torch, lazyslide, wsidata; print('lazyslide', m.version('lazyslide'), 'torch', torch.__version__, 'cuda', torch.version.cuda)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
