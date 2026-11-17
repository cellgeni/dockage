# CellFlow - https://github.com/theislab/cellflow (PyPI: cellflow-tools)
# Flow-matching (JAX/Flax, ott-jax) generative model of single-cell responses to complex
# perturbations (drugs, genetic, cytokines, developmental protocols).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG CELLFLOW_VERSION="0.0.9"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    NUMBA_CACHE_DIR=/tmp \
    XLA_PYTHON_CLIENT_PREALLOCATE=false

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# cellflow-tools requires Python >= 3.11
RUN uv venv "${VENV_PATH}" --python 3.12

# jax[cuda12] brings its own CUDA 12 / cuDNN pip wheels. cellflow does not pin jax/flax;
# pin them to releases contemporary with cellflow-tools 0.0.9 (April 2026) to avoid
# breakage from newer JAX/Flax APIs.
RUN uv pip install \
        "cellflow-tools==${CELLFLOW_VERSION}" \
        "jax[cuda12]==0.9.2" \
        "flax==0.12.6" \
        jupyterlab ipykernel papermill

RUN python -c "import cellflow, jax; print('jax', jax.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
