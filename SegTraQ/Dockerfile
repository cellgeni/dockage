FROM python:3.13-slim

# install UV for python packages
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# create a virtual environment
ENV VIRTUAL_ENV="/env"
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
RUN uv venv "${VIRTUAL_ENV}"

# install system dependencies required by geopandas/rasterio
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgdal-dev libspatialindex-dev procps \
    && rm -rf /var/lib/apt/lists/*

# install SegTraQ and jupyterlab/papermill for notebook support
RUN . "${VIRTUAL_ENV}/bin/activate" && \
    uv pip install pip "setuptools<82.0.0" && \
    uv pip install segtraq 'scanpy[leiden]' spatialdata-io jupyterlab papermill

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker

