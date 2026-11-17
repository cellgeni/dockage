# FICTURE - https://github.com/seqscope/ficture
# Segmentation-free factor analysis (LDA-style) for sub-micron resolution spatial
# transcriptomics (Seq-Scope, Stereo-seq, Visium HD, CosMx, MERSCOPE, Xenium...).
# CLI: `ficture run_together ...` (generates and runs a GNU Makefile) or individual steps.
# Licence: CC BY-NC 4.0.
FROM python:3.11-slim

ARG FICTURE_VERSION="0.0.5.7"

LABEL org.opencontainers.image.source="https://github.com/seqscope/ficture"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV MPLCONFIGDIR=/tmp
ENV QT_QPA_PLATFORM=offscreen

# run_together drives the pipeline through `make` and shells out to sort/gzip;
# the docs' manual steps also use perl, pigz, bgzip/tabix.
# PyQt5 (dependency of ete3) needs libGL/libglib/X libs at import time.
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git make gawk perl pigz tabix coreutils \
      libgl1 libglib2.0-0 libfontconfig1 libdbus-1-3 libxkbcommon0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python /usr/local/bin/python3.11

# Upstream tests with Python 3.11. Extra packages from requirements.txt not in the
# wheel's metadata (kneed, pypng, mpmath - mpmath used by de_bulk) are added.
RUN uv pip install --no-cache \
      "ficture==${FICTURE_VERSION}" \
      kneed pypng mpmath \
      jupyterlab ipykernel papermill

RUN ficture run_together -h > /dev/null && python -c "import ficture; from ficture.models.online_slda import OnlineLDA"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
