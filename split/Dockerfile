# SPLIT - https://github.com/bdsc-tds/SPLIT
# R package (Spatial Purification of Layered Intracellular Transcripts): removes transcript
# spillover/contamination from imaging- and sequencing-based spatial data (Xenium, Visium HD,
# ATERA) using RCTD (spacexr) or any other deconvolution output.
FROM rocker/rstudio:4.5.2

ARG SPLIT_VERSION="v0.3.0"
ARG SPACEXR_COMMIT="9f5dc33c8060f946c6072a138b70e189636e1435"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates build-essential cmake \
        libxml2-dev libssl-dev libcurl4-openssl-dev libhdf5-dev libglpk-dev libgmp3-dev \
        libpng-dev libjpeg-dev libtiff-dev libfontconfig1-dev libfreetype6-dev \
        libharfbuzz-dev libfribidi-dev libicu-dev zlib1g-dev libzstd-dev liblz4-dev \
        libudunits2-dev libgdal-dev libgeos-dev libproj-dev \
        python3 python3-venv python3-dev pandoc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Jupyter (for IRkernel) in a venv
RUN python3 -m venv "${VENV_PATH}" && \
    pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir jupyterlab ipykernel papermill

# Dependencies from SPLIT's DESCRIPTION (rocker images point CRAN at Posit binaries)
RUN Rscript -e 'install.packages(c("BiocManager", "remotes", "IRkernel"))' && \
    Rscript -e 'BiocManager::install(c("S4Vectors", "SingleCellExperiment", "rhdf5", "BiocParallel"), ask = FALSE, update = FALSE)' && \
    Rscript -e 'install.packages(c("Matrix", "dplyr", "magrittr", "rlang", "forcats", "entropy", "ggplot2", "scatterpie", "Seurat", "igraph", "arrow", "knitr", "rmarkdown"))'

RUN Rscript -e 'remotes::install_github("dmcable/spacexr@'"${SPACEXR_COMMIT}"'", upgrade = "never")' && \
    Rscript -e 'remotes::install_github("bdsc-tds/SPLIT@'"${SPLIT_VERSION}"'", upgrade = "never")' && \
    Rscript -e 'library(SPLIT); library(spacexr); library(Seurat)'

RUN Rscript -e 'IRkernel::installspec(user = FALSE)'

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
