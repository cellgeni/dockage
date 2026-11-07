# OmiCLIP / Loki - https://github.com/GuangyuWangLab2021/Loki
# (paper: https://www.nature.com/articles/s41592-025-02707-1)
# OmiCLIP visual-omics foundation model (H&E <-> transcriptomics, open_clip based) and the Loki
# platform: tissue alignment, cell-type decomposition, tissue annotation, ST expression
# prediction from H&E, and image-transcriptomics retrieval.
#
# Pretrained OmiCLIP weights are NOT baked in; download from Hugging Face
# (https://huggingface.co/WangGuangyuLab/Loki) and pass the checkpoint path to loki.utils.load_model.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

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
ENV HF_HOME=/tmp/hf_home

# No releases upstream (package `loki` 0.0.1 in src/); pin commit
ARG LOKI_COMMIT="c6d3eed94dc18c5c19a10120828578d5a09d5347"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      python3.10 python3.10-dev python3.10-venv \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# upstream uses python 3.9; numpy==1.25.0 has py3.10 wheels, so use the system python 3.10
RUN uv venv ${VENV_PATH} --python python3.10

# torch/torchvision pinned by upstream setup.py (2.3.1 / 0.18.1) - use the CUDA 12.1 builds
RUN uv pip install --no-cache \
      torch==2.3.1+cu121 torchvision==0.18.1+cu121 \
      --extra-index-url https://download.pytorch.org/whl/cu121

# Only src/ is the package; fetch the tarball of the pinned commit (repo .git is ~0.5 GB)
RUN mkdir -p /opt/Loki && \
    curl -fsSL "https://github.com/GuangyuWangLab2021/Loki/archive/${LOKI_COMMIT}.tar.gz" \
      | tar -xz -C /opt/Loki --strip-components=1 && \
    rm -rf /opt/Loki/src/build /opt/Loki/src/dist /opt/Loki/src/loki.egg-info

# setup.py pins (anndata 0.10.9, numpy 1.25.0, pandas 2.2.3, open_clip_torch 2.26.1, tangram-sc 1.0.4,
# pycpd 2.0.0, ...). scanpy and scikit-learn are imported but not declared upstream.
RUN uv pip install --no-cache /opt/Loki/src \
      "scanpy==1.10.3" scikit-learn \
      jupyterlab ipykernel papermill

RUN python -c "import torch, open_clip, loki.utils, loki.preprocess, loki.align, loki.annotate, loki.decompose, loki.retrieve, loki.predex, loki.plot; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
