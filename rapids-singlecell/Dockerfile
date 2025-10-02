FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive 

SHELL ["/bin/bash", "-c"]


# non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_INSTALL_DIR="/usr/local/share/uv"


# Update and install system dependencies
RUN apt-get update && apt-get install -y \
    git build-essential procps curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and install uv package manager and copy to system bin
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/uv

# Create venv first
RUN uv venv "${VENV_PATH}" --python 3.13

# Install RAPIDS dependencies
RUN uv pip install \
    --no-cache-dir \
    --extra-index-url=https://pypi.nvidia.com \
    "cudf-cu12==25.8.*" "dask-cudf-cu12==25.8.*" "cuml-cu12==25.8.*" \
    "cugraph-cu12==25.8.*" "nx-cugraph-cu12==25.8.*" "cuxfilter-cu12==25.8.*" \
    "cucim-cu12==25.8.*" "pylibraft-cu12==25.8.*" "raft-dask-cu12==25.8.*" \
    "cuvs-cu12==25.8.*" "nx-cugraph-cu12==25.8.*" cupy-cuda12x

# Install core rapids-singlecell and other useful packages
RUN uv pip install rapids-singlecell==0.13.2 jupyterlab notebook tqdm ipywidgets papermill ipykernel gdown \
    --no-cache-dir

# Copy Dockerfile to /docker/ in image and set permissions
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
