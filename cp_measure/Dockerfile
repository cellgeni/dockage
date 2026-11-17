# cp_measure - https://github.com/afermg/cp_measure
# CellProfiler's object/image measurements (intensity, shape, texture, granularity,
# colocalisation, ...) as a plain Python API on numpy masks/images.
FROM python:3.12-slim

ARG CP_MEASURE_VERSION="0.3.0"

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

# build-essential in case centrosome/mahotas need building from sdist
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git ca-certificates build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python /usr/local/bin/python3.12

# [numba] enables the JIT-accelerated measurements; tifffile/pandas/pyarrow for I/O.
RUN uv pip install \
        "cp-measure[numba]==${CP_MEASURE_VERSION}" \
        tifffile imagecodecs pandas pyarrow \
        jupyterlab ipykernel papermill

RUN python -c "import cp_measure.bulk"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
