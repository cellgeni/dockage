# COAST - https://github.com/mahfouzlab/COAST
# Consecutive multi-Omics Alignment of Spatial Tissues: aligns consecutive uni-/multi-modal
# spatial sections using ssDINO image embeddings + CAST Stack (rigid + FFD) + KD-tree spot matching.
# COAST is a set of scripts (no package); they are cloned to /opt/COAST and put on PYTHONPATH.
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

# No release tags upstream - pin commits.
ARG COAST_COMMIT="c3f446ed82a94e3736223eba32305201360b8f1a"
ARG CAST_COMMIT="3ebcf4fbe1e43dbbb9ae92ecd07e93562e156160"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV PYTHONPATH="/opt/COAST/COAST"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
        python3.10 python3.10-dev \
        libgl1 libglib2.0-0 libgeos-dev libspatialindex-dev \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python python3.10

# Upstream env uses torch 2.5.1, but CAST needs DGL, whose newest CUDA wheels
# (2.4.0) are built against torch 2.4 - so use torch 2.4.1 + dgl 2.4.0 (cu121).
RUN uv pip install --no-cache \
        torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 \
        --index-url https://download.pytorch.org/whl/cu121 && \
    uv pip install --no-cache \
        dgl==2.4.0+cu121 "torchdata==0.8.0" pydantic \
        -f https://data.dgl.ai/wheels/torch-2.4/cu121/repo.html

# Versions follow upstream environment.yml (numpy kept <2 for the DGL 2.4 wheels).
RUN uv pip install --no-cache \
        "numpy<2" \
        scipy==1.15.2 \
        pandas==2.3.3 \
        scikit-learn==1.7.2 \
        seaborn==0.13.2 \
        matplotlib==3.9.4 \
        scanpy==1.11.5 \
        anndata==0.11.3 \
        umap-learn==0.5.9.post2 \
        pynndescent \
        h5py==3.12.1 \
        pillow==11.3.0 \
        statsmodels==0.14.5 \
        pyyaml tqdm natsort networkx \
        geopandas shapely rtree libpysal ipywidgets \
        jupyterlab ipykernel papermill

RUN uv pip install --no-cache "git+https://github.com/wanglab-broad/CAST.git@${CAST_COMMIT}"

RUN git clone https://github.com/mahfouzlab/COAST.git /opt/COAST && \
    cd /opt/COAST && git checkout "${COAST_COMMIT}" && \
    chmod -R 755 /opt/COAST

# NOTE: extract_features.py fetches the DINO ViT-S/16 weights at runtime via
# torch.hub.load('facebookresearch/dino:main', 'dino_vits16') - needs network access,
# or pre-populate $TORCH_HOME (default ~/.cache/torch/hub) and mount it.
RUN python -c "import torch, dgl, CAST, scanpy; print('torch', torch.__version__, 'dgl', dgl.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
