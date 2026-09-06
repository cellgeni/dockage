# syntax=docker/dockerfile:1
# pyapr - Adaptive Particle Representation for volumetric images
# https://github.com/AdaptiveParticles/pyapr
# Wheels are published up to cp311 only, hence Python 3.11.
FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# `import pyapr` pulls in pyapr.viewer, which imports PyQt5/pyqtgraph at module
# level - so the Qt runtime .so's must be present even though nothing here
# renders. QT_QPA_PLATFORM=offscreen keeps Qt from looking for a display; the
# libxcb-* packages below are not needed for that path, they are there so the
# interactive viewers still work over X11 forwarding.
ENV QT_QPA_PLATFORM=offscreen

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libdbus-1-3 \
        libegl1 \
        libfontconfig1 \
        libgl1 \
        libglib2.0-0 \
        libxkbcommon-x11-0 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
        libxcb-randr0 \
        libxcb-render-util0 \
        libxcb-shape0 \
        libxcb-xinerama0 \
        libxrender1 \
        procps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# pyapr's pybind11 extension is built against the NumPy 1.x C-API, so NumPy 2
# would break it at import time.
RUN python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install \
        "numpy<2" \
        "pyapr==1.0.7" \
        tifffile \
        jupyterlab \
        ipykernel \
        papermill \
        fire

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
