FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${VENV_PATH}:${PATH}"

# OS dependecies
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential software-properties-common \
      python3.10 python3.10-dev python3-venv python3-pip python-is-python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# create venv
RUN python -m venv /env && \
    . ${VENV_PATH}/bin/activate && \
    pip install -U pip wheel setuptools

COPY terra_model /opt/terra_model
WORKDIR /opt/terra
RUN . /env/bin/activate && \
    pip install --no-cache-dir "terra-st==0.1.13" papermill jupyterlab

COPY Dockerfile /docker/
