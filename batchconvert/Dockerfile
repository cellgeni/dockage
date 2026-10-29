# BatchConvert - https://github.com/Euro-BioImaging/BatchConvert
# Nextflow-based CLI that batch-converts image collections to OME-TIFF (bfconvert)
# or OME-Zarr (bioformats2raw) in parallel.
# The default profile is switched from `conda` to `manual` (tools on PATH), e.g.
#   batchconvert omezarr /path/in /path/out
# User config/params are written to $HOME/.batchconvert.
# Not included: go-mc (MinIO client, s3 transfer - upstream binaries no longer
# distributed) and aspera-cli (BioImage Archive transfer), so only local/mounted
# input and output paths are supported.
# No package release (tags stop at v0.0.4, recipe is 0.0.6): pinned to a git commit.
FROM ubuntu:22.04

ARG BATCHCONVERT_COMMIT="9015e71c431fc238bde2ba6033f6567a0d9ea172"
ARG NXF_VER="24.10.5"
ARG BF2RAW_VERSION="0.12.1"
ARG BFTOOLS_VERSION="8.3.0"

LABEL org.opencontainers.image.source="https://github.com/Euro-BioImaging/BatchConvert"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm

# python-is-python3: BatchConvert's bin/ scripts use `#!/usr/bin/env python` (stdlib only).
# ncurses-bin provides `tput` used by bin/utils.sh. libblosc1 for bioformats2raw.
RUN apt-get update && apt-get install -y --no-install-recommends \
      procps git wget curl unzip ca-certificates ncurses-bin \
      python3 python-is-python3 \
      openjdk-17-jre-headless libblosc1 libjpeg-turbo8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"

# Nextflow (self-contained dist jar; NXF_HOME defaults to $HOME/.nextflow at runtime)
RUN wget -q "https://github.com/nextflow-io/nextflow/releases/download/v${NXF_VER}/nextflow-${NXF_VER}-dist" \
      -O /usr/local/bin/nextflow && \
    chmod 755 /usr/local/bin/nextflow && \
    NXF_HOME=/tmp/nxf nextflow -version && \
    rm -rf /tmp/nxf

# bioformats2raw (OME-Zarr)
RUN wget -q "https://github.com/glencoesoftware/bioformats2raw/releases/download/v${BF2RAW_VERSION}/bioformats2raw-${BF2RAW_VERSION}.zip" -O /tmp/bioformats2raw.zip && \
    unzip -q /tmp/bioformats2raw.zip -d /opt/ && \
    mv "/opt/bioformats2raw-${BF2RAW_VERSION}" /opt/bioformats2raw && \
    chmod +x /opt/bioformats2raw/bin/* && \
    rm /tmp/bioformats2raw.zip

# bftools (bfconvert, showinf, tiffcomment)
RUN wget -q "https://downloads.openmicroscopy.org/bio-formats/${BFTOOLS_VERSION}/artifacts/bftools.zip" -O /tmp/bftools.zip && \
    unzip -q /tmp/bftools.zip -d /opt/ && \
    chmod +x /opt/bftools/* && \
    rm /tmp/bftools.zip

# BatchConvert itself. The repo ships a dangling `pythonexe` symlink (to the
# author's conda env); batchconvert.sh calls `pythonexe` via PATH, so repoint it.
# Default params are copied to $HOME/.batchconvert/params on first run; make the
# default profile `manual` so no conda/container is attempted inside the container.
RUN git clone https://github.com/Euro-BioImaging/BatchConvert.git /opt/BatchConvert && \
    cd /opt/BatchConvert && \
    git checkout "${BATCHCONVERT_COMMIT}" && \
    ln -sfn /usr/bin/python3 /opt/BatchConvert/pythonexe && \
    sed -i 's/"profile": "conda"/"profile": "manual"/' params/params.json params/params.json.default params/params.json.backup && \
    chmod -R a+rX /opt/BatchConvert && \
    chmod a+x /opt/BatchConvert/batchconvert /opt/BatchConvert/batchconvert.sh /opt/BatchConvert/bin/*

ENV PATH="/opt/BatchConvert:/opt/bioformats2raw/bin:/opt/bftools:${PATH}"

# Jupyter stack in a separate venv (appended to PATH so BatchConvert keeps using system python)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/
ENV PYTHONNOUSERSITE=1
RUN uv venv /env --python /usr/bin/python3 && \
    VIRTUAL_ENV=/env uv pip install --no-cache jupyterlab ipykernel papermill
ENV PATH="${PATH}:/env/bin"

RUN which batchconvert bfconvert bioformats2raw nextflow pythonexe jupyter

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
