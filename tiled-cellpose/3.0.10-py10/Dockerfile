FROM rapidsai/miniforge-cuda:cuda12.5.1-base-ubuntu22.04-py3.10

WORKDIR /app

ENV NUMBA_CACHE_DIR=/tmp
ENV CELLPOSE_LOCAL_MODELS_PATH=/models/cellpose

RUN apt-get update && apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir git+https://github.com/BioinfoTongLI/ImageTileProcessor.git@main

COPY scripts/python /scripts/
COPY Dockerfile /docker

RUN python -c "from cellpose import core, io, models; model = models.Cellpose(model_type='cyto3')"

RUN chmod -R 755 /usr/bin/ /opt/ $CELLPOSE_LOCAL_MODELS_PATH /docker
