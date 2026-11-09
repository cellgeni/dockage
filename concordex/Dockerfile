# concordex - https://github.com/pachterlab/concordex
# kNN-graph based identification of spatial homogeneous regions (SHRs) and
# assessment of clustering concordance (Jackson et al., 2024). Python implementation
# (an R/Bioconductor version also exists; this image uses the Python package on AnnData).
FROM python:3.11-slim

ARG CONCORDEX_VERSION="2.0.0"

LABEL org.opencontainers.image.source="https://github.com/pachterlab/concordex"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python /usr/local/bin/python3.11

# concordex itself only needs anndata/numpy/pandas/scikit-learn; scanpy and squidpy
# are added for the usual preprocessing / spatial-neighbour workflow around it.
RUN uv pip install --no-cache \
      "concordex==${CONCORDEX_VERSION}" \
      "scanpy[leiden]==1.11.4" \
      "squidpy==1.6.5" \
      jupyterlab ipykernel papermill

RUN python -c "from concordex.tools import calculate_concordex; import scanpy"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
