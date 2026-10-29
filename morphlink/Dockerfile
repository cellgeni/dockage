# MorphLink - https://github.com/jianhuupenn/MorphLink
# Extracts interpretable morphological features from histology images and links them
# to molecular measurements (spatial transcriptomics / proteomics) via CPSI.
# CPU-only: torch is imported by MorphLink.main_functions but no GPU code is used.
FROM python:3.11-slim

ARG MORPHLINK_VERSION="1.0.7"

LABEL org.opencontainers.image.source="https://github.com/jianhuupenn/MorphLink"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
# MorphLink tutorial sets this so OpenCV can open very large H&E images
ENV OPENCV_IO_MAX_IMAGE_PIXELS=1099511627776

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python /usr/local/bin/python3.11

# Versions from the upstream "Environment 1" (tested, Python 3.11.5) in README/tutorial.
RUN uv pip install --no-cache \
      torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu

RUN uv pip install --no-cache \
      "MorphLink==${MORPHLINK_VERSION}" \
      pandas==2.1.4 \
      numpy==1.26.2 \
      numba==0.58.1 \
      scipy==1.11.4 \
      scanpy==1.9.6 \
      anndata==0.10.3 \
      scikit-learn==1.3.2 \
      scikit-image==0.23.2 \
      matplotlib==3.8.2 \
      imutils==0.5.4 \
      opencv-python==4.8.1.78 \
      leidenalg==0.10.2 \
      slideio==2.10.0 \
      seaborn==0.13.2 \
      jupyterlab ipykernel papermill

RUN python -c "import MorphLink as mph; print('MorphLink', mph.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
