# CellSeg3D (napari-cellseg3d) - https://github.com/AdaptiveMotorControlLab/CellSeg3D
# Self-supervised / supervised 3D cell segmentation (WNet3D, SwinUNetR, SegResNet...)
# for fluorescence volumes; napari plugin that can also be used as a Python library.
# Pretrained weights are downloaded by the plugin on first use (not baked in).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG CELLSEG3D_VERSION="0.2.4"

LABEL org.opencontainers.image.source="https://github.com/AdaptiveMotorControlLab/CellSeg3D"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

# build-essential: pydensecrf2 is sdist-only (Cython/C++ build).
# Qt/X11/GL libs: napari[all] ships PyQt5, needed for the GUI and for importing
# the plugin modules. OpenCL ICD loader (+ pocl CPU fallback) for pyclesperanto;
# the nvidia.icd entry lets it use the GPU when run with --nv / --gpus.
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git curl ca-certificates build-essential \
      python3.10 python3.10-dev python3.10-venv \
      libgl1 libegl1 libglib2.0-0 libfontconfig1 libdbus-1-3 \
      libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
      libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 \
      libxcb-xfixes0 libxcb-cursor0 libx11-xcb1 libxrender1 libxi6 \
      ocl-icd-libopencl1 pocl-opencl-icd clinfo \
    && mkdir -p /etc/OpenCL/vendors \
    && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv venv ${VENV_PATH} --python python3.10

# torch 2.5.1 is the last release with cu121 wheels; monai>=1.5 needs torch>=2.4.
RUN uv pip install --no-cache \
      torch==2.5.1+cu121 \
      torchvision==0.20.1+cu121 \
      --extra-index-url https://download.pytorch.org/whl/cu121

# onnx-cpu rather than onnx-gpu: current onnxruntime-gpu wheels need cuDNN 9 (base has cuDNN 8);
# ONNX models are only an optional inference path - torch models use the GPU.
RUN uv pip install --no-cache \
      "torch==2.5.1+cu121" "torchvision==0.20.1+cu121" \
      "napari-cellseg3d[crf,onnx-cpu]==${CELLSEG3D_VERSION}" \
      jupyterlab ipykernel papermill ipywidgets \
      --extra-index-url https://download.pytorch.org/whl/cu121 \
      --index-strategy unsafe-best-match

RUN python -c "import torch, monai, napari_cellseg3d; print('torch', torch.__version__, 'monai', monai.__version__)"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
