FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    software-properties-common \
    procps curl maven openjdk-11-jre \
    ocl-icd-libopencl1 ocl-icd-opencl-dev clinfo nvidia-cuda-toolkit \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y --no-install-recommends \
    python3.11 python3.11-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.11 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel uv

COPY requirements.txt /app/

RUN /opt/venv/bin/uv pip install --python /opt/venv/bin/python --no-cache-dir -r /app/requirements.txt

# Singularity runs as the host user (not root); make interpreter and site-packages
# executable/readable for all users and ensure python3 resolves predictably.
RUN chmod -R a+rX /opt/venv && \
    ln -sf /opt/venv/bin/python /usr/bin/python3 && \
    ln -sf /opt/venv/bin/python /usr/local/bin/python3

ENV VIRTUAL_ENV=/opt/venv
ENV PATH=/opt/venv/bin:/usr/local/bin:/usr/bin:/bin
ENV NUMBA_CACHE_DIR=/tmp

# Force clean runtime env inside Singularity/Apptainer.
RUN mkdir -p /.singularity.d/env && \
    printf '%s\n' \
    '#!/bin/sh' \
    'export PATH=/opt/venv/bin:/usr/local/bin:/usr/bin:/bin' \
    'unset PYTHONHOME' \
    'unset PYTHONPATH' \
    > /.singularity.d/env/99-python-path.sh && \
    chmod 755 /.singularity.d/env/99-python-path.sh

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
