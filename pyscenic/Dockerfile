FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y cmake python-is-python3

RUN set -xe \
    && apt-get -y update \
    && apt-get -y install python3 \
    && apt-get -y install python3-dev \
    && apt-get -y install python3-pip 

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade --no-cache \
	scanpy pyscenic==0.11.2
