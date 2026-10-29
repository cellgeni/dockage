# ENACT - https://github.com/Sanofi-Public/enact-pipeline
# End-to-end Visium HD pipeline: StarDist nuclei segmentation on H&E, bin-to-cell
# assignment and cell-type annotation (CellAssign / CellTypist / Sargent).
# Run: python -m enact.pipeline --configs_path config.yaml
# The repo (config templates, demo notebooks) is cloned to /opt/enact-pipeline.
# StarDist pretrained models are fetched by stardist/csbdeep on first use.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG ENACT_VERSION="0.2.5"
ARG ENACT_COMMIT="5cf6f2a3612589cecdfabaafd682005c5166f8f1"

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
        libgl1 libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# upstream uses Python 3.10
RUN uv venv "${VENV_PATH}" --python 3.10

# scvi-tools (CellAssign) needs torch; install the cu121 build first so the resolver does not
# pull the latest PyPI torch (built for a newer CUDA).
RUN uv pip install \
        torch==2.5.1 \
        --index-url https://download.pytorch.org/whl/cu121

# enact-SO pins tensorflow==2.17.0 (StarDist). tensorflow[and-cuda] is NOT used: its
# nvidia-cudnn-cu12==8.9.x pin conflicts with torch's cuDNN 9, so TF only uses the GPU if it
# can load the base image's CUDA 12.1/cuDNN 8 libs (otherwise StarDist runs on CPU, which
# upstream documents as supported).
RUN uv pip install \
        "enact-SO==${ENACT_VERSION}" \
        jupyterlab ipykernel papermill

RUN git clone https://github.com/Sanofi-Public/enact-pipeline.git /opt/enact-pipeline && \
    cd /opt/enact-pipeline && \
    git checkout "${ENACT_COMMIT}"

RUN python -c "import enact, stardist, tensorflow as tf; print('tf', tf.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
