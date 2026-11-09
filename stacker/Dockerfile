# STaCker - https://github.com/regeneron-mpds/stacker
# Deep-learning (TensorFlow/voxelmorph) image-registration based common coordinate builder
# for aligning spatial transcriptomics slices.
#
# Base image deviates from the house nvidia/cuda:12.1.1 base on purpose: STaCker requires
# TensorFlow 2.9 (CUDA 11.x), and upstream tests exclusively on nvcr.io/nvidia/tensorflow:22.07-tf2-py3
# (Ubuntu 20.04, Python 3.8, TF 2.9, pip-installed - no conda). Driver must support CUDA 11.7.
#
# STaCker is not a package: code lives in /opt/stacker/code/libs (on PYTHONPATH as `libs`).
# Sample model weights ship with the repo in /opt/stacker/data/stacker-params-sample;
# example notebooks in /opt/stacker/testing.
FROM nvcr.io/nvidia/tensorflow:22.07-tf2-py3

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONNOUSERSITE=true
ENV PIP_NO_CACHE_DIR=1
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

# No releases upstream; pin commit
ARG STACKER_COMMIT="580a821447424673b084b7572a0a53c0ca9f2de9"

# docker-config.sh: openexr ffmpeg libsm6 libxext6 (exact apt versions there are not pinned here)
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git ca-certificates \
      openexr libopenexr-dev ffmpeg libsm6 libxext6 libgl1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/regeneron-mpds/stacker.git /opt/stacker && \
    cd /opt/stacker && \
    git checkout "${STACKER_COMMIT}"

# Installed into the image's system python so the NGC TensorFlow build stays in use.
# docker-requirements.txt pins jupyterlab==2.3.2; papermill added per house rules.
# antspyx==0.3.8 is no longer on PyPI; 0.4.2 is the oldest release left (has cp38 wheels).
RUN sed -i 's/^antspyx==0.3.8$/antspyx==0.4.2/' /opt/stacker/docker-requirements.txt && \
    pip install pip==23.3.1 && \
    pip install -r /opt/stacker/docker-requirements.txt && \
    pip install papermill ipykernel

ENV PYTHONPATH="/opt/stacker/code"

RUN python -c "import tensorflow as tf, voxelmorph, neurite, squidpy; from libs.alignment import stacker_register; from libs.models import STaCkerSemiSupervised; print('tf', tf.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
