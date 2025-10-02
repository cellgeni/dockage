FROM python:3.10

# Configure the environment
ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"

# Install the required Python packages
RUN python -m venv "${VENV_PATH}" && \
    . "${VENV_PATH}/bin/activate" && \
    pip install -U pip setuptools wheel && \
    pip install palom tiledb zarr pyarrow pandas fire && \
    pip install jupyterlab papermill

# Copy Dockerfile to the image
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
