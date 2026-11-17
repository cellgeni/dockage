# MicroSplit - https://github.com/CAREamics/MicroSplit-reproducibility
# Deep-learning (hierarchical VAE) computational multiplexing: unmixes several structures
# imaged in one fluorescence channel. Built on CAREamics; this image contains the
# reproducibility package + example notebooks (/opt/MicroSplit-reproducibility/examples).
# Pretrained models / datasets are downloaded by the notebooks at runtime (pooch).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG MICROSPLIT_COMMIT="f45d01d1f71c0c9a0370e4e692cbdfc58d305869"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    HDF5_USE_FILE_LOCKING=FALSE

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python 3.10

# careamics<=0.0.12 caps torch<=2.6 / torchvision<=0.21
RUN uv pip install \
        torch==2.5.1 torchvision==0.20.1 \
        --index-url https://download.pytorch.org/whl/cu121

RUN git clone https://github.com/CAREamics/MicroSplit-reproducibility.git /opt/MicroSplit-reproducibility && \
    cd /opt/MicroSplit-reproducibility && \
    git checkout "${MICROSPLIT_COMMIT}"

# careamics pinned to the newest version the reproducibility package allows (<=0.0.12).
# albumentations / torchmetrics / pandas / pooch are imported by the package but not
# declared in its pyproject.
RUN uv pip install \
        "careamics[examples,wandb]==0.0.12" \
        /opt/MicroSplit-reproducibility \
        albumentations torchmetrics pandas pooch \
        jupyterlab ipykernel papermill

RUN python -c "import torch, careamics, microsplit_reproducibility; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
