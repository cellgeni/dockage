FROM ubuntu:22.04

ARG SSAM_VERSION=1.1.3

ENV DEBIAN_FRONTEND=noninteractive
ENV NUMBA_CACHE_DIR=/tmp
ENV VIRTUAL_ENV=/env
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV UV_PYTHON_INSTALL_DIR=/opt/python
ENV UV_PYTHON=3.12

RUN apt-get update && apt-get install -y --no-install-recommends \
        vim procps git wget build-essential ca-certificates

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv python install "${UV_PYTHON}" \
    && uv venv --python "${UV_PYTHON}" "${VIRTUAL_ENV}"

RUN uv pip install pip setuptools && \
    uv pip install "ssam==${SSAM_VERSION}" && \
    uv pip install jupyterlab papermill shapely zarr matplotlib pandas tifffile imagecodecs pyarrow

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
