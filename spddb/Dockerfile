# spDDB - https://github.com/Zafar-Lab/spDDB
# Benchmark of spatial deconvolution / domain-detection methods. This image covers the
# reusable parts of the repo: the SynthST simulator (synthetic cell-type proportions and
# spatial gene expression) and spDDB's evaluation metrics (incl. LISI via rpy2, mclust).
# The ~35 benchmarked methods each need their own environment (Environments/*.yml) and
# are NOT installed here. Code is cloned to /opt/spDDB; `import SynthST` works via PYTHONPATH.
# Python deps follow Environments/SynthST.yml (originally Python 3.9 / conda).
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ARG SPDDB_COMMIT="d3b2bec027726acb47fe5a57b0ea8bb1dffea380"
ARG LISI_COMMIT="a917556310d8d2c66833dcc35aa3d0f4d1b6e0f4"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_NO_CACHE=1 \
    NUMBA_CACHE_DIR=/tmp \
    PYTHONPATH=/opt/spDDB/SynthST/Simulator_CTP:/opt/spDDB/Experiments/_Deconvolution_Metrics_Calculation:/opt/spDDB/Experiments/_Domain_Detection_Metrics_Calculation

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# R (for rpy2: mclust in SynthST.utils.mclust_R, lisi in the domain-detection metrics)
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential \
        r-base r-base-dev r-cran-mclust r-cran-remotes r-cran-rcpp r-cran-rcpparmadillo \
        libcurl4-openssl-dev libssl-dev libxml2-dev libreadline-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN Rscript -e 'options(repos = c(CRAN = "https://cloud.r-project.org")); remotes::install_github("immunogenomics/LISI@'"${LISI_COMMIT}"'", upgrade = "never")' && \
    Rscript -e 'library(mclust); library(lisi)'

RUN uv venv "${VENV_PATH}" --python 3.10

# torch 2.1.2 as in SynthST.yml
RUN uv pip install \
        torch==2.1.2 \
        --index-url https://download.pytorch.org/whl/cu121

# squidpy (used by some metric notebooks) needs pandas>=2.1, so pandas is bumped from the
# yml's 2.0.3 to 2.1.4 (squidpy 1.2.x would need numpy<1.23).
# SynthST uses tensorflow.compat.v1 graph mode. SynthST.yml pins TF 2.13 (CUDA 11.8);
# TF 2.15 is the closest release built for CUDA 12 and still on Keras 2.
RUN uv pip install \
        tensorflow==2.15.1 \
        numpy==1.26.4 \
        pandas==2.1.4 \
        scipy==1.10.1 \
        scikit-learn==1.3.0 \
        anndata==0.9.2 \
        scanpy==1.9.3 \
        squidpy==1.4.1 \
        matplotlib==3.7.2 \
        seaborn==0.12.2 \
        rpy2==3.5.14 \
        diptest \
        tqdm Pillow \
        jupyterlab ipykernel papermill

RUN git clone https://github.com/Zafar-Lab/spDDB.git /opt/spDDB && \
    cd /opt/spDDB && \
    git checkout "${SPDDB_COMMIT}"

RUN python -c "import SynthST, torch, tensorflow, rpy2.robjects; print('ok')"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
