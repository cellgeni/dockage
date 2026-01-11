FROM python:3.11-slim

RUN pip install --no-cache-dir uv
RUN apt-get update \
 && apt-get install -y procps \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN uv venv /opt/venv \
 && . /opt/venv/bin/activate \
 && uv pip install "vitessce[all]" spatialdata click

ENV PATH="/opt/venv/bin:$PATH"