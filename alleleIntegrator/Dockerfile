FROM rocker/r-ver:4.4.1

# Use bash as default shell
SHELL ["/bin/bash", "-c"]

# Install alleleCounter
COPY --from=quay.io/wtsicgp/allelecount:v4.3.0 /opt/wtsi-cgp/bin/alleleCounter /bin/

# Install parallel and bcftools
RUN apt-get update && \
    apt-get install -y -qq --no-install-recommends \
    zlib1g-dev libbz2-dev liblzma-dev libpng-dev libxml2-dev  parallel bcftools libcurl4-openssl-dev libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install "easy" packages
RUN R -e "install.packages('devtools')" && \
    R -e "install.packages('pak')" && \
    R -e "install.packages('BiocManager')" && \
    R -e "install.packages('tidyverse')" && \
    R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/grr/grr_0.9.5.tar.gz', repos = NULL, type = 'source')" && \
    R -e "install.packages('https://cran.r-project.org/src/contrib/Archive/Matrix.utils/Matrix.utils_0.9.8.tar.gz', repos = NULL, type = 'source')"

# Install ASCAT (no, I can't use devtools)
RUN R -e "pak::pkg_install('VanLoo-lab/ascat/ASCAT@v3.2.0')"

# Install missing Bioconductor dependencies for alleleIntegrator
RUN R -e "BiocManager::install(c('DelayedArray', 'Rsamtools', 'VariantAnnotation', 'rtracklayer', 'GenomicFeatures', 'ComplexHeatmap', 'SNPRelate'))"

# Install AlleleIntegrator (no, I can't use pak)
RUN R -e "devtools::install_github('constantAmateur/alleleIntegrator')"

# Clean up temporary files
RUN rm -rf /tmp/*

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
