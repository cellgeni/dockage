FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

ARG CELLVIT_VERSION=1.0.9

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONNOUSERSITE=1
ENV HDF5_USE_FILE_LOCKING=FALSE

ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
COPY --from=ghcr.io/astral-sh/uv:0.9.1 /uv /uvx /bin/

# install libraries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    procps git wget curl build-essential vim ca-certificates libgeos-dev \
  && rm -rf /var/lib/apt/lists/*

# install python packages
RUN uv venv "${VENV_PATH}" --python 3.13 && \
    uv pip install pip setuptools

RUN uv pip install torch torchvision cucim-cu12 "cupy-cuda12x<14.0" "numpy<2.0" cutensor-cu12 --torch-backend=cu121 && \
    uv pip install cellvit=="${CELLVIT_VERSION}" openslide-bin openslide-python 

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
