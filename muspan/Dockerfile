# syntax=docker/dockerfile:1
# MuSpAn - https://www.muspan.co.uk (public issue tracker: https://github.com/MuSpAn-Multiscale-Spatial-Analysis/MuSpAn-Public)
# Multiscale spatial analysis toolbox for spatial omics / imaging data (spatial statistics,
# networks, topology, distributions, ...).
#
# MuSpAn is NOT publicly downloadable: it is distributed under an Academic Use Licence
# behind HTTP basic auth (request credentials at https://www.muspan.co.uk/get-the-code).
# Credentials are passed as BuildKit secrets so they do not end up in the image layers:
#
#   printf '%s' "$MUSPAN_USER" > muspan_user.txt
#   printf '%s' "$MUSPAN_PASS" > muspan_pass.txt   # URL-encode special characters
#   DOCKER_BUILDKIT=1 docker build \
#       --secret id=muspan_user,src=muspan_user.txt \
#       --secret id=muspan_pass,src=muspan_pass.txt \
#       -t muspan:1.2.5 .
#
# Licence note: images containing MuSpAn must not be redistributed outside the licence terms.
FROM python:3.12-slim

ARG MUSPAN_VERSION="v1.2.5"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_PREFERENCE=only-system \
    UV_NO_CACHE=1 \
    NUMBA_CACHE_DIR=/tmp

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
        libgeos-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# MuSpAn supports Python 3.10-3.13
RUN uv venv "${VENV_PATH}" --python /usr/local/bin/python3.12

RUN --mount=type=secret,id=muspan_user,required=true \
    --mount=type=secret,id=muspan_pass,required=true \
    MUSPAN_USER="$(cat /run/secrets/muspan_user)" && \
    MUSPAN_PASS="$(cat /run/secrets/muspan_pass)" && \
    uv pip install "https://${MUSPAN_USER}:${MUSPAN_PASS}@docs.muspan.co.uk/code/${MUSPAN_VERSION}.zip"

RUN uv pip install jupyterlab ipykernel papermill

RUN python -c "import muspan as ms; print('MuSpAn installed')"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
