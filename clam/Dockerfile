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
    git clone https://github.com/mahmoodlab/CLAM.git /tmp/CLAM && \
    sed -i '/^prefix/d' /tmp/CLAM/docs/clam.yaml && \
    sed -i 's/pytorch=1.3.1/pytorch=1.4.0/g' /tmp/CLAM/docs/clam.yaml && \
    conda env create -f /tmp/CLAM/docs/clam.yaml

# install smooth-topk
RUN git clone https://github.com/oval-group/smooth-topk.git /tmp/smooth-topk && \
    . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate $CLAM_ENV_NAME && \
    cd /tmp/smooth-topk && \
    python setup.py install

RUN rm -rf /tmp/CLAM /tmp/smooth-topk && conda clean -afy

RUN mkdir -p /.singularity.d/env && \
    chmod -R a+rx /.singularity.d/env && \
    echo '. "${CONDA_PATH}/etc/profile.d/conda.sh"' >> /.singularity.d/env/99-conda.sh && \
    echo "conda activate $CLAM_ENV_NAME" >> /.singularity.d/env/99-conda.sh && \ 
    cat /.singularity.d/env/99-conda.sh >> ~/.bashrc
