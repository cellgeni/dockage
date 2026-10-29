# TACCO - Transfer of Annotations to Cells and their COmbinations
# https://github.com/simonwm/tacco
# Annotation transfer / compositional deconvolution of single-cell and spatial omics data (CPU, MKL-accelerated).
FROM python:3.12-slim

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

ARG TACCO_VERSION=0.5.0

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
# pip-installed MKL (needed by sparse_dot_mkl) puts libmkl_rt.so.* into the venv lib dir
ENV LD_LIBRARY_PATH="${VENV_PATH}/lib"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.12

RUN uv pip install --no-cache \
      "tacco==${TACCO_VERSION}" \
      jupyterlab ipykernel papermill

RUN python -c "import tacco, importlib.metadata as m; print('tacco', m.version('tacco'))"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
