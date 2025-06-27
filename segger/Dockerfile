# Base image with CUDA 12.1 runtime and cuDNN
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# Set environment variables
# ENV PYTHONPATH=/workspace/segger_dev/src:$PYTHONPATH

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Set working directory
WORKDIR /workspace

# Install essential system tools and Python
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends \
    git \
    wget \
    curl \
    unzip \
    htop \
    vim \
    build-essential \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the repository and install segger with CUDA 12 support
RUN python -m pip install --no-cache-dir --upgrade pip && \
    git clone https://github.com/EliHei2/segger_dev.git /workspace/segger_dev && \
    pip install -e "/workspace/segger_dev[cuda12]"

RUN pip uninstall -y torch torchvision pandas numpy shapely && \
    pip install torchvision pandas torch==2.5.1 numpy==2.0.2 shapely==2.0.6 fire

# expose ports for debugpy and jupyterlab
# EXPOSE 5678 8888

# COPY predict_fast.py /workspace/segger_dev/src/segger/cli/predict_fast.py

COPY Dockerfile /docker/
RUN chmod -R 755 /docker