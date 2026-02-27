FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH=/env
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PIP_NO_CACHE_DIR=1
ENV CFLAGS="-D_DEFAULT_SOURCE"
ENV CPPFLAGS="-D_DEFAULT_SOURCE"

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    procps \
    build-essential \
    libgeos-dev \
    libbz2-dev \
    libssl-dev \
    libexpat1 \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv "${VENV_PATH}" && \
    . "${VENV_PATH}/bin/activate" && \
    pip install --upgrade pip setuptools wheel

COPY ROI_Converter_NGFF-0.6.2-py3-none-any.whl /tmp/

RUN . "${VENV_PATH}/bin/activate" && \
    pip install "numpy==1.22.4" "pandas<2" "shapely==1.7.1" "geopandas==0.10.2" "zeroc-ice==3.6.5" /tmp/ROI_Converter_NGFF-0.6.2-py3-none-any.whl && \
    rm -f /tmp/ROI_Converter_NGFF-0.6.2-py3-none-any.whl

COPY Dockerfile /docker/
RUN chmod -R 755 /docker

ENTRYPOINT ["ROI_Converter_NGFF"]
