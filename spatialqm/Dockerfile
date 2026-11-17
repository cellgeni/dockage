# SpatialQM - https://github.com/Center-for-Spatial-OMICs/SpatialQM
# Quality-control metrics for imaging-based spatial transcriptomics
# (Xenium, CosMx, MERSCOPE) from Seurat / SingleCellExperiment / SpatialExperiment.
FROM rocker/rstudio:4.5.2

SHELL ["/bin/bash", "-c"]

# No release tags upstream - pin a commit.
ARG SPATIALQM_COMMIT="36e1a59d4ca3f8f360a1d826f5e999d9f40c6760"
# GitHub-only Imports (no Remotes: field in DESCRIPTION, so install them explicitly).
ARG SPACEXR_COMMIT="9f5dc33c8060f946c6072a138b70e189636e1435"
ARG INSITUTYPE_COMMIT="f3ef0dd0814318d74675e6a613fad3ef7f1e23a1"

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"

RUN apt-get update && apt-get install -y -qq --no-install-recommends \
        build-essential gfortran git curl procps \
        libxml2-dev libssl-dev libcurl4-openssl-dev libhdf5-dev libglpk-dev \
        libgsl0-dev libudunits2-dev libgdal-dev libgeos-dev libproj-dev \
        libpng-dev libjpeg-dev libtiff-dev libfftw3-dev libmagick++-dev \
        libcairo2-dev libharfbuzz-dev libfribidi-dev libfreetype6-dev libfontconfig1-dev \
        zlib1g-dev libbz2-dev liblzma-dev libicu-dev pandoc \
        python3-venv python3-dev libzmq3-dev \
    && rm -rf /var/lib/apt/lists/*

# Jupyter stack in a venv (for IRkernel / papermill)
RUN python3 -m venv "${VENV_PATH}" && \
    pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir jupyterlab ipykernel papermill

RUN Rscript -e 'install.packages(c("pak", "remotes", "BiocManager"))'

# CRAN + Bioconductor Imports (pak resolves Bioconductor packages automatically).
RUN Rscript -e 'pak::pkg_install(c( \
        "Seurat", "dplyr", "ggplot2", "shadowtext", "scales", "cowplot", "data.table", \
        "Matrix", "matrixStats", "fs", "gridExtra", "magrittr", "tibble", "lsa", "coop", \
        "bioc::SingleCellExperiment", "bioc::SpatialExperiment", "bioc::bluster", \
        "bioc::BiocParallel", "bioc::BioQC", "bioc::scater", \
        "bioc::SpatialFeatureExperiment", "bioc::Voyager", \
        "knitr", "rmarkdown", "R.utils", "IRkernel"))'

# NMI was archived from CRAN (2026-05) - install the last release from the archive
# (pak's url:: resolver fails on it, so fetch and install the tarball directly).
RUN curl -fsSL -o /tmp/NMI_2.0.tar.gz https://cran.r-project.org/src/contrib/Archive/NMI/NMI_2.0.tar.gz && \
    R CMD INSTALL /tmp/NMI_2.0.tar.gz && \
    rm /tmp/NMI_2.0.tar.gz

# GitHub-only dependencies: spacexr (RCTD) and InSituType.
RUN Rscript -e 'pak::pkg_install(c( \
        "dmcable/spacexr@'"${SPACEXR_COMMIT}"'", \
        "Nanostring-Biostats/InSituType@'"${INSITUTYPE_COMMIT}"'"))'

RUN Rscript -e 'remotes::install_github("Center-for-Spatial-OMICs/SpatialQM@'"${SPATIALQM_COMMIT}"'", dependencies = FALSE, upgrade = "never")' && \
    Rscript -e 'library(SpatialQM)' && \
    Rscript -e 'IRkernel::installspec(user = FALSE)'

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
