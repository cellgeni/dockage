FROM python:3.11-slim

# install UV for python packages
COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /uvx /bin/

# create a virtual environment
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
RUN uv venv "${VENV_PATH}"

# install system dependencies required by geopandas/rasterio
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgdal-dev \
    libspatialindex-dev \
    && rm -rf /var/lib/apt/lists/*

# install SegTraQ and jupyterlab/papermill for notebook support
RUN . "${VENV_PATH}/bin/activate" && \
    uv pip install "setuptools<82.0.0" && \
    uv pip install segtraq jupyterlab papermill

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker

ENTRYPOINT ["/env/bin/python"]
