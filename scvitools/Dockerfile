ARG ubuntu_version=20.04

FROM ubuntu:$ubuntu_version

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
    scvi-tools scanpy==1.8.2 scarches jupyter \
    igraph==0.9.9 leidenalg==0.8.10
