FROM rocker/r-ver:4.1.3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends --yes \
        wget vim wget ca-certificates git \
        software-properties-common build-essential \
        libcurl4-openssl-dev libssl-dev libglpk-dev libgmp3-dev \
        libxml2-dev libxslt-dev libpng-dev liblzma-dev libbz2-dev \
        make zlib1g-dev pandoc libicu-dev gfortran libhdf5-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN Rscript -e "install.packages(c('BiocManager', 'devtools'))"
RUN Rscript -e "install.packages(c('Matrix', 'ggplot2', 'Seurat', 'R.utils', 'DropletUtils'))"
RUN Rscript -e "devtools::install_github('constantAmateur/SoupX', ref = 'devel')"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
