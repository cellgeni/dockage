# SegJointGene - https://github.com/daifengwanglab/segjointgene
# Self-training UNet framework for spatial cell-type segmentation with attribution
# (CID) constrained label propagation. Not a pip package: the code is cloned to
# /opt/segjointgene and run from there (python main.py ... / scripts/run_cid.sh).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG SEGJOINTGENE_COMMIT="41365a38da32f01fafa785ef094a47fc5c89fec4"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    PYTHONPATH=/opt/segjointgene

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# libgl1/libglib2.0-0 for opencv-python
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
        libgl1 libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# upstream tests with Python 3.11
RUN uv venv "${VENV_PATH}" --python 3.11

RUN uv pip install \
        torch==2.5.1 torchvision==0.20.1 \
        --index-url https://download.pytorch.org/whl/cu121

RUN git clone https://github.com/daifengwanglab/segjointgene.git /opt/segjointgene && \
    cd /opt/segjointgene && \
    git checkout "${SEGJOINTGENE_COMMIT}"

# requirements.txt is unpinned (>= lower bounds); also add the optional preprocessing deps
# (scanpy/anndata) and tifffile which the upstream conda recipe installs.
RUN uv pip install -r /opt/segjointgene/requirements.txt && \
    uv pip install tifffile scanpy anndata jupyterlab ipykernel papermill

RUN cd /opt/segjointgene && python scripts/check_env.py

WORKDIR /opt/segjointgene

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
