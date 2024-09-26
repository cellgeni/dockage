FROM rocker/r-ver:4.2.2

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN Rscript -e "install.packages('BiocManager')"
RUN Rscript -e "install.packages(c('argparse', 'tidyr', 'tidyverse', 'dplyr', 'vcfR', 'lsa' 'R.utils'))"
RUN Rscript -e "BiocManager::install('ComplexHeatmap')"
