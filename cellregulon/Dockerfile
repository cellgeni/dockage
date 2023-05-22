FROM ubuntu:22.04

SHELL ["/bin/bash", "-c"]

ENV PYTHONNOUSERSITE=1
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV CONDA_PATH=/opt/conda
ENV PATH="${CONDA_PATH}/bin:${PATH}"
ENV PYTHON_VERSION="3.7"

RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends \
      bzip2 ca-certificates fonts-liberation locales wget vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "C.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# install miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && /bin/bash /tmp/miniconda.sh -b -p "${CONDA_PATH}" \
    && rm /tmp/miniconda.sh

# install python packages
COPY scenic.yaml /tmp/environment.yml
RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda env create -f /tmp/environment.yml && \
    conda clean -ya

ARG THE_CONDA_ENV="scenic"
# add kernel
RUN . "${CONDA_PATH}/etc/profile.d/conda.sh" && \
    conda activate ${THE_CONDA_ENV} && \
    python -m ipykernel install --name ${THE_CONDA_ENV}

# setup environment to activate conda
# we shouldn't be doing this but it works
# https://docs.sylabs.io/guides/latest/user-guide/environment_and_metadata.html#singularity-d-directory
RUN mkdir -p /.singularity.d/env && \
    chmod -R a+rx /.singularity.d/env && \
    echo '. "${CONDA_PATH}/etc/profile.d/conda.sh"' >> /.singularity.d/env/99-conda.sh && \
    echo "conda activate ${THE_CONDA_ENV}" >> /.singularity.d/env/99-conda.sh && \
    cat /.singularity.d/env/99-conda.sh >> ~/.bashrc

CMD pyscenic -h
