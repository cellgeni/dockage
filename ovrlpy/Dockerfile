# ovrlpy - detection of overlapping cells / signal integrity in imaging-based spatial transcriptomics
# https://github.com/HiDiHlabs/ovrl.py
# Transcript-level quality control (vertical signal integrity) for Xenium/MERFISH/CosMx etc. (CPU only).
FROM python:3.12-slim

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

ARG OVRLPY_VERSION=1.2.1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.12

# [segmentation] extra adds shapely/rasterio/networkx for the segmentation-related helpers
RUN uv pip install --no-cache \
      "ovrlpy[segmentation]==${OVRLPY_VERSION}" \
      jupyterlab ipykernel papermill

RUN python -c "import ovrlpy; print('ovrlpy', ovrlpy.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
