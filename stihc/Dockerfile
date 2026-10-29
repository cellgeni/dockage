# stIHC - https://github.com/CatherineH1/stIHC (CRAN: https://cran.r-project.org/package=stIHC)
# Spatial Transcriptomics Iterative Hierarchical Clustering: clusters spatially variable
# genes into spatial co-expression modules (R).
FROM rocker/rstudio:4.6.1

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
# rgl (an stIHC dependency) needs libGLU and has no display in containers; use its null device.
ENV RGL_USE_NULL=TRUE
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true

ARG STIHC_VERSION="0.1.1"

RUN apt-get update && apt-get install -y -qq --no-install-recommends \
        build-essential gfortran libxml2-dev libssl-dev libcurl4-openssl-dev \
        libblas-dev liblapack-dev libglpk-dev libpng-dev zlib1g-dev libicu-dev \
        procps git python3-venv python3-dev tcl8.6 tk8.6 libzmq3-dev libglu1-mesa libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Jupyter stack in a venv (for IRkernel / papermill)
RUN python3 -m venv "${VENV_PATH}" && \
    pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir jupyterlab ipykernel papermill

# stIHC (Imports: fdaPDE, cluster, mclust) + packages used in upstream simulations.R
RUN Rscript -e 'install.packages(c("remotes", "IRkernel", "fda", "clusterCrit", "cluster", "mclust", "fdaPDE"))' && \
    Rscript -e 'remotes::install_version("stIHC", version = "'${STIHC_VERSION}'", upgrade = "never")' && \
    Rscript -e 'library(stIHC); stopifnot(packageVersion("stIHC") == "'${STIHC_VERSION}'")' && \
    Rscript -e 'IRkernel::installspec(user = FALSE)'

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
