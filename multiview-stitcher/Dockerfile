# syntax=docker/dockerfile:1
# multiview-stitcher - registration and fusion of large imaging datasets in 2D and 3D
# https://github.com/multiview-stitcher/multiview-stitcher
# Requires Python >=3.11.
FROM python:3.12-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends procps libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install \
        "multiview-stitcher[ants,itk-elastix,czi,imaris,distributed]==0.1.62" \
        jupyterlab \
        ipykernel \
        papermill

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
