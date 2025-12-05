FROM rocker/rstudio:4.5.1

RUN apt-get update && \
    apt-get install -y git make build-essential zlib1g-dev libcurl4-openssl-dev libssl-dev \
     libfontconfig1-dev libfreetype6-dev libfribidi-dev libharfbuzz-dev \
     libjpeg-dev libpng-dev libtiff-dev pandoc libicu-dev libxml2-dev \
     libgit2-dev zlib1g-dev libgsl-dev libglpk-dev libgmp3-dev libpng-dev

RUN Rscript -e 'install.packages("pak")'
RUN Rscript -e 'pak::pkg_install("sparseMatrixStats")' 
RUN Rscript -e 'pak::pkg_install("SpatialExperiment")'
RUN Rscript -e 'pak::pkg_install("SummarizedExperiment")'
RUN Rscript -e 'pak::pkg_install("aaronkwc/DenoIST")'
RUN Rscript -e 'pak::pak("scverse/anndataR", dependencies = TRUE)'


COPY Dockerfile /docker/
RUN chmod -R 755 /docker

