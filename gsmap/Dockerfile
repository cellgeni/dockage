# gsMap - genetically informed spatial mapping of cells for complex traits
# https://github.com/JianYang-Lab/gsMap
# Integrates spatial transcriptomics with GWAS summary statistics to map trait-associated cells (GNN latent step uses PyTorch, GPU).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

ARG GSMAP_VERSION=1.73.8

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

RUN uv venv ${VENV_PATH} --python 3.11

# torch pinned in the same resolve so it is not upgraded to a non-cu121 build.
# gsMap reference resources (LD scores, gene annotations, ~GBs) are NOT downloaded here;
# fetch gsMap_resource from https://yanglab.westlake.edu.cn/data/gsMap/ and mount at runtime.
RUN uv pip install --no-cache --torch-backend=cu121 \
      torch==2.5.1 \
      "gsMap==${GSMAP_VERSION}" \
      jupyterlab ipykernel papermill

RUN gsmap --help > /dev/null && \
    python -c "import gsMap, torch; print('gsMap', gsMap.__version__, 'torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
