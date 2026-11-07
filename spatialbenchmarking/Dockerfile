# SpatialBenchmarking - https://github.com/QuKunLab/SpatialBenchmarking
# Li et al. 2022 Nat Methods: benchmark of spatial + scRNA-seq integration methods.
# This image reproduces the *gene prediction / imputation* environment
# (Benchmarking/SpatialGenes.py): SpaGE, SpaOTsc, novoSpaRc, gimVI (scvi-tools),
# Tangram, stPlus (Python) and Seurat, LIGER (R, called via Rscript).
#
# Notes / deviations from upstream (conda env Benchmarkingenvironment.yml: python 3.6.13, R 3.6.1):
#  - No conda: Python 3.8 (Ubuntu focal system python) with the upstream pip pins where
#    they have cp38 wheels; R 4.1.3 with Seurat 4 (upstream: Seurat 3.2.0) and
#    liger 0.5.0.9000 (tag v0.5.0, the old `library(liger)` API used by Codes/Impute/LIGER.r).
#  - CPU-only torch (gimVI/Tangram/stPlus run on CPU; pass device='cpu').
#  - The *deconvolution* part (Cell2location 0.6a0, RCTD, SpatialDWLS/Giotto, SPOTlight,
#    STRIDE, DSTG, DestVI, Stereoscope) needs many mutually-incompatible old environments
#    and is NOT included; see the separate cell2location/RCTD/Giotto images in this repo.
#  - Upstream code uses repo-relative paths (Extenrnal/..., Codes/...), so run from
#    /opt/SpatialBenchmarking (it is on PYTHONPATH: `import Benchmarking.SpatialGenes`).
FROM rocker/rstudio:4.1.3

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV VIRTUAL_ENV="${VENV_PATH}"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true
ENV UV_PYTHON_PREFERENCE=only-system
ENV NUMBA_CACHE_DIR=/tmp
ENV MPLCONFIGDIR=/tmp

# Repo has no releases; pin last commit
ARG SPATIALBENCHMARKING_COMMIT="3586b9d81c479f939aa40adedfe1c95c5b496bcb"
ARG LIGER_TAG="v0.5.0"

RUN apt-get update && apt-get install -y -qq --no-install-recommends \
        build-essential gfortran cmake procps git curl ca-certificates \
        python3.8 python3.8-dev python3.8-venv \
        libxml2-dev libssl-dev libcurl4-openssl-dev libglpk-dev libgmp3-dev \
        libpng-dev libjpeg-dev zlib1g-dev libicu-dev libhdf5-dev \
        libfontconfig1-dev libfreetype6-dev libharfbuzz-dev libfribidi-dev libcairo2-dev \
        libgsl-dev libzmq3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/QuKunLab/SpatialBenchmarking.git /opt/SpatialBenchmarking && \
    cd /opt/SpatialBenchmarking && \
    git checkout "${SPATIALBENCHMARKING_COMMIT}"

# ---- Python environment ----
RUN uv venv ${VENV_PATH} --python python3.8

# CPU torch matching the upstream pin (torch==1.9.0); stPlus needs torchvision
RUN uv pip install --no-cache \
      torch==1.9.0+cpu torchvision==0.10.0+cpu \
      -f https://download.pytorch.org/whl/torch_stable.html

# Core pins taken from Benchmarkingenvironment.yml
RUN uv pip install --no-cache \
      numpy==1.19.5 \
      scipy==1.5.4 \
      pandas==1.1.5 \
      scikit-learn==0.24.2 \
      matplotlib==3.3.4 \
      seaborn==0.11.1 \
      statsmodels==0.12.2 \
      h5py==3.1.0 \
      numba==0.53.1 \
      llvmlite==0.36.0 \
      umap-learn==0.5.1 \
      pynndescent==0.5.2 \
      networkx==2.5 \
      python-igraph==0.9.1 \
      louvain==0.7.0 \
      POT==0.7.0 \
      anndata==0.7.6 \
      scanpy==1.7.2 \
      hyperopt==0.1.2 \
      scvi-tools==0.8.0b0 \
      novosparc==0.4.3 \
      stPlus==0.0.6 \
      tangram-sc==1.0.0 \
      tables==3.6.1 \
      xlrd==1.2.0 \
      tqdm

# Keep numpy at the upstream pin for every later install (SpaOTsc deps otherwise pull
# numpy 1.24, which breaks numba 0.53's compiled extensions; bezier 2020.5.19 is the
# last release that allows numpy 1.19).
RUN echo "numpy==1.19.5" > /etc/uv-constraints.txt
ENV UV_CONSTRAINT=/etc/uv-constraints.txt

# SpaOTsc (vendored in Extenrnal/SpaOTsc). Its requirements.txt pins 2019-era packages
# (astropy 2.0.3, pytest 4.6, ...) that do not build on py3.8; install the modules it imports.
RUN uv pip install --no-cache \
      "dit==1.2.3" "astropy<5" "bezier==2020.5.19" "progressbar==2.5" && \
    uv pip install --no-cache --no-deps /opt/SpatialBenchmarking/Extenrnal/SpaOTsc

RUN uv pip install --no-cache jupyterlab ipykernel papermill

# stPlus 0.0.6 sets the default tensor type to torch.cuda.FloatTensor at import, which fails
# with this CPU-only torch; only do that when CUDA is actually available.
RUN sed -i "s/^torch.set_default_tensor_type('torch.cuda.FloatTensor')$/if torch.cuda.is_available(): torch.set_default_tensor_type('torch.cuda.FloatTensor')/" \
      ${VENV_PATH}/lib/python3.8/site-packages/stPlus/model.py && \
    grep -q "if torch.cuda.is_available(): torch.set_default_tensor_type" ${VENV_PATH}/lib/python3.8/site-packages/stPlus/model.py

ENV PYTHONPATH="/opt/SpatialBenchmarking:/opt/SpatialBenchmarking/Extenrnal/SpaGE-master"

# ---- R environment (Seurat / LIGER imputation via Rscript) ----
# rocker/rstudio:4.1.3 pins CRAN to a 2022 Posit Package Manager snapshot
RUN Rscript -e 'install.packages(c("remotes", "IRkernel", "Seurat", "plyr", "Matrix", "ggplot2", "data.table", "dplyr"))' && \
    Rscript -e 'remotes::install_version("riverplot", version = "0.10", upgrade = "never")' && \
    Rscript -e 'remotes::install_github("welch-lab/liger@'${LIGER_TAG}'", upgrade = "never")' && \
    Rscript -e 'library(liger); library(Seurat); message("Seurat ", packageVersion("Seurat"), ", liger ", packageVersion("liger"))' && \
    Rscript -e 'IRkernel::installspec(user = FALSE)'

RUN python -c "import scvi, tangram, novosparc, stPlus, spaotsc, SpaGE.main; from scvi.model import GIMVI; print('scvi', scvi.__version__)"

WORKDIR /opt/SpatialBenchmarking

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
