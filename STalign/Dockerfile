# STalign - alignment of spatial transcriptomics data via diffeomorphic metric mapping (LDDMM)
# https://github.com/JEFworks-Lab/STalign
# Aligns ST sections to each other, to H&E images, or to 3D atlases (e.g. Allen CCF).
# CPU image: v2.0 ships an optional C++ engine (built here) that is much faster than the
# torch backend on CPU; GPU is not needed.
FROM python:3.12-slim

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

# STalign is not on PyPI and 2.0.0 is not tagged upstream; pin the commit that bumps to 2.0.0.
ARG STALIGN_VERSION=2.0.0
ARG STALIGN_COMMIT=8a84bf1facc5173f7155400867a09c302125904e

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_PREFERENCE=only-system \
    UV_NO_CACHE=1 \
    MPLCONFIGDIR=/tmp \
    NUMBA_CACHE_DIR=/tmp

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# build-essential (g++ with C++17) compiles the optional STalign._stalign_cpp engine.
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git ca-certificates build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python /usr/local/bin/python3.12

# CPU-only torch keeps the image small. scanpy/anndata/tifffile are commonly used in the
# tutorials for reading Xenium/MERFISH/Visium data and images.
RUN uv pip install --torch-backend=cpu \
        torch \
        "STalign @ git+https://github.com/JEFworks-Lab/STalign.git@${STALIGN_COMMIT}" \
        scanpy anndata tifffile \
        jupyterlab ipykernel papermill

# Fail the build if the C++ engine silently fell back to torch.
RUN python -c "import STalign, STalign._stalign_cpp, torch; \
assert STalign.__version__ == '${STALIGN_VERSION}', STalign.__version__; \
print('STalign', STalign.__version__, 'torch', torch.__version__, 'cpp engine OK')"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
