# Base image with CUDA 12.1 runtime and cuDNN
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04


SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${VENV_PATH}:${PATH}"


RUN apt-get update -y && apt-get install -y --no-install-recommends \
    software-properties-common

# Install essential system tools and Python
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update -y && apt-get install -y --no-install-recommends \
    git \
    wget \
    curl \
    unzip \
    htop \
    vim \
    build-essential \
    python3 \
    python3.12 \
    python3.12-dev \
    python3-venv \
    python3-pip \
    python-is-python3 \
    bedtools \
    gcc \
    perl \
    make \
    libbz2-dev \
    zlib1g-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libdeflate-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install htslib
RUN wget -P /tmp https://github.com/samtools/htslib/releases/download/1.22/htslib-1.22.tar.bz2 && \
    tar xvjf /tmp/htslib-1.22.tar.bz2 -C /opt && \
    rm /tmp/htslib-1.22.tar.bz2
WORKDIR /opt/htslib-1.22
RUN make
ENV PATH="${PATH}:/opt/htslib-1.22"

# create venv
RUN python -m venv /env && \
    . ${VENV_PATH}/bin/activate && \
    pip install -U pip wheel setuptools

# install scdori
WORKDIR /opt
RUN git clone https://github.com/bioFAM/scDoRI.git /opt/scDoRI
RUN . /env/bin/activate && \
    pip install -e '/opt/scDoRI' && \
    pip install papermill jupyterlab 

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
