# Pycytominer - https://github.com/cytomining/pycytominer
# Python functions for processing image-based (Cell Painting) morphological profiling data
# (aggregate, annotate, normalize, feature_select, consensus).
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system

ARG PYCYTOMINER_VERSION="1.7.1"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.12

# extras: anndata (AnnData output), cell-locations (S3 cell location lookup)
RUN uv pip install --no-cache \
      "pycytominer[anndata,cell-locations]==${PYCYTOMINER_VERSION}" \
      jupyterlab ipykernel papermill

RUN python -c "import importlib.metadata as m, pycytominer; print('pycytominer', m.version('pycytominer'))"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
