FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    && ln -sf /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN mkdir -p /opt/tmp && chmod 1777 /opt/tmp

ENV TMPDIR=/opt/tmp
ENV UV_CONCURRENT_DOWNLOADS=1
ENV UV_CONCURRENT_BUILDS=1
ENV UV_CONCURRENT_INSTALLS=1

RUN python -m pip install --no-cache-dir --upgrade pip uv

RUN uv pip install --system --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    "torch==2.5.1"

RUN uv pip install --system --no-cache-dir \
    "hyperactive<5" \
    "gradient-free-optimizers<1.7" \
    "numpy<2"

RUN uv pip install --system --no-cache-dir \
    cucim \
    fire \
    ome-zarr \
    ome-types \
    aicsimageio \
    scipy \
    scikit-image \
    cupy-cuda12x

RUN uv pip install --system --no-cache-dir \
    "fractal-tasks-core[fractal-tasks]" \
    apx_fractal_task_collection \
    "torch<2.6"

# RUN uv pip install --system --no-cache-dir \
#     git+https://github.com/jluethi/fractal-helper-tasks.git

COPY Dockerfile /docker

RUN chmod -R 755 /docker
