FROM ubuntu:18.04

# install os packages
RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
        vim curl unzip g++ wget ca-certificates git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# see http://bugs.python.org/issue19846
ENV LANG C.UTF-8

# install miniconda3 - https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && /bin/bash /tmp/miniconda.sh -b -p /opt/conda \
    && rm /tmp/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

COPY environment.yml /tmp/
RUN conda env create -f /tmp/environment.yml
RUN conda clean --all --yes --quiet 

RUN echo "source activate bavaria" > ~/.bashrc
ENV PATH /opt/conda/envs/bavaria/bin:$PATH
RUN cat ~/.bashrc > /.singularity_bashrc

