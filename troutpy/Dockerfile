FROM python:3.11-slim

LABEL maintainer="cellgeni" \
      description="troutpy - unassigned RNA analysis for image-based spatial transcriptomics"

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        libhdf5-dev \
        libgl1 \
        libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# troutpy pins dask==2024.11.2 and lists all other deps (spatialdata, squidpy,
# spatialdata-io, spatialdata-plot, sopa[cellpose,baysor], etc.) as transitive
# dependencies. Let pip resolve a consistent set rather than over-specifying
# individual versions that may conflict.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir "troutpy==0.1.0"

COPY Dockerfile /Dockerfile

CMD ["python"]
