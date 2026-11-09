# MDV (Multi-Dimensional Viewer) - https://github.com/Taylor-CCB-Group/MDV (PyPI: mdvtools)
# Web-based viewer for large single-cell / spatial / tabular data. The mdvtools wheel
# bundles the pre-built frontend, so projects can be created and served locally
# without node/pnpm; use the bundled `mdv-serve` launcher (not serve_project, which only
# binds the container's loopback) -> http://localhost:5050.
# This installs the slim core; the multi-user DB/chat/auth server (`mdvtools[app]`,
# Postgres + gunicorn) is better run from upstream's own docker-compose setup.
FROM python:3.12-slim

ARG MDVTOOLS_VERSION="1.3.0"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# libhdf5-dev: upstream installs it for h5py; build-essential for any sdist fallbacks.
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python python3.12

RUN uv pip install --no-cache \
        "mdvtools==${MDVTOOLS_VERSION}" \
        jupyterlab ipykernel papermill && \
    mdvtools --help > /dev/null

# serve_project() binds Flask to the container's loopback only, so a published port is
# unreachable. mdv-serve wraps create_app() with a container-aware bind address: 0.0.0.0
# under Docker/Podman, 127.0.0.1 under Singularity (host network) - see its docstring:
#   docker run --rm -p 127.0.0.1:5050:5050 -v $PWD/proj:/proj mdv mdv-serve /proj
# Publish on the host loopback only - the viewer has no authentication.
COPY mdv-serve /usr/local/bin/mdv-serve
RUN chmod 755 /usr/local/bin/mdv-serve && mdv-serve --help > /dev/null

EXPOSE 5050

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
