FROM python:3.10-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        procps \
        pkg-config \
        default-libmysqlclient-dev \
        build-essential \
        gfortran \
        libopenblas-dev \
        liblapack-dev \
        default-jdk-headless \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade "pip<26" "setuptools<81" wheel \
    && pip install --no-cache-dir "numpy<2" cellprofiler-core
