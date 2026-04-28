FROM python:3.12-slim AS gdal-builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake ninja-build g++ \
    libopenjp2-7-dev \
    libsqlite3-dev libproj-dev \
    libgeos-dev libcurl4-openssl-dev \
    libexpat1-dev libtiff-dev libzstd-dev \
    wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget -qO /tmp/gdal.tar.gz https://github.com/OSGeo/gdal/releases/download/v3.10.2/gdal-3.10.2.tar.gz && \
    tar xf /tmp/gdal.tar.gz -C /tmp && rm /tmp/gdal.tar.gz

# Inject custom JP2000 LibTIFF codec + apply source patches
COPY tif_jp2000.h /tmp/gdal-3.10.2/frmts/gtiff/
COPY tif_jp2000.c /tmp/gdal-3.10.2/frmts/gtiff/libtiff/
COPY patch_gdal.py /tmp/
RUN python3 /tmp/patch_gdal.py

# Build patched GDAL with OpenJPEG compiled in
RUN cmake -S /tmp/gdal-3.10.2 -B /tmp/gdal-build \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        -DGDAL_USE_OPENJPEG=ON \
        -DGDAL_ENABLE_DRIVER_JP2OPENJPEG_PLUGIN=OFF \
        -DGDAL_USE_TIFF_INTERNAL=ON \
        -DGDAL_USE_GEOTIFF_INTERNAL=ON \
        -DGDAL_USE_GEOS=ON \
        -DGDAL_USE_CURL=ON \
        -DGDAL_USE_SQLITE3=ON \
        -DGDAL_USE_PROJ=ON && \
    ninja -C /tmp/gdal-build -j$(nproc) && \
    ninja -C /tmp/gdal-build install && \
    rm -rf /tmp/gdal-3.10.2 /tmp/gdal-build


FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY --from=gdal-builder /usr/local /usr/local

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libopenjp2-7 libsqlite3-0 libproj25 \
    libgeos-c1t64 libcurl4t64 libexpat1 libtiff6 libzstd1 \
    && rm -rf /var/lib/apt/lists/*

ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV GDAL_VERSION=3.10.2
ENV GDAL_INCLUDE_PATH=/usr/local/include
ENV GDAL_LIBRARY_PATH=/usr/local/lib
ENV LD_LIBRARY_PATH=/usr/local/lib

RUN uv venv --python python3.12 "${VENV_PATH}" && \
    uv pip install --no-binary rasterio rasterio==1.5.0


FROM python:3.12-slim

ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV LD_LIBRARY_PATH=/usr/local/lib
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=gdal-builder /usr/local /usr/local
COPY --from=builder /env /env

RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenjp2-7 libsqlite3-0 libproj25 \
    libgeos-c1t64 libcurl4t64 libexpat1 libtiff6 libzstd1 \
    procps \
    && rm -rf /var/lib/apt/lists/* && ldconfig

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
