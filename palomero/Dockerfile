# Palomero - https://github.com/Yu-AnChen/palomero
# CLI (and optional web app) to align whole-slide images stored in OMERO (palom coarse
# affine + itk-elastix non-rigid) and transfer ROIs between them.
# Usage: omero login -s <server> -u <user> ...; palomero --help; palomero-web
FROM ubuntu:22.04

ARG PALOMERO_VERSION="2026.7.2"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates \
        libgl1 libglib2.0-0 libbz2-1.0 libssl3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Python 3.10 to match Glencoe's prebuilt zeroc-ice (omero-py dependency) wheel, as in
# upstream's pixi environment.
RUN uv venv "${VENV_PATH}" --python 3.10

# Install exactly what upstream's release pixi.toml installs: the zeroc-ice wheel and the
# released palomero wheel with the web-app extra (pulls omero-py, ezomero fork, palom,
# itk-elastix, python-fasthtml).
RUN uv pip install \
        "https://github.com/glencoesoftware/zeroc-ice-py-linux-x86_64/releases/download/20240202/zeroc_ice-3.6.5-cp310-cp310-manylinux_2_28_x86_64.whl" \
        "palomero[webapp] @ https://github.com/Yu-AnChen/palomero/releases/download/v${PALOMERO_VERSION}/palomero-${PALOMERO_VERSION}-py3-none-any.whl" \
        jupyterlab ipykernel papermill

RUN palomero --help > /dev/null && python -c "import omero, palom, itk; print('ok')"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
