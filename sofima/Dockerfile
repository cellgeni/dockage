# SOFIMA - https://github.com/google-research/sofima
# Scalable Optical Flow-based Image Montaging and Alignment (JAX): stitching and elastic
# alignment of large microscopy (EM / light) image datasets; GPU-accelerated via JAX.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV MPLCONFIGDIR=/tmp
# don't let JAX grab 75% of GPU memory up front
ENV XLA_PYTHON_CLIENT_PREALLOCATE=false

# PyPI release (0.1, 2022) is stale; pin a git commit
ARG SOFIMA_COMMIT="c8b5e254a9b031a9c00f3d399e47bafda3c96a22"

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python 3.12

# JAX with pip-installed CUDA 12 libraries (jax[cuda12] brings its own CUDA/cuDNN wheels)
RUN uv pip install --no-cache "jax[cuda12]==0.4.38"

RUN git clone https://github.com/google-research/sofima.git /opt/sofima && \
    cd /opt/sofima && \
    git checkout "${SOFIMA_COMMIT}"

# sofima (+ decorators extra: gin-config, tensorstore); connectomics is a runtime dependency.
# Version comes from setuptools_scm and the repo has no tags, so set it explicitly.
RUN SETUPTOOLS_SCM_PRETEND_VERSION="0.0.0+g${SOFIMA_COMMIT:0:7}" \
    uv pip install --no-cache \
      "/opt/sofima[decorators]" \
      matplotlib tqdm \
      jupyterlab ipykernel papermill

RUN python -c "import jax, sofima; from sofima import flow_field, mesh, stitch_rigid, stitch_elastic, warp; print('jax', jax.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
