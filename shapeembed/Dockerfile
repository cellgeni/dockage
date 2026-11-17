# ShapeEmbed - self-supervised representation learning for 2D shape analysis
# https://github.com/uhlmanngroup/ShapeEmbed  (paper: https://arxiv.org/abs/2507.01009)
# VAE on Euclidean distance matrices of object contours, giving translation/scale/rotation/reflection/indexing-invariant shape embeddings (PyTorch, GPU).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

# Script-based repos with no releases: pin commits.
ARG SHAPEEMBED_COMMIT="da515f9856f29585a36876a303f7ae896bd1bd6b"
# Companion repo to turn binary masks into the distance-matrix (EDM) inputs ShapeEmbed expects
ARG MASK2DM_COMMIT="71491b038018e655dc29a2414f41c44df5eab198"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python 3.12

RUN git clone https://github.com/uhlmanngroup/ShapeEmbed.git /opt/ShapeEmbed && \
    cd /opt/ShapeEmbed && git checkout "${SHAPEEMBED_COMMIT}" && \
    git clone https://github.com/uhlmanngroup/ConvertBinaryMasksToDMs.git /opt/ConvertBinaryMasksToDMs && \
    cd /opt/ConvertBinaryMasksToDMs && git checkout "${MASK2DM_COMMIT}"

# Upstream requirements.txt is unpinned (torch, torchvision, torchaudio, tensorboard, pandas,
# seaborn, scikit-learn, umap-learn, matplotlib, tqdm, torchinfo); ConvertBinaryMasksToDMs adds
# numpy, pillow, scikit-image, scipy, requests. torch pinned to a cu121 build.
RUN uv pip install --no-cache --torch-backend=cu121 \
      torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 \
      -r /opt/ShapeEmbed/requirements.txt \
      -r /opt/ConvertBinaryMasksToDMs/requirements.txt \
      scipy requests \
      jupyterlab ipykernel papermill

# Convenience wrapper: `shapeembed --help` == `python /opt/ShapeEmbed/shape_embed.py --help`
# (mask->EDM helpers: /opt/ConvertBinaryMasksToDMs/helpers.py, add it to PYTHONPATH or copy it)
RUN printf '#!/bin/bash\nexec python /opt/ShapeEmbed/shape_embed.py "$@"\n' > /usr/local/bin/shapeembed && \
    chmod 755 /usr/local/bin/shapeembed && \
    shapeembed --help > /dev/null

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
