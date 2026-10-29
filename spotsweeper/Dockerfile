# SpotSweeper - https://github.com/MicTott/SpotSweeper (Bioconductor)
# Spatially-aware quality control for spot-based spatial transcriptomics (e.g. 10x Visium):
# local outlier spots and large technical artifacts (R/Bioconductor).
FROM rocker/rstudio:4.6.1

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONNOUSERSITE=true

# SpotSweeper 1.8.0 is in Bioconductor 3.23 (R 4.6)
ARG BIOC_VERSION="3.23"

RUN apt-get update && apt-get install -y -qq --no-install-recommends \
        build-essential gfortran libxml2-dev libssl-dev libcurl4-openssl-dev \
        libglpk-dev libpng-dev libjpeg-dev libtiff-dev zlib1g-dev libicu-dev \
        libudunits2-dev libgdal-dev gdal-bin libgeos-dev libproj-dev libsqlite3-dev \
        libfontconfig1-dev libfreetype6-dev libharfbuzz-dev libfribidi-dev libcairo2-dev \
        libmagick++-dev procps git python3-venv python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Jupyter stack in a venv (for IRkernel / papermill)
RUN python3 -m venv "${VENV_PATH}" && \
    pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir jupyterlab ipykernel papermill

# Imports: SpatialExperiment, SummarizedExperiment, BiocNeighbors, SingleCellExperiment,
# escheR, MASS, ggplot2, spatialEco, BiocParallel. Suggests used in the vignette are added too.
RUN Rscript -e 'install.packages(c("BiocManager", "IRkernel", "remotes"))' && \
    Rscript -e 'BiocManager::install(version = "'${BIOC_VERSION}'", ask = FALSE, update = FALSE)' && \
    Rscript -e 'BiocManager::install(c("SpotSweeper", "scuttle", "STexampleData", "ggpubr"), ask = FALSE, update = FALSE)' && \
    Rscript -e 'library(SpotSweeper); message("SpotSweeper ", packageVersion("SpotSweeper"))' && \
    Rscript -e 'IRkernel::installspec(user = FALSE)'

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
