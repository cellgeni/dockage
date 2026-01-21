# syntax=docker/dockerfile:1
FROM rocker/r-base:4.4.1

RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates build-essential gcc-13 g++-13 gfortran-13 \
    libcurl4-openssl-dev libssl-dev libxml2-dev \
    libicu-dev libfontconfig1-dev libfreetype6-dev libharfbuzz-dev libfribidi-dev \
    libpng-dev libjpeg-dev libtiff-dev pandoc \
  && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 100 \
  && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-13 100 \
  && update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-13 100 \
  && rm -rf /var/lib/apt/lists/*

RUN printf "%s\n" \
    "CC=gcc-13" \
    "CXX=g++-13" \
    "CXX11=g++-13" \
    "CXX14=g++-13" \
    "CXX17=g++-13" \
    "FC=gfortran-13" \
  > /etc/R/Makevars.site

RUN echo 'options(repos = c(CRAN = "https://packagemanager.rstudio.com/all/__linux__/bookworm/latest"))' > /etc/R/Rprofile.site

RUN Rscript -e 'install.packages(c("remotes","anndata"), repos = "https://cloud.r-project.org")' \
  && Rscript -e 'remotes::install_github("saezlab/DOT")'

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
