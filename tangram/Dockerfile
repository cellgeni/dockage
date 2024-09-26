FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PIP_NO_CACHE_DIR=off
ENV NUMBA_CACHE_DIR=/tmp

RUN apt update && apt install --no-install-recommends --yes \
        wget unzip python3 python3-venv python3-dev python3-pip python-is-python3

RUN python -m venv $VENV_PATH && \
    . ${VENV_PATH}/bin/activate && \
    pip install -U pip wheel setuptools

RUN . ${VENV_PATH}/bin/activate && \
    pip install 'numpy<2' && \
    pip install jupyterlab papermill 'scanpy[leiden]' squidpy tangram-sc

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
