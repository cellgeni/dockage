# PathoPatch (PathoPatcher) - https://github.com/TIO-IKIM/PathoPatcher (PyPI: pathopatch)
# Fast whole-slide-image preprocessing: tissue detection, patch extraction, annotation
# handling, stain normalisation; OpenSlide + DICOM, with optional cuCIM GPU acceleration.
# CLI entry points: wsi_extraction, annotation_conversion, macenko_vector_generation.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG PATHOPATCH_VERSION="1.0.10"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV MPLCONFIGDIR=/tmp

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
        python3.10 python3.10-dev \
        libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upstream: Python < 3.12, 3.10 recommended.
RUN uv venv "${VENV_PATH}" --python python3.10

RUN uv pip install --no-cache \
        torch==2.3.1 torchvision==0.18.1 \
        --index-url https://download.pytorch.org/whl/cu121

# Upstream installs the OpenSlide C library (4.0.0, for DICOM) via conda; instead use the
# openslide-bin wheel, which openslide-python >= 1.4 picks up automatically.
# cuCIM + CuPy are the optional GPU speed-up recommended in the README
# (cucim-cu12 pinned to a release supporting Python 3.10; the newest needs >= 3.11).
RUN uv pip install --no-cache \
        "pathopatch==${PATHOPATCH_VERSION}" \
        "openslide-python>=1.4" openslide-bin \
        cucim-cu12==25.6.0 "cupy-cuda12x<14" \
        jupyterlab ipykernel papermill && \
    python -c "import openslide, pathopatch; print('OpenSlide', openslide.__library_version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
