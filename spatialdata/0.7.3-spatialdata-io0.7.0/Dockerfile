FROM python:3.11-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        git && \
    rm -rf /var/lib/apt/lists/*

ENV UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

RUN pip install --no-cache-dir uv

RUN uv pip install --system --no-cache \
    fire \
    numpy \
    shapely \
    spatialdata==0.7.3 \
    spatialdata-io==0.7.0

COPY Dockerfile /docker

RUN chmod -R 755 /docker && \
    chmod -R 755 /opt
