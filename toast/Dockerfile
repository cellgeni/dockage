# TOAST - https://github.com/cecca46/TOAST
# Topography-aware Optimal Transport for alignment of spatial omics slices
# (Python API `spatial_OT` + `toast` CLI).
FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp

# Latest release tag (no PyPI release; package name `toast-spatial-ot`)
ARG TOAST_TAG="v1.1.2"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.11

RUN git clone https://github.com/cecca46/TOAST.git /opt/TOAST && \
    cd /opt/TOAST && \
    git checkout "${TOAST_TAG}"

# requirements.txt is the upstream pinned environment (numpy 2.1, scanpy 1.11, POT 0.9.5, ...)
RUN uv pip install --no-cache -r /opt/TOAST/requirements.txt && \
    uv pip install --no-cache /opt/TOAST && \
    uv pip install --no-cache jupyterlab ipykernel papermill

RUN python -c "import spatial_OT; from spatial_OT import align_anndata, align_csv" && toast --help

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
