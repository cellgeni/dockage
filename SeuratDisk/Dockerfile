FROM rocker/r-ver:4.3.0

RUN apt-get update && \
    apt-get install -y zlib1g-dev libicu-dev libcurl4-openssl-dev \
        libssl-dev libglpk-dev libgmp3-dev libxml2-dev libpng-dev \
        python3 make libhdf5-dev build-essential

# rocker images pin packages to the date of the release of the image
# this change will make it use the latest aviable packages instead
RUN sed 's@jammy/[0-9]\{4\}\-[0-9]\{2\}\-[0-9]\{2\}@jammy/latest@g' -i /usr/local/lib/R/etc/Rprofile.site

RUN Rscript -e 'install.packages(c("devtools","BiocManager"))'
# install all the stuff
RUN Rscript -e 'BiocManager::install("Seurat")'
RUN Rscript -e 'devtools::install_github("mojaveazure/seurat-object","seurat5")' && \ 
    Rscript -e 'devtools::install_github("satijalab/seurat-data")' && \
    Rscript -e 'devtools::install_github("mojaveazure/seurat-disk")'

COPY Dockerfile /
RUN chmod -R 755 /docker
