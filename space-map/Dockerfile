# Space-map - atlas-level single-cell 3D tissue reconstruction from serial sections
# https://github.com/czhu/space-map  (the spreadsheet link github.com/a12910/space-map now 404s; czhu/space-map is the current upstream)
# Affine + GPU-accelerated LDDMM registration of serial Xenium/CODEX sections into 3D, with LoFTR/SIFT feature matching (PyTorch/kornia, GPU).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

# Not on PyPI and no tags upstream: pin the latest master commit (package version 0.2.0)
ARG SPACEMAP_COMMIT="fe0eb874085321ac6f083a33d8905973f6a960af"

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

# libgl1/libglib2.0-0 for opencv-python
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git ca-certificates \
      libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python 3.11

RUN git clone https://github.com/czhu/space-map.git /opt/space-map && \
    cd /opt/space-map && \
    git checkout "${SPACEMAP_COMMIT}"

# requirement.txt is unpinned; torch pinned to a cu121 build and opencv kept on 4.x.
# LoFTR weights used by kornia are downloaded on first use, not at build time.
RUN uv pip install --no-cache --torch-backend=cu121 \
      torch==2.5.1 torchvision==0.20.1 \
      "opencv-python<5" \
      -r /opt/space-map/requirement.txt \
      -e /opt/space-map \
      jupyterlab ipykernel papermill

RUN space-map --help > /dev/null && \
    python -c "import space_map, torch; print('space_map', space_map.__version__, 'torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
