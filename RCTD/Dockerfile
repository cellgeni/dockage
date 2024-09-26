FROM rocker/r-base:4.3.1

RUN apt-get update && \
    apt-get install -y make build-essential zlib1g-dev libcurl4-openssl-dev libssl-dev \
     libfontconfig1-dev libfreetype6-dev libfribidi-dev libharfbuzz-dev \
     libjpeg-dev libpng-dev libtiff-dev pandoc libicu-dev libxml2-dev git \
     libgit2-dev zlib1g-dev libgsl-dev libglpk-dev libgmp3-dev libpng-dev \
     python3 python3-dev

RUN echo 'options(repos = c(REPO_NAME = "https://packagemanager.rstudio.com/all/__linux__/bookworm/latest"))' > ~/.Rprofile
RUN Rscript -e 'install.packages(c("devtools","BiocManager"))'
RUN Rscript -e 'devtools::install_github("dmcable/spacexr")'

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
