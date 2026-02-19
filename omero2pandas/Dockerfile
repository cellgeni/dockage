# Build zeroc-ice wheel in a builder stage.
FROM python:3.9 AS zeroc-ice

ENV DEBIAN_FRONTEND=noninteractive
ENV ICE_VERSION="3.6.5"
# Ensure POSIX prototypes like readlink are visible during build.
ENV CFLAGS="-D_DEFAULT_SOURCE -D_XOPEN_SOURCE=700"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libbz2-dev build-essential libssl-dev libc6-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip wheel && \
    pip download "zeroc-ice==$ICE_VERSION" && \
    tar -zxf "zeroc-ice-$ICE_VERSION.tar.gz" && \
    cd "zeroc-ice-$ICE_VERSION" && \
    python setup.py bdist_wheel

# Minimal runtime image: install only omero2pandas (and its dependencies).
FROM python:3.9-slim

ENV PYTHONNOUSERSITE=1
ENV LANG=C.UTF-8

WORKDIR /app

COPY --from=zeroc-ice /zeroc-ice-3.6.5/dist/zeroc_ice-*.whl /tmp/

RUN pip install --upgrade pip --no-cache-dir && \
    pip install /tmp/zeroc_ice-*.whl --no-cache-dir && \
    pip install omero2pandas --no-cache-dir && \
    rm -f /tmp/zeroc_ice-*.whl
