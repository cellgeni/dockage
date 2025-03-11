FROM rocker/r-ver:4.3.1

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH=/env
ENV PATH=$VENV_PATH/bin:$VENV_PATH:$PATH
ENV NUMBA_CACHE_DIR=/tmp

RUN apt-get update && apt-get install -y \
        python3 python3-dev python3-pip python3-venv python-is-python3 \
        libpcre2-dev libbz2-dev zlib1g-dev liblzma-dev libcurl4-openssl-dev \
        libxml2-dev libicu-dev libcairo2-dev \
        build-essential software-properties-common  git

RUN python -m venv $VENV_PATH && \
    . $VENV_PATH/bin/activate && \
    pip install jupyterlab setuptools wheel && \
    pip install 'scanpy[leiden]'

RUN . $VENV_PATH/bin/activate && \ 
    pip install anndata2ri

RUN Rscript -e "install.packages(c('BiocManager', 'statmod','tidyverse','reshape2','patchwork'))" && \
    Rscript -e "BiocManager::install('edgeR')"

RUN . $VENV_PATH/bin/activate && \ 
    git clone --depth 1 https://github.com/emdann/milopy.git /opt/milopy && \
    cd /opt/milopy && \
    pip install .

COPY Dockerfile /docker/
RUN chmod -R 755 /docker

ENTRYPOINT ["/env/bin/python"]
