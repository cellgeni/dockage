# STARCall - https://github.com/FowlerLab/starcall-workflow (+ packages starcall, constitch)
# STitching, Alignment and Read CALLing for in situ sequencing (FISSEQ / optical pooled screens):
# Snakemake pipeline + Python packages, with Cellpose/StarDist segmentation.
# Paper: https://www.biorxiv.org/content/10.1101/2025.10.31.685785v1
#
# The workflow is cloned (with its starcall/constitch submodules) to /opt/starcall-workflow;
# both packages are also pip-installed so they import from anywhere. Run e.g.:
#   cp -r /opt/starcall-workflow ./run && cd run && snakemake <target> --cores N
# CellProfiler phenotyping is optional upstream (separate conda env) and is NOT included.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# No release tags upstream - pin the workflow commit (submodules follow its pinned SHAs).
ARG STARCALL_WORKFLOW_COMMIT="f2b486a39a74575ae3f6d7a71a78b9032f66e764"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
        python3.10 python3.10-dev \
        libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upstream: Python 3.10.
RUN uv venv "${VENV_PATH}" --python python3.10

# setuptools>=81 dropped pkg_resources (and the distutils shim), which older deps still
# import at build and run time; keep it below 81 for every uv install in this image.
RUN echo "setuptools<81" > /etc/uv-constraints.txt
ENV UV_CONSTRAINT=/etc/uv-constraints.txt
ENV UV_BUILD_CONSTRAINT=/etc/uv-constraints.txt
RUN uv pip install --no-cache "setuptools<81"

RUN git clone https://github.com/FowlerLab/starcall-workflow.git /opt/starcall-workflow && \
    cd /opt/starcall-workflow && \
    git checkout "${STARCALL_WORKFLOW_COMMIT}" && \
    git submodule update --init --recursive && \
    chmod -R 755 /opt/starcall-workflow

RUN uv pip install --no-cache \
        torch==2.3.1 torchvision==0.18.1 \
        --index-url https://download.pytorch.org/whl/cu121

# Based on upstream requirements.txt, with one deliberate change: tensorflow 2.13.0 caps
# typing-extensions < 4.6, which conflicts with modern torch and basicpy (pydantic 2), so
# tensorflow 2.15.1 (last Keras-2 release; fine for stardist 0.8.5) is used instead.
# Extra imports found in the code: opencv, plotly, psutil, tqdm, imageio, numba, scipy.
RUN uv pip install --no-cache \
        "numpy<2" \
        "scikit-image>=0.18" \
        "scikit-learn>=1" \
        cellpose==2.2.1 \
        tensorflow==2.15.1 \
        stardist==0.8.5 \
        "matplotlib>=3" \
        tifffile \
        pulp==2.7.0 \
        "snakemake>=7" \
        nd2==0.7.1 \
        nd2reader \
        pandas==1.5.3 \
        ome-types \
        basicpy \
        opencv-python-headless plotly psutil tqdm imageio numba scipy \
        jupyterlab ipykernel papermill

RUN uv pip install --no-cache \
        /opt/starcall-workflow/packages/starcall \
        /opt/starcall-workflow/packages/constitch && \
    python -c "import starcall, constitch, cellpose, stardist, snakemake; print('ok')"

# NOTE: Cellpose / StarDist pretrained weights are downloaded on first use (needs network,
# or pre-populate ~/.cellpose and ~/.keras).

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
