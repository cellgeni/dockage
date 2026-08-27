FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:$PATH" \
    UV_PYTHON=3.12 \
    UV_PYTHON_INSTALL_DIR=/opt/python

# ── 1. System packages ────────────────────────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        git \
        build-essential \
        libgomp1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# ── 2. uv + Python 3.12 venv ──────────────────────────────────────────────────
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv python install ${UV_PYTHON} && \
        uv venv --python "${UV_PYTHON}" "${VIRTUAL_ENV}"

# ── 3. PyTorch (CUDA 12.1) ────────────────────────────────────────────────────
RUN uv pip install --no-cache \
        "torch==2.3.1+cu121" \
        --index-url https://download.pytorch.org/whl/cu121

# ── 4. DOTpy runtime dependencies ────────────────────────────────────────────
RUN uv pip install --no-cache \
        "numpy>=1.20.0" \
        "scanpy>=1.9.0" \
        "anndata>=0.8.0" \
        "matplotlib>=3.5.0" \
        "scikit-learn>=1.0.0" \
        "scipy>=1.7.0" \
        "squidpy>=1.5.0" \
        "scikit-misc>=0.3.1" \
        pandas \
        natsort

# ── 5. DOTpy ──────────────────────────────────────────────────────────────────
RUN git clone --depth 1 https://github.com/earmingol/DOTpy.git /opt/DOTpy \
    && uv pip install --no-cache /opt/DOTpy

# ── 6. JupyterLab + papermill ─────────────────────────────────────────────────
RUN uv pip install --no-cache \
        "jupyterlab==4.2.5" \
        "papermill==2.6.0"


# ── 7. Dockerfile provenance ───────────────────────────────────────────────────
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
