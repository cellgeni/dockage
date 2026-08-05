FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/env
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV UV_PYTHON_INSTALL_DIR=/opt/python
ENV UV_PYTHON=3.13

RUN apt-get update && apt-get install -y --no-install-recommends \
        vim procps git wget build-essential ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv python install "${UV_PYTHON}" \
    && uv venv --python "${UV_PYTHON}" "${VIRTUAL_ENV}"

RUN uv pip install "raw2features[all]"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
