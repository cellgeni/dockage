FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

LABEL description="GLUE single-cell multi-omics integration environment"

# System packages: Python 3.10, bedtools (pybedtools runtime), build tools for
# C-extension packages (leidenalg/igraph), and HDF5/XML dev headers
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3.10 \
        python3.10-dev \
        python3-pip \
        bedtools \
        build-essential \
        git \
        libhdf5-dev \
        libxml2-dev \
    && ln -sf /usr/bin/python3.10 /usr/local/bin/python \
    && ln -sf /usr/bin/python3.10 /usr/local/bin/python3 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade --no-cache-dir pip

# Install PyTorch with CUDA 12.1 wheels (matches the driver base image)
RUN pip install --no-cache-dir \
    torch \
    --index-url https://download.pytorch.org/whl/cu121

# Install faiss with CUDA 12 support for GPU-accelerated k-means
RUN pip install --no-cache-dir faiss-gpu-cu12

# Install all runtime dependencies before copying source so this layer is
# cached independently of local code changes.
RUN pip install --no-cache-dir \
    # scglue declared dependencies (pyproject.toml)
    "numpy>=1.19" \
    "scipy>=1.3" \
    "pandas>=1.1" \
    "matplotlib>=3.1.2" \
    "seaborn>=0.9" \
    "dill>=0.2.3" \
    "tqdm>=4.27" \
    "scikit-learn>=0.21.2" \
    "statsmodels>=0.10" \
    "parse>=1.3.2" \
    "networkx>=2" \
    "pynvml>=8.0.1" \
    "pytorch-ignite>=0.4.1" \
    "pyro-ppl>=1.0" \
    "tensorboardX>=1.4" \
    "anndata>=0.7" \
    "scanpy>=1.5" \
    "pybedtools>=0.8.1" \
    "h5py>=2.10" \
    "sparse>=0.3.1" \
    "packaging>=16.8" \
    "leidenalg>=0.7" \
    "muon>=0.1.5" \
    # additional deps
    "pynndescent" \
    "numba" \
    "scikit-network" \
    # notebook execution and interactive use
    "jupyterlab" \
    "papermill"

# Install scglue from source (pyproject.toml / flit_core build backend)
COPY GLUE/ /opt/scglue/
RUN pip install --no-cache-dir /opt/scglue

WORKDIR /workspace

# To run JupyterLab:
#   singularity exec --nv container.sif jupyter lab --ip=0.0.0.0 --no-browser
# To run papermill:
#   singularity exec --nv container.sif papermill input.ipynb output.ipynb

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
