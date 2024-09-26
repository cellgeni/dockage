FROM nvcr.io/nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

SHELL ["/bin/bash", "-c"]

ENV PYTHONNOUSERSITE=1
ENV PATH="/env/bin:${PATH}"

# OS dependecies
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential software-properties-common \
      python3.10 python3.10-dev python3-venv python3-pip python-is-python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# create venv
RUN python -m venv /env

# update pip/wheel
RUN source /env/bin/activate && \
    pip install -U pip wheel setuptools --no-cache-dir
# pre install jax/torch
RUN . /env/bin/activate && \
    TORCH=2.3.0 CUDA=cu121 && \
    pip install "jax[cuda12]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html --no-cache-dir && \
    pip install torch==${TORCH}+${CUDA} torchvision --index-url "https://download.pytorch.org/whl/${CUDA}" --no-cache-dir

RUN apt-get update && apt-get install build-essential 
# install scvi tools and scarches
RUN source /env/bin/activate && \
    pip install "scvi-tools[tutorials]" \
      papermill jupyterlab --no-cache-dir

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
