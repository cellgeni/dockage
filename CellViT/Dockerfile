FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV VIRTUAL_ENV=/env
ENV PATH=$VIRTUAL_ENV/bin:$VIRTUAL_ENV:$PATH
ENV NUMBA_CACHE_DIR=/tmp
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
        procps git wget build-essential \
        python3 python-is-python3 python3-dev python3-venv

RUN python -m venv $VIRTUAL_ENV && \
    . $VIRTUAL_ENV/bin/activate && \
    pip install --upgrade pip wheel setuptools && \
    pip install shapely zarr tqdm numpy pandas tifffile imagecodecs


RUN apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:openslide/openslide && \
    apt-get update -y &&  \
    apt-get install -y python3-openslide

RUN git clone https://github.com/TIO-IKIM/CellViT.git /opt/CellViT
RUN . $VIRTUAL_ENV/bin/activate && \
    pip install 'torch==2.4.1+cu121' torchvision --index-url https://download.pytorch.org/whl/cu121 && \
    pip install -r "/opt/CellViT/requirements.txt" && \
    pip install cucim-cu12 cupy-cuda12x

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
