FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG STARDIST_VERSION=0.9.2

# Configure the environment
ENV DEBIAN_FRONTEND=noninteractive
ENV NUMBA_CACHE_DIR=/tmp
ENV VIRTUAL_ENV="/env"
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
ENV UV_PYTHON_INSTALL_DIR=/opt/python
ENV UV_PYTHON=3.11

RUN apt-get update && apt-get install -y \
        vim procps git wget build-essential

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv python install "${UV_PYTHON}" && \
    uv venv --python "${UV_PYTHON}" "${VIRTUAL_ENV}"

# Install the required Python packages
RUN uv pip install pip setuptools wheel && \
    uv pip install 'tensorflow[and-cuda]==2.15.*' && \
    uv pip install stardist=="${STARDIST_VERSION}" csbdeep gputools edt && \
    uv pip install shapely zarr tqdm 'numpy<2' pandas tifffile imagecodecs openslide-python openslide-bin numcodecs pyarrow fire dask scikit-image && \
    uv pip install jupyterlab papermill

# Copy Dockerfile to the image
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
