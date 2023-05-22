FROM r-base:4.1.0

RUN set -xe \
    && apt-get -y update \
    && apt-get -y install libcurl4-openssl-dev \ 
    && apt-get -y install libssl-dev \
    && apt-get -y install libhdf5-dev \
    && apt-get -y install libxml2-dev \
    && apt-get -y install libboost-all-dev \
    && apt-get -y install freetype2-doc \
    && apt-get -y install libfontconfig1-dev 

# Install BiocManager
RUN Rscript -e 'install.packages(c("remotes", "BiocManager"))' && \
    Rscript -e 'BiocManager::install()'

RUN Rscript -e 'remotes::install_github(c( \
    "r-lib/systemfonts", "davidgohel/ggiraph"))'

# Install Bioconductor packages
RUN Rscript -e 'BiocManager::install(c( \
    "GeomxTools", "GeoMxWorkflows", "NanoStringNCTools"))'
