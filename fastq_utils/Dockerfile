FROM ubuntu:22.04

ARG FASTQ_UTILS_VERSION=0.25.3

RUN apt-get update -y && apt-get install -y \
        build-essential libbz2-dev libncurses5-dev zlib1g-dev xz-utils \
        git gcc wget make liblzma-dev

WORKDIR /fastq_utils
RUN wget https://github.com/nunofonseca/fastq_utils/archive/refs/tags/${FASTQ_UTILS_VERSION}.tar.gz
RUN tar xvf "${FASTQ_UTILS_VERSION}.tar.gz" 
RUN cd "fastq_utils-${FASTQ_UTILS_VERSION}" && \
    ./install_deps.sh && \
    make && make install && \
    rm -rf test* && \
    chmod a+x bin/* && \
    cp bin/* /usr/bin
RUN rm -rf /fastq_utils

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
