# SAFAARI - https://github.com/VafaeeLab/SAFAARI
# Single-cell Annotation and Fusion with Adversarial open-set domain Adaptation:
# label transfer / novel cell-type detection and cross-modality integration.
# CLIs: safaari-unsupervised, safaari-supervised_integration.
# No PyPI release / tags: pinned to a git commit. The scripts read and write
# relative paths (data/FACS10X/..., data/results/...), so run them from a working
# directory that contains your `data/` folder (example Tabula Muris data is in /opt/SAFAARI/data).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG SAFAARI_COMMIT="af1febe55bb5b7dcb8947b40e63c3a8a1f4f0eab"

LABEL org.opencontainers.image.source="https://github.com/VafaeeLab/SAFAARI"

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
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python 3.10: pinned requirements (torch 2.0.0, numpy 1.24.2, pandas 1.5.3,
# scikit-learn 1.2.2, scipy 1.10.1) have wheels only up to 3.11.
RUN uv venv ${VENV_PATH} --python python3.10

RUN git clone https://github.com/VafaeeLab/SAFAARI.git /opt/SAFAARI && \
    cd /opt/SAFAARI && \
    git checkout "${SAFAARI_COMMIT}" && \
    rm -rf build dist SAFAARI.egg-info __pycache__ */__pycache__

# requirements.txt uses the `imblearn==0.0` shim (unpinned imbalanced-learn); pin the
# real package to a release compatible with scikit-learn 1.2.2.
# torch 2.0.0 from PyPI bundles its own CUDA 11.7 runtime.
# Editable install: the package's top-level modules are named `models` and `scripts`.
RUN uv pip install --no-cache \
      -r /opt/SAFAARI/requirements.txt \
      "imbalanced-learn==0.12.4" \
      -e /opt/SAFAARI \
      jupyterlab ipykernel papermill

RUN python -c "import torch, imblearn; from models.SAFAARI import SAFAARIModel; print('torch', torch.__version__)" && \
    chmod -R a+rX /opt/SAFAARI

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
