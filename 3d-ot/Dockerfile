# 3d-OT - https://github.com/dbjzs/3d-OT (Python package: lib_3d_OT)
# Geometry-aware (PointNet++ / GNN + soft-communication optimal transport) alignment of
# heterogeneous spatial (multi-)omics slices, spatial-domain detection and 3D reconstruction.
# Uses R's mclust (via rpy2) for clustering, so R is installed alongside Python.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# No release tags upstream - pin a commit.
ARG THREEDOT_COMMIT="39a7cb02748d83299cd471f172f3b972896e61d8"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
ENV R_HOME=/usr/lib/R

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Upstream installs r-base + r-mclust via conda; use Ubuntu's R (4.1) + r-cran-mclust instead.
# r-base-dev is needed to build rpy2's C extension.
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates pkg-config \
        python3.10 python3.10-dev \
        r-base r-base-dev r-cran-mclust \
        libopenblas-dev libpcre2-dev liblzma-dev libbz2-dev libicu-dev libreadline-dev \
    && rm -rf /var/lib/apt/lists/*

# Upstream: Python 3.10.
RUN uv venv "${VENV_PATH}" --python python3.10

RUN uv pip install --no-cache \
        torch==2.2.0 \
        --index-url https://download.pytorch.org/whl/cu121

# Pins from upstream requirements.txt.
RUN uv pip install --no-cache \
        anndata==0.10.5.post1 \
        numpy==1.26.3 \
        pandas==2.2.3 \
        scanpy==1.9.8 \
        torch_geometric==2.4.0 \
        scikit-learn==1.4.0 \
        scipy==1.12.0 \
        scikit-misc==0.5.1 \
        tqdm==4.67.1 \
        rpy2==3.5.11 \
        plotly==6.0.1 \
        nbformat==5.10.4 \
        matplotlib-inline==0.1.6 \
        matplotlib==3.6.2 \
        jupyterlab ipykernel papermill

RUN uv pip install --no-cache "git+https://github.com/dbjzs/3d-OT.git@${THREEDOT_COMMIT}" && \
    python -c "import lib_3d_OT, torch_geometric; from rpy2.robjects.packages import importr; importr('mclust'); print('ok')"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
