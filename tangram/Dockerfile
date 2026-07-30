FROM nvcr.io/nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Keerthi Priya Chakala <kc28@sanger.ac.uk>, Stanislaw Makarchuk <sm57@sanger.ac.uk>, Tong Li <tl10@sanger.ac.uk>"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system

# ---- System dependencies ----
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential \
      python3.10 python3.10-dev \
      ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ---- Create venv ----
RUN uv venv ${VENV_PATH} --python python3.10

# ---- Install Python requirements ----
# Core scientific stack + single-cell / spatial
RUN uv pip install --no-cache \
      "numpy<2.0" \
      pandas==2.1.4 \
      scipy==1.10.1 \
      matplotlib==3.7.5 \
      seaborn==0.13.2 \
      scikit-learn==1.3.2 \
      tqdm \
      h5py==3.10.0 \
      anndata==0.9.2 \
      scanpy==1.9.8 \
      tangram-sc==1.0.4 \
      spatialdata==0.0.16

# GPU / ML
RUN uv pip install --no-cache \
      torch==2.3.0+cu121 \
      torchvision==0.18.0+cu121 \
      --extra-index-url https://download.pytorch.org/whl/cu121

# JAX (CUDA 12)
RUN uv pip install --no-cache \
      jax==0.4.28 \
      jaxlib==0.4.28+cuda12.cudnn89 \
      -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

# ---- Sanity check: confirm Python + Torch + JAX ----
RUN python --version && which python && \
    python -c "import torch; print('Torch:', torch.__version__, 'CUDA available:', torch.cuda.is_available())" && \
    python -c "import jax; print('JAX:', jax.__version__, 'Backend:', jax.default_backend())"