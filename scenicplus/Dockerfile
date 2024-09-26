FROM python:3.11

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV MALLET_PATH="/opt/Mallet"
RUN python -m venv "${VENV_PATH}"

RUN apt-get update && apt-get install -y \
      build-essential libcurl4-openssl-dev zlib1g-dev libfftw3-dev libc++-dev hdf5-tools \
      openjdk-17-jdk-headless libbz2-dev liblzma-dev procps libfftw3-dev ant

RUN git clone https://github.com/aertslab/scenicplus /tmp/scenicplus
RUN . "${VENV_PATH}/bin/activate" && \
    pip install -r /tmp/scenicplus/requirements.txt --no-cache-dir && \
    pip install /tmp/scenicplus

RUN . "${VENV_PATH}/bin/activate" && \
    pip install jupyterlab papermill

RUN mkdir -p /usr/share/man/man1 && \
    git clone --depth=1 https://github.com/mimno/Mallet.git "${MALLET_PATH}" && \
    cd "${MALLET_PATH}" && ant

ENV PATH="${VENV_PATH}/bin:$PATH"
ENV PATH="${MALLET_PATH}/bin:$PATH"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
