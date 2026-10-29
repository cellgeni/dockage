# syntax=docker/dockerfile:1
# point_cloud_linking - link/register 3D point clouds (e.g. spot or nuclei centroids)
# across imaging cycles: trackpy for nearest-neighbour linking, probreg for
# rigid/non-rigid point-set registration, spatialdata for I/O.
FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# probreg ships no prebuilt wheel (sdist only) and builds two C++ extensions
# (pybind11 + Eigen3, vendored/fetched by its own setup.py), so it needs a
# compiler toolchain. Its open3d dependency links libGL/libEGL/libX11, libgomp,
# libusb and libidn2 at import time even though nothing here renders or touches a
# camera - the runtime libs below satisfy that headlessly.
# procps provides `ps`, which Nextflow needs for task metrics.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libgl1 libegl1 libx11-6 libgomp1 libusb-1.0-0 libidn2-0 \
        procps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# setuptools>=81 dropped pkg_resources, which spatialdata's xarray_schema
# dependency still imports at module load time - pin below that.
# aicsimageio caps zarr at 2.15, which needs numcodecs<0.16 (0.16 dropped
# numcodecs.blosc.cbuffer_sizes).
RUN python -m pip install --upgrade pip wheel \
    && python -m pip install \
        "setuptools<81" \
        "numcodecs<0.16" \
        "pandas==2.3.3" \
        "scipy==1.15.3" \
        "trackpy==0.7" \
        "probreg==0.3.8" \
        "spatialdata==0.5.0" \
        "aicsimageio==4.14.0" \
        "readlif==0.6.6" \
        "fire==0.7.1" \
    && python -c "import trackpy, probreg, spatialdata, aicsimageio, readlif, fire"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
