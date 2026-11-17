# HESCAPE - benchmark for cross-modal learning of histology and spatial gene expression
# https://github.com/peng-lab/hescape  (paper: https://arxiv.org/abs/2508.01490)
# CLIP-style contrastive pretraining of H&E image encoders and gene-expression encoders on Xenium data (PyTorch Lightning + Hydra, GPU).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

# No PyPI release / tags upstream: pin the latest main commit
ARG HESCAPE_COMMIT="bd5470480594f1b11d21633e11aaaffe2cfbd4d4"
ARG CONCH_COMMIT="141cc09c7d4ff33d8eda562bd75169b457f71a62"

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

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# hescape requires python >=3.10,<3.13
RUN uv venv ${VENV_PATH} --python 3.12

RUN git clone https://github.com/peng-lab/hescape.git /opt/hescape && \
    cd /opt/hescape && \
    git checkout "${HESCAPE_COMMIT}"

# Notes on deviations from upstream pyproject:
#  * --no-sources: [tool.uv.sources] points drvi-py at a theislab/drvi branch
#    ("update-scvi-version") that no longer exists; use the PyPI release that
#    contains that work instead (drvi-py 0.2.0, scvi-tools <1.4.1).
#  * "conch" on PyPI is an unrelated package (Twisted Conch), so CONCH is
#    installed explicitly from mahmoodlab/CONCH at a pinned commit.
#  * scib-metrics and pytorch-lightning are imported by hescape but not declared.
#  * transformers<5 to stay in the API range current when hescape was released.
# torch pinned in the same resolve so it is not upgraded to a non-cu121 build.
RUN uv pip install --no-cache --no-sources --torch-backend=cu121 \
      torch==2.5.1 torchvision==0.20.1 \
      "conch @ git+https://github.com/mahmoodlab/CONCH.git@${CONCH_COMMIT}" \
      drvi-py==0.2.0 \
      "transformers<5" \
      scib-metrics \
      pytorch-lightning \
      -e /opt/hescape \
      jupyterlab ipykernel papermill

# Pretrained encoder weights (UNI, CONCH, GigaPath, ... - several are gated on Hugging Face)
# and the Peng-AI/hescape-pyarrow dataset are NOT baked in; they are fetched at runtime
# (set HF_TOKEN / HF_HOME). Training entry point: /opt/hescape/experiments/hescape_pretrain/train.py
RUN python -c "import hescape, drvi, torch; from conch.open_clip_custom import create_model_from_pretrained; print('hescape OK, torch', torch.__version__)"

WORKDIR /opt/hescape

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
