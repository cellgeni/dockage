FROM rapidsai/miniforge-cuda:cuda11.8.0-base-ubuntu22.04-py3.11

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps curl maven openjdk-11-jre ocl-icd-libopencl1 ocl-icd-opencl-dev clinfo nvidia-cuda-toolkit && \ 
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uv

COPY requirements.txt /app/

# Install PyTorch 2.5.1 with CUDA 12 support using uv
RUN uv venv --python=python3.12 ./ && \
    uv pip install --no-cache-dir --upgrade pip setuptools && \
    uv pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV NUMBA_CACHE_DIR=\$PWD

# cjdk is needed for aicsimageio-bioformats_jar
# COPY cjdk /root/.cache/cjdk

COPY Dockerfile /docker/
RUN chmod -R 755 /docker

RUN echo "source /app/bin/activate" >> /root/.bashrc
