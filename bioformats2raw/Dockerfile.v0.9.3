FROM ubuntu:22.04

ARG BF2RAW_VERSION="0.9.3"
ARG RAW2OME_VERSION="0.7.1"

SHELL ["/bin/bash", "-c"]

# set envs
ENV DEBIAN_FRONTEND=noninteractive

# install base OS packages
RUN apt-get update && \
     apt-get install -y --no-install-recommends \
      git wget unzip procps binutils libblosc-dev libjpeg-turbo8-dev openjdk-18-jre-headless
ENV JAVA_HOME="/usr/lib/jvm/java-18-openjdk-amd64"

# get bioformats2raw
RUN wget -q "https://github.com/glencoesoftware/bioformats2raw/releases/download/v${BF2RAW_VERSION}/bioformats2raw-${BF2RAW_VERSION}.zip" -O /tmp/bioformats2raw.zip && \
    unzip /tmp/bioformats2raw.zip -d /opt/ && \
    mv "/opt/bioformats2raw-${BF2RAW_VERSION}" /opt/bioformats2raw && \
    chmod +x /opt/bioformats2raw/bin/* && \
    rm /tmp/bioformats2raw.zip
ENV PATH="/opt/bioformats2raw/bin:${PATH}"

# get raw2ometiff
RUN wget -q "https://github.com/glencoesoftware/raw2ometiff/releases/download/v${RAW2OME_VERSION}/raw2ometiff-${RAW2OME_VERSION}.zip" -O /tmp/raw2ometiff.zip && \
    unzip /tmp/raw2ometiff.zip -d /opt/ && \
    mv "/opt/raw2ometiff-${RAW2OME_VERSION}" /opt/raw2ometiff && \
    chmod +x /opt/raw2ometiff/bin/* && \
    rm /tmp/raw2ometiff.zip
ENV PATH="/opt/raw2ometiff/bin:${PATH}"

# get bftools
RUN wget -q "https://downloads.openmicroscopy.org/bio-formats/latest/artifacts/bftools.zip" -O /tmp/bftools.zip && \
    unzip /tmp/bftools.zip -d /opt/ && \
    chmod +x /opt/bftools/* && \
    rm /tmp/bftools.zip
ENV PATH="/opt/bftools:${PATH}"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker