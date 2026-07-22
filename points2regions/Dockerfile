FROM ubuntu:22.04

ARG POINTS2REGIONS_VERSION=0.0.6

ENV DEBIAN_FRONTEND=noninteractive
ENV NUMBA_CACHE_DIR=/tmp
ENV VIRTUAL_ENV=/env
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV UV_PYTHON_INSTALL_DIR=/opt/python
ENV UV_PYTHON=3.13

RUN apt-get update && apt-get install -y --no-install-recommends \
        vim procps git wget build-essential ca-certificates

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv python install "${UV_PYTHON}" \
    && uv venv --python "${UV_PYTHON}" "${VIRTUAL_ENV}"

RUN uv pip install pip wheel &&\
    uv pip install "points2regions==${POINTS2REGIONS_VERSION}" "numpy<2" && \
    uv pip install jupyterlab papermill shapely zarr matplotlib pandas tifffile imagecodecs pyarrow

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
