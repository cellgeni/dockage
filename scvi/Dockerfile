FROM nvcr.io/nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${VENV_PATH}:${PATH}"
ENV PYTHONNOUSERSITE=true

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

# pre install jax/torch
RUN . ${VENV_PATH}/bin/activate && \
    TORCH=2.3.0 CUDA=cu121 && \
    pip install "jax[cuda12]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html --no-cache-dir && \
    pip install torch==${TORCH}+${CUDA} torchvision --index-url "https://download.pytorch.org/whl/${CUDA}" --no-cache-dir && \
    pip install papermill jupyterlab 

# install scvi tools and scarches
RUN . /env/bin/activate && \
    pip install "scvi-tools[tutorials]"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
