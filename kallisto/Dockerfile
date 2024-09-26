FROM r-base:4.0.4

RUN apt-get -y update && apt-get -y install \
    libcurl4-openssl-dev libssl-dev \
    libhdf5-dev libxml2-dev libboost-all-dev

# Install BiocManager
RUN Rscript -e 'install.packages(c("remotes", "BiocManager"))' && \
    Rscript -e 'BiocManager::install()'

# Install Bioconductor packages
RUN Rscript -e 'BiocManager::install(c( \
    "DropletUtils", \ 
    "BSgenome.Mmusculus.UCSC.mm10", \ 
    "AnnotationHub", "SingleR", "pcaMethods"))'

# Install github packages
RUN Rscript -e 'library(remotes)'
RUN Rscript -e 'remotes::install_github(c( \
    "BUStools/BUSpaRse", \ 
    "satijalab/seurat-wrappers", \
    "velocyto-team/velocyto.R"))'
