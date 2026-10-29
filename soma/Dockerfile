# soma - https://github.com/clemsgrs/soma (PyPI: soma-pathology)
# Modular computational-pathology experimentation framework: WSI tiling (hs2p), frozen
# foundation-model feature extraction (slide2vec) and MIL / dense downstream training.
# Usage: soma run config.yaml   |   soma list encoders
# Simplified from upstream's Dockerfile: no ASAP (wholeslidedata ASAP backend unusable),
# no flash-attn, no dev tools (node/codex/claude/gh/sshd).
# Foundation-model weights are fetched from Hugging Face at runtime (gated models need HF_TOKEN).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG SOMA_VERSION="2.2.1"
# git-only encoder dependencies installed by upstream's Dockerfile, pinned to commits
ARG MUSK_COMMIT="714b666969c1911e5efe70d991140a21030f4ef3"
ARG CONCH_COMMIT="141cc09c7d4ff33d8eda562bd75169b457f71a62"
ARG GIGAPATH_COMMIT="55431e04ff853a08f752a0ba42e6e9c48e60c776"
ARG SAM2_COMMIT="2b90b9f5ceec907a1c18123530e92e794ad901a4"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    HDF5_USE_FILE_LOCKING=FALSE \
    SAM2_BUILD_CUDA=0

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
        libgl1 libglib2.0-0 libtiff5 libvips42 libspatialindex-dev libnuma1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# upstream uses Python 3.11
RUN uv venv "${VENV_PATH}" --python 3.11

# Upstream pins torch 2.8.* (lowest accepted by torchvision>=0.23, highest with prebuilt
# cu12 flash-attn wheels). cu126 wheels bundle their own CUDA 12.6 runtime.
RUN uv pip install \
        "torch==2.8.0" "torchvision==0.23.0" \
        --index-url https://download.pytorch.org/whl/cu126

RUN uv pip install \
        "soma-pathology==${SOMA_VERSION}" \
        "git+https://github.com/lilab-stanford/MUSK.git@${MUSK_COMMIT}" \
        "git+https://github.com/Mahmoodlab/CONCH.git@${CONCH_COMMIT}" \
        "git+https://github.com/prov-gigapath/prov-gigapath.git@${GIGAPATH_COMMIT}" \
        "git+https://github.com/facebookresearch/sam2.git@${SAM2_COMMIT}" \
        jupyterlab ipykernel papermill

RUN soma --help > /dev/null && python -c "import soma, slide2vec, hs2p, torch; print('torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
