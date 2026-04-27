FROM python:3.12-slim

ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install runtime library required by rasterio's GDAL wheel
RUN apt-get update && apt-get install -y --no-install-recommends \
    libexpat1 \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment and install rasterio
RUN python -m venv "${VENV_PATH}" && \
    "${VENV_PATH}/bin/pip" install --no-cache-dir --upgrade pip && \
    "${VENV_PATH}/bin/pip" install --no-cache-dir rasterio==1.5.0

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
