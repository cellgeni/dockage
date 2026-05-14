FROM ubuntu:22.04

# Configure the environment
ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV="/env"
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
ENV UV_PYTHON_INSTALL_DIR=/opt/python
ENV UV_PYTHON=3.10
ENV VIRTUAL_ENV=/env
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv python install ${UV_PYTHON} && \
    uv venv --python "${UV_PYTHON}" "${VIRTUAL_ENV}"

# Install the required Python packages
RUN uv pip install pip setuptools wheel && \
    uv pip install 'palom[all]' 'numpy<2' openslide-python openslide-bin tifffile imagecodecs numcodecs tiledb zarr pyarrow pandas fire && \
    uv pip install jupyterlab papermill

# Copy Dockerfile to the image
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
