FROM ubuntu:22.04 AS builder

ARG WKDIR=/usr/local/src
WORKDIR ${WKDIR}

ARG VIPS_VERSION=8.16.0
ARG BF_VERSION=8.3.0
ARG PYTORCH_VERSION=2.4.0
ARG TORCHVISION_VERSION=0.20.1
ARG OPENCV_VERSION=4.9.0.80

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="/env/bin:${PATH}"
ENV TORCH_HOME=/opt/torch/
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SCYJAVA_DISABLE_JGO=1
ENV SCYJAVA_CLASSPATH=${WKDIR}/valis/bioformats_package.jar

COPY --from=ghcr.io/astral-sh/uv:0.8.14 /uv /uvx /bin/

# Get build dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
	build-essential software-properties-common \
	ninja-build python3-dev bc wget ca-certificates \
	git-all cmake libjxr-dev openjdk-11-jre procps \
        libglib2.0-dev \
        glib-2.0-dev \
        libexpat1-dev \
        libexpat-dev \
        librsvg2-2 \
        librsvg2-common \
        librsvg2-dev \
        libpng-dev \
        libjpeg-turbo8-dev \
        libopenjp2-7-dev \
        libtiff-dev \
        libexif-dev \
        liblcms2-dev \
        libheif-dev \
        liborc-dev \
        libgirepository1.0-dev \
        libopenslide-dev \
        librsvg2-dev

RUN update-ca-certificates && \
    uv venv /env

# libvips dependencies for libvips build
RUN . /env/bin/activate && \
    uv pip install meson

### Install libvips from source to get latest version
ENV LD_LIBRARY_PATH=/usr/local/lib
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

# build the head of the stable 8.14 branch
ARG VIPS_URL=https://github.com/libvips/libvips/releases/download
RUN wget ${VIPS_URL}/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.xz --no-check-certificate && \
    tar xf vips-${VIPS_VERSION}.tar.xz && \
    cd vips-${VIPS_VERSION} && \
    meson build --buildtype=release --libdir=lib -Dopenjpeg=enabled && \
    cd build && \
    ninja && ninja install && \
    rm ${WKDIR}/vips-${VIPS_VERSION}.tar.xz && \
    rm -r ${WKDIR}/vips-${VIPS_VERSION}

# Copy over necessary files
RUN git clone --depth 1 --branch v1.2.0 https://github.com/MathOnco/valis.git /tmp/src && \
    mv /tmp/src/valis . && \
    mv /tmp/src/LICENSE.txt . && \
    mv /tmp/src/CITATION.cff . && \
    mv /tmp/src/README.rst . && \
    mv /tmp/src/pyproject.toml . && \
    mv /tmp/src/docker/docker_download_weights.py . && \
    rm -rf /tmp/src
    
# RUN uv sync
RUN . /env/bin/activate && \
    uv pip install .

# Install bioformats.jar in valis
RUN wget https://downloads.openmicroscopy.org/bio-formats/${BF_VERSION}/artifacts/bioformats_package.jar -P valis

# Download pytorch model weights
RUN mkdir -p /opt/torch && \
    chmod a+rwx /opt/torch && \
    . /env/bin/activate && python3 docker_download_weights.py

# Clean up
RUN apt-get remove -y wget build-essential ninja-build && \
  apt-get autoremove -y && \
  apt-get autoclean && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  rm -rf /usr/local/lib/python*


COPY Dockerfile /docker/
RUN chmod -R 755 /docker

