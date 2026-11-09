# Cellpin - https://cellpin.readthedocs.io (source: https://github.com/Saur-Lab/cellpin)
# Probabilistic model (PyTorch) for reference-based imputation and denoising of spatial
# transcriptomes from scRNA-seq, plus atlas-to-spatial label transfer.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG CELLPIN_VERSION="0.3.0"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    NUMBA_CACHE_DIR=/tmp \
    HDF5_USE_FILE_LOCKING=FALSE

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# cellpin requires Python >= 3.11
RUN uv venv "${VENV_PATH}" --python 3.12

# cellpin requires torch>=2.9.1; there is no cu121 build of that, so use the cu126 wheels
# (bundle their own CUDA 12.6 runtime; need a driver supporting CUDA 12.x).
RUN uv pip install \
        torch==2.9.1 \
        --index-url https://download.pytorch.org/whl/cu126

RUN uv pip install \
        "cellpin[spatial]==${CELLPIN_VERSION}" \
        jupyterlab ipykernel papermill

RUN python -c "import cellpin, torch; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
