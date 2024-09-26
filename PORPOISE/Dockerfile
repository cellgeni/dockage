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

ENV CLAM_ENV_NAME=deep_learning

# install CLAM
RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    git clone https://github.com/mahmoodlab/PORPOISE.git /tmp/PORPOISE && \
    sed -i '/^prefix/d' /tmp/PORPOISE/docs/clam.yaml && \
    sed -i 's/pytorch=1.3.1/pytorch=1.6.0/g' /tmp/PORPOISE/docs/clam.yaml && \
    conda env create -f /tmp/PORPOISE/docs/clam.yaml

# install smooth-topk
RUN git clone https://github.com/oval-group/smooth-topk.git /tmp/smooth-topk && \
    . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate $CLAM_ENV_NAME && \
    cd /tmp/smooth-topk && \
    python setup.py install

# install torch-scatter/sparse/cluster/spline-conv/geometric
RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate $CLAM_ENV_NAME && \
    pip install \
      torch_scatter==2.0.6 \
      torch_sparse==0.6.9 \
      torch_cluster==1.5.9 \
      torch_spline_conv==1.2.1 \
      torch_geometric==1.6.3 \
         -f https://data.pyg.org/whl/torch-1.6.0+cu101.html

# install even more undocumented stuff (lifelines, scikit-survival)
RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate $CLAM_ENV_NAME && \
    pip install lifelines==0.26.0 && \
    conda install -c sebp scikit-survival

RUN rm -rf /tmp/PORPOISE /tmp/smooth-topk && conda clean -afy

RUN mkdir -p /.singularity.d/env && \
    chmod -R a+rx /.singularity.d/env && \
    echo '. "${CONDA_PATH}/etc/profile.d/conda.sh"' >> /.singularity.d/env/99-conda.sh && \
    echo "conda activate $CLAM_ENV_NAME" >> /.singularity.d/env/99-conda.sh && \ 
    cat /.singularity.d/env/99-conda.sh >> ~/.bashrc

