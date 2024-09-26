FROM rocker/r-base:4.4.0

# set OCI labels
LABEL org.opencontainers.image.authors="Pasha Mazin <pavel.mazin@sanger.ac.uk>"
LABEL org.opencontainers.image.title="reticulate-free single cell format conversion"
LABEL org.opencontainers.image.description="Package to load scanpy h5ad into R as list, SingleCellExperiment or Seurat object."
LABEL org.opencontainers.image.source="https://github.com/cellgeni/schard"
LABEL org.opencontainers.image.licenses="GPL-3"

# os packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y make zlib1g-dev libcurl4-openssl-dev libssl-dev \
     libfontconfig1-dev libfreetype6-dev libfribidi-dev libharfbuzz-dev \
     libjpeg-dev libpng-dev libtiff-dev pandoc libicu-dev libxml2-dev git \
     libgit2-dev zlib1g-dev libglpk-dev libgmp3-dev libhdf5-dev python3

# required for installing
RUN Rscript -e 'install.packages(c("remotes"))'

# schard
RUN Rscript -e 'remotes::install_github("cellgeni/schard", upgrade = "always", dependencies = TRUE)'

