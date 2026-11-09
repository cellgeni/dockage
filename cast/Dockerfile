# CAST - https://github.com/wanglab-broad/CAST
# Physical alignment of spatial transcriptomics samples across technologies and
# batches: CAST Mark (graph self-supervised features, DGL GCNII), CAST Stack
# (rigid + B-spline registration) and CAST Projection (single-cell projection).
# No PyPI release / tags: pinned to a git commit (setup.py version 0.4).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG CAST_COMMIT="3ebcf4fbe1e43dbbb9ae92ecd07e93562e156160"

LABEL org.opencontainers.image.source="https://github.com/wanglab-broad/CAST"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
ENV DGLBACKEND=pytorch
ENV DGLDEFAULTDIR=/tmp/dgl

RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      python3.10 python3.10-dev python3.10-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.10

# DGL is not declared in setup.py but is required (CAST_Mark / GCNII model).
# DGL 2.4.0 is the newest release with cu121 wheels, built against torch 2.4.x.
RUN uv pip install --no-cache \
      torch==2.4.0+cu121 \
      torchvision==0.19.0+cu121 \
      --extra-index-url https://download.pytorch.org/whl/cu121

RUN git clone https://github.com/wanglab-broad/CAST.git /opt/CAST && \
    cd /opt/CAST && \
    git checkout "${CAST_COMMIT}"

# torch must be exactly 2.4.0 (DGL's graphbolt library is built per torch version);
# torchdata 0.8.0 still ships the datapipes module DGL 2.4 imports.
# numpy<2: DGL 2.4 wheels are built against numpy 1.x.
# shapely + ipywidgets are imported lazily in CAST.utils (region selection helpers).
RUN uv pip install --no-cache \
      "torch==2.4.0+cu121" "torchvision==0.19.0+cu121" \
      "dgl==2.4.0+cu121" \
      "torchdata==0.8.0" \
      "numpy<2" \
      /opt/CAST \
      shapely ipywidgets \
      jupyterlab ipykernel papermill \
      --extra-index-url https://download.pytorch.org/whl/cu121 \
      --find-links https://data.dgl.ai/wheels/torch-2.4/cu121/repo.html \
      --index-strategy unsafe-best-match

RUN python -c "import dgl, torch, CAST; print('dgl', dgl.__version__, 'torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
