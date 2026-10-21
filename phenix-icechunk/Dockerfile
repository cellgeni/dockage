# syntax=docker/dockerfile:1
# phenix-icechunk - Opera Phenix / Harmony Index.xml export as a virtual OME-Zarr plate in icechunk
# https://github.com/BioinfoTongLI/phenix-icechunk
# Requires Python >=3.12.
FROM python:3.12-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends procps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install \
        "phenix-icechunk[extras]==0.3.0" \
        jupyterlab \
        ipykernel \
        papermill

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
