FROM python:3.12-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        git \
        procps && \
    rm -rf /var/lib/apt/lists/*

ENV UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

RUN pip install --no-cache-dir uv

RUN uv pip install --system --no-cache \
    fire \
    numpy \
    shapely \
    spatialdata==0.9.0 \
    spatialdata-io==0.7.2

COPY Dockerfile /docker

RUN chmod -R 755 /docker && \
    chmod -R 755 /opt
