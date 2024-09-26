FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y cmake 

RUN set -xe \
    && apt-get -y update \
    && apt-get -y install python3 \
    && apt-get -y install python3-dev \
    && apt-get -y install python3-pip \
    && apt-get -y install python-is-python3  

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade --no-cache \
    scvi-tools scanpy scarches jupyterlab papermill igraph leidenalg

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
