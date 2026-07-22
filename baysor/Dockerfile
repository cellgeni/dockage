ARG BAYSOR_VERSION=cpp-0.8.2

FROM ubuntu:22.04 AS build

ARG BAYSOR_VERSION

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates lsb-release wget \
    && wget https://packages.apache.org/artifactory/arrow/$(lsb_release --id --short | tr 'A-Z' 'a-z')/apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb \
    && apt-get install -y --no-install-recommends ./apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb \
    && rm -f ./apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb \
    && apt-get update && apt-get install -y --no-install-recommends \
       build-essential cmake ninja-build pkg-config  git libeigen3-dev \
       libomp-dev libspdlog-dev libcgal-dev libarrow-dev libparquet-dev \
       libhdf5-dev nlohmann-json3-dev libtiff-dev \
    && rm -rf /var/lib/apt/lists/*

RUN wget "https://github.com/kharchenkolab/Baysor/archive/refs/tags/${BAYSOR_VERSION}.tar.gz" -O /tmp/src.tar.gz && \
    tar -xvf /tmp/src.tar.gz -C /opt


WORKDIR "/opt/Baysor-${BAYSOR_VERSION}"

RUN cmake -S . -B build -GNinja -DBAYSOR_WITH_TESTS=OFF
RUN cmake --build build --target baysor -j"$(nproc)"

FROM ubuntu:22.04

ARG BAYSOR_VERSION
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates lsb-release wget \
    && wget https://packages.apache.org/artifactory/arrow/$(lsb_release --id --short | tr 'A-Z' 'a-z')/apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb \
    && apt-get install -y --no-install-recommends ./apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb \
    && rm -f ./apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb \
    && apt-get update && apt-get install -y --no-install-recommends \
       libeigen3-dev libomp-dev libspdlog-dev libcgal-dev \
       libarrow-dev libparquet-dev libhdf5-dev nlohmann-json3-dev libtiff-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build "/opt/Baysor-${BAYSOR_VERSION}/build/baysor" /usr/local/bin/baysor

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
