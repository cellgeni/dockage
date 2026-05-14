FROM rocker/rstudio:4.4.3

RUN git clone https://github.com/bioFAM/MOFA2.git
WORKDIR /MOFA2
RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-venv python3-pip \
       libcurl4-openssl-dev libcairo2-dev libfreetype6-dev \
       libpng-dev libtiff5-dev libjpeg-dev libxt-dev libharfbuzz-dev libfribidi-dev

# Install mofapy2
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install -U pip setuptools wheel && \
    pip install 'git+https://github.com/bioFAM/mofapy2.git@master'

# Install bioconductor dependencies
RUN R --vanilla -e "\
  if (!requireNamespace('BiocManager', quietly = TRUE)) install.packages('BiocManager', repos = 'https://cran.r-project.org'); \
  sapply(c('rhdf5', 'dplyr', 'tidyr', 'reshape2', 'pheatmap', 'corrplot', \
           'ggplot2', 'ggbeeswarm', 'scales', 'GGally', 'doParallel', 'RColorBrewer', \
           'cowplot', 'ggrepel', 'foreach', 'reticulate', 'HDF5Array', 'DelayedArray', \
           'ggpubr', 'forcats', 'Rtsne', 'uwot', \
           'systemfonts', 'ragg', 'Cairo', 'ggrastr', 'basilisk', 'mvtnorm'), \ 
         BiocManager::install)"
RUN R CMD INSTALL --build .


COPY Dockerfile /docker/
RUN chmod -R 755 /docker
