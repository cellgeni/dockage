# InSituPy - https://github.com/SpatialPathology/InSituPy (PyPI: insitupy-spatial)
# Histology-guided, multi-sample analysis of single-cell spatial omics data (Xenium etc.),
# with a napari-based interactive viewer.
FROM python:3.12-slim

ARG INSITUPY_VERSION="0.12.1"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp
# napari/Qt is pulled in by the base install; default to headless rendering.
# Override (e.g. QT_QPA_PLATFORM=xcb) when running with an X display.
ENV QT_QPA_PLATFORM=offscreen

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Runtime libs for opencv-python and napari[all] (PyQt / vispy OpenGL).
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git build-essential ca-certificates \
        libgl1 libegl1 libglib2.0-0 libgomp1 libfontconfig1 libdbus-1-3 \
        libxkbcommon0 libxkbcommon-x11-0 libx11-xcb1 libxrender1 libxi6 libxext6 \
        libxcb1 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 \
        libxcb-render-util0 libxcb-shape0 libxcb-xfixes0 libxcb-xinerama0 libxcb-cursor0 \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python python3.12

# Base install includes napari[all]; [spatialdata] adds spatialdata/spatialdata-io I/O.
RUN uv pip install --no-cache \
        "insitupy-spatial[spatialdata]==${INSITUPY_VERSION}" \
        jupyterlab ipykernel papermill && \
    python -c "import insitupy; print('insitupy', insitupy.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
