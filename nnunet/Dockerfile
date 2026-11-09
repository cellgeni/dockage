# nnU-Net (v2) - https://github.com/MIC-DKFZ/nnUNet (PyPI: nnunetv2)
# Self-configuring deep-learning framework for 2D/3D (bio)medical image segmentation.
# CLI entry points: nnUNetv2_plan_and_preprocess, nnUNetv2_train, nnUNetv2_predict, ...
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG NNUNET_VERSION="2.8.1"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV MPLCONFIGDIR=/tmp
ENV TORCHINDUCTOR_CACHE_DIR=/tmp/torchinductor

# nnU-Net needs these three paths at runtime (see documentation/setting_up_paths.md).
# Defaults point under /data - override with -e / --env or bind-mount to /data.
ENV nnUNet_raw="/data/nnUNet_raw"
ENV nnUNet_preprocessed="/data/nnUNet_preprocessed"
ENV nnUNet_results="/data/nnUNet_results"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# build-essential + python3.10-dev: torch.compile (used by default in training) needs a C compiler.
# graphviz: optional network-architecture plots.
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
        python3.10 python3.10-dev graphviz \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python python3.10

# torch 2.5.1 is the newest cu121 build (nnunetv2 requires torch >=2.1.2, != 2.9.*).
RUN uv pip install --no-cache \
        torch==2.5.1 torchvision==0.20.1 \
        --index-url https://download.pytorch.org/whl/cu121

RUN uv pip install --no-cache \
        "nnunetv2==${NNUNET_VERSION}" \
        jupyterlab ipykernel papermill && \
    python -c "import nnunetv2, torch; print('torch', torch.__version__)" && \
    nnUNetv2_train -h > /dev/null

# Pretrained models are not bundled; fetch with nnUNetv2_download_pretrained_model_by_url
# or nnUNetv2_install_pretrained_model_from_zip into $nnUNet_results.

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
