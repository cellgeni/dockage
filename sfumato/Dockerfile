# SFUMATO - https://github.com/ale2sia-g/SFUMATO
# Bayesian (GPU, pure-torch) Gaussian-mixture clustering of binned spatial transcriptomics
# with uncertainty-aware colour visualisation. Not a pip package: the code is cloned to
# /opt/SFUMATO and run from there, e.g.
#   python /opt/SFUMATO/run_sfumato.py --config configs/mousexeniumniche.json
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG SFUMATO_COMMIT="93806f5c374f88bf4de0bf6e13df4bb7c85df4a4"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    NUMBA_CACHE_DIR=/tmp \
    HDF5_USE_FILE_LOCKING=FALSE \
    PYTHONPATH=/opt/SFUMATO

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# libgl1/libglib2.0-0 for opencv-python (make_masks/)
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
        libgl1 libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python 3.12

RUN uv pip install \
        torch==2.5.1 \
        --index-url https://download.pytorch.org/whl/cu121

RUN git clone https://github.com/ale2sia-g/SFUMATO.git /opt/SFUMATO && \
    cd /opt/SFUMATO && \
    git checkout "${SFUMATO_COMMIT}"

# requirements.txt is unpinned; pyyaml is imported but not listed.
# Note: the repo's own points2regions.py shadows the PyPI points2regions package when
# running from /opt/SFUMATO (that is what upstream's scripts import).
RUN uv pip install -r /opt/SFUMATO/requirements.txt && \
    uv pip install pyyaml jupyterlab ipykernel papermill

RUN cd /opt/SFUMATO && python -c "import torch, bgm, preprocess, run_bgm_gpu; print('torch', torch.__version__)"

WORKDIR /opt/SFUMATO

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
