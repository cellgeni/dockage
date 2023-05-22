FROM rocker/r-ver:4.1.2

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends apt-utils

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential software-properties-common wget unzip tabix \
    liblzma-dev libbz2-dev zlib1g libpng-dev libxml2-dev gfortran-7 libglpk-dev libhdf5-dev libcurl4-openssl-dev \
    python3.8 python3-dev python3-pip python-is-python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH="/opt/conda/condabin:${PATH}"

RUN conda update -n base conda && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda

COPY conda.yml /tmp/conda.yml

RUN conda env update -n base --file /tmp/conda.yml

RUN Rscript -e "install.packages(c('BiocManager','remotes'))"

RUN Rscript -e "BiocManager::install(c('GSVA', 'limma', 'ComplexHeatmap'))"

RUN Rscript -e "remotes::install_github('navinlabcode/copykat')"

RUN Rscript -e "remotes::install_github('linxihui/NNLM')"

RUN Rscript -e "remotes::install_github('Miaoyx323/stCancer')"
