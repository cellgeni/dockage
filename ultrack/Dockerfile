# Ultrack - large-scale multi-hypothesis cell tracking
# https://github.com/royerlab/ultrack
# Tracks cells in 2D/3D time-lapse microscopy from candidate segmentation hierarchies via ILP (PyTorch/CuPy/cuCIM GPU acceleration).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL org.opencontainers.image.authors="Tong Li <tl10@sanger.ac.uk>"

ARG ULTRACK_VERSION=0.8.0

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_INSTALL_DIR="/opt/python"
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
# napari (a hard dependency of ultrack) needs a Qt backend; run headless by default
ENV QT_QPA_PLATFORM=offscreen

# Qt/OpenGL runtime libs for napari/pyqt5; xvfb for `xvfb-run` when a real X display is needed
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git build-essential ca-certificates \
      libgl1 libegl1 libglib2.0-0 libfontconfig1 libdbus-1-3 \
      libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
      libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-xfixes0 \
      libxcb-shape0 libxcb-cursor0 x11-utils xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ultrack 0.8.0 requires python >=3.11,<3.14
RUN uv venv ${VENV_PATH} --python 3.12

# torch pinned in the same resolve so it is not upgraded to a non-cu121 build.
# cupy + cucim are the optional GPU image-processing extras recommended upstream.
# gurobipy is installed as an ultrack dependency, but a Gurobi licence (free academic)
# must be provided at runtime (e.g. mount gurobi.lic and set GRB_LICENSE_FILE);
# without one ultrack falls back to the open-source CBC solver via python-mip.
RUN uv pip install --no-cache --torch-backend=cu121 \
      torch==2.5.1 \
      "ultrack==${ULTRACK_VERSION}" \
      "cupy-cuda12x==14.2.0" \
      "cucim-cu12==26.10.0" \
      "napari[pyqt5]" \
      jupyterlab ipykernel papermill

RUN ultrack --help > /dev/null && \
    python -c "import ultrack, torch, importlib.metadata as m; print('ultrack', m.version('ultrack'), 'torch', torch.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
