FROM python:3.11

ENV VIRTUAL_ENV=/env
ENV PATH=$VIRTUAL_ENV/bin:$VIRTUAL_ENV:$PATH
ENV NUMBA_CACHE_DIR=/tmp
ENV PIP_NO_CACHE_DIR=off

RUN python3 -m venv $VIRTUAL_ENV && \
    . $VIRTUAL_ENV/bin/activate && \
    pip install --upgrade pip && \
    pip install tifffile imagecodecs ome-zarr
RUN . $VIRTUAL_ENV/bin/activate && \
    pip install --upgrade "jax[cuda11_pip]==0.4.23" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    git clone --depth=1 https://github.com/peng-lab/BaSiCPy.git /opt/BaSiCPy && cd /opt/BaSiCPy && pip install -e .

COPY Dockerfile /

FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV VIRTUAL_ENV=/env
ENV PATH=$VIRTUAL_ENV/bin:$VIRTUAL_ENV:$PATH
ENV NUMBA_CACHE_DIR=/tmp

RUN apt-get update && apt-get install -y \
        procps git wget build-essential \
        python3 python-is-python3 python3-dev python3-venv

RUN python -m venv $VIRTUAL_ENV && \
    . $VIRTUAL_ENV/bin/activate && \
    pip install --upgrade pip wheel setuptools && \
    pip install shapely zarr tqdm numpy pandas tifffile imagecodecs
