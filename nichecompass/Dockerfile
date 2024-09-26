FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

SHELL ["/bin/bash", "-c"]

ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PIP_NO_CACHE_DIR=off
ENV NUMBA_CACHE_DIR=/tmp
ENV PYTHONNOUSERSITE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git python3 python3-dev python3-venv python3-pip python-is-python3 wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# get bedtools
RUN wget -O /usr/bin/bedtools https://github.com/arq5x/bedtools2/releases/download/v2.31.0/bedtools.static && \
    chmod a+x /usr/bin/bedtools

# install python packagess
RUN TORCH=2.2.0 CUDA=cu121 && \
    python3 -m venv $VENV_PATH && \
    . $VENV_PATH/bin/activate && \
    pip install -U pip wheel setuptools
RUN . $VENV_PATH/bin/activate && \
    pip install "torch==${TORCH}+${CUDA}" --index-url "https://download.pytorch.org/whl/${CUDA}" --no-cache-dir && \
    pip install pyg_lib torch_scatter torch_sparse -f https://data.pyg.org/whl/torch-${TORCH}+${CUDA}.html
RUN . $VENV_PATH/bin/activate && \
    pip install papermill jupyterlab ipykernel nichecompass[all] --no-cache-dir

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
