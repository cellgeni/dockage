# Phoenix - https://github.com/peng-lab/phoenix
# Latent flow-matching model that predicts spatially resolved single-cell gene expression
# from routine H&E histology ("virtual spatial transcriptomics").
# Installs the pure-torch model variant (`full` extra). The optimised apex/flash-attn/xformers
# variant (phoenix.models.flow_llama3 / mlp_mixer_ae; needs CUDA 13 + sm_80+) is NOT built.
# Model weights (huggingface.co/peng-lab/phoenix) are downloaded at runtime.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG PHOENIX_COMMIT="e96e260735191af9214a7ff82b0f6f47cf28706d"
# phoenix[full] depends on spatialrefinery@main; pin it to a commit via a uv override
ARG SPATIALREFINERY_COMMIT="3cf0363103f48f79ee4e98ac4daeceb489b303b6"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    NUMBA_CACHE_DIR=/tmp \
    HDF5_USE_FILE_LOCKING=FALSE

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
        libgl1 libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# phoenix requires Python >= 3.12
RUN uv venv "${VENV_PATH}" --python 3.12

# phoenix[full] pins torch==2.12.1 / torchvision==0.27.1. Upstream targets CUDA 13; use the
# cu126 wheels instead (bundle their own CUDA 12.6 runtime, work with CUDA 12.x drivers).
RUN uv pip install \
        torch==2.12.1 torchvision==0.27.1 \
        --index-url https://download.pytorch.org/whl/cu126

RUN echo "spatialrefinery[segmentation] @ git+https://github.com/peng-lab/spatialrefinery.git@${SPATIALREFINERY_COMMIT}" > /tmp/overrides.txt && \
    uv pip install \
        --override /tmp/overrides.txt \
        "phoenix[full] @ git+https://github.com/peng-lab/phoenix.git@${PHOENIX_COMMIT}" \
        jupyterlab ipykernel papermill && \
    rm /tmp/overrides.txt

RUN python -c "import phoenix, torch; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
