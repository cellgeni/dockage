# Spotiphy - https://github.com/jyyulab/Spotiphy
# Deconvolution/decomposition of sequencing-based spatial transcriptomics (Visium etc.)
# into pseudo single-cell resolution images (pyro/torch model + StarDist nuclei segmentation).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG SPOTIPHY_VERSION="0.3.1"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
        python3.10 python3.10-dev \
        libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# squidpy 1.6.1 (pinned by spotiphy) needs Python >= 3.10.
RUN uv venv "${VENV_PATH}" --python python3.10

# setuptools>=81 dropped pkg_resources (and the distutils shim), which older deps still
# import at build and run time; keep it below 81 for every uv install in this image.
RUN echo "setuptools<81" > /etc/uv-constraints.txt
ENV UV_CONSTRAINT=/etc/uv-constraints.txt
ENV UV_BUILD_CONSTRAINT=/etc/uv-constraints.txt
RUN uv pip install --no-cache "setuptools<81"

# torch and tensorflow are not declared by spotiphy and must be installed manually
# (README: torch + tensorflow==2.16.2). torch drives the pyro deconvolution on GPU;
# tensorflow is only used by StarDist for nuclei segmentation.
RUN uv pip install --no-cache \
        torch==2.3.1 \
        --index-url https://download.pytorch.org/whl/cu121

RUN uv pip install --no-cache \
        tensorflow==2.16.2 \
        "spotiphy==${SPOTIPHY_VERSION}" \
        jupyterlab ipykernel papermill && \
    python -c "import spotiphy, torch, pyro, stardist; print('torch', torch.__version__)"

# NOTE: StarDist '2D_versatile_he' weights are downloaded on first use
# (StarDist2D.from_pretrained) into ~/.keras - needs network access at runtime.

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
