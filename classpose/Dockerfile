FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

ARG CLASSPOSE_COMMIT="8d7359172b935ee3fa2b697c662bc19f1429e079"

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONNOUSERSITE=1
ENV HDF5_USE_FILE_LOCKING=FALSE
ENV CLASSPOSE_MODEL_DIR=/models
ENV TORCHINDUCTOR_CACHE_DIR=/tmp/torchinductor

ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV UV_PYTHON_INSTALL_DIR="/opt/python"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir -p "${CLASSPOSE_MODEL_DIR}" && \
    mkdir -p "${TORCHINDUCTOR_CACHE_DIR}"

# install libraries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    procps git wget curl build-essential vim ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# install python packages
RUN uv venv "${VENV_PATH}" --python 3.14 && \
    uv pip install pip setuptools

RUN git clone https://github.com/sohmandal/classpose.git /opt/classpose && \
    cd /opt/classpose && \
    git checkout "${CLASSPOSE_COMMIT}"

RUN uv pip install -e /opt/classpose


COPY Dockerfile /docker/
RUN chmod -R 755 /docker
