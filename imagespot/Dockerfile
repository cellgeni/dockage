FROM ubuntu:22.04

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONNOUSERSITE=1
ENV LANG=C.UTF-8
ENV CONDA_PATH=/opt/conda
ENV PATH="${CONDA_PATH}/bin:${PATH}"

RUN apt-get update && \
    apt-get install --no-install-recommends --yes \
        wget curl unzip g++ vim wget ca-certificates git \
        software-properties-common build-essential \
        openslide-tools libxml2-dev libxslt-dev bzip2 \
        fonts-liberation locales && \
    apt-get clean && \
    echo "$LANG UTF-8" > /etc/locale.gen && \
    locale-gen && \
    rm -rf /var/lib/apt/lists/*

# install miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && /bin/bash /tmp/miniconda.sh -b -p "${CONDA_PATH}" \
    && rm /tmp/miniconda.sh

RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda create -n imagespot_cpu -c conda-forge python=3.9 && \
    conda activate imagespot_cpu && \
    conda install -c conda-forge scanpy python-igraph leidenalg && \
    conda install -c conda-forge jupyterlab 

RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate imagespot_cpu && \
    pip install \
      scikit-learn \
      scikit-image \
      opencv-python \
      jupyter_bokeh \
      bokeh

RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate imagespot_cpu && \
    ipython kernel install --name imagespot_cpu

COPY jupyter-annotator /tmp/jupyter-annotator
RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate imagespot_cpu && \
    cd /tmp/jupyter-annotator && \
    pip install .

RUN mkdir -p /.singularity.d/env && \
    chmod -R a+rx /.singularity.d/env && \
    echo '. "${CONDA_PATH}/etc/profile.d/conda.sh"' >> /.singularity.d/env/99-conda.sh && \
    echo "conda activate imagespot_cpu" >> /.singularity.d/env/99-conda.sh && \ 
    cat /.singularity.d/env/99-conda.sh >> ~/.bashrc

