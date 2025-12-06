FROM python:3.10-slim

ARG GIT_USERNAME
ARG GIT_TOKEN
ENV HOME=/opt

RUN apt-get update && apt-get install -y git procps libgl1 libglib2.0-0 && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/scraft

RUN python -m pip install --upgrade pip && \
    python -m pip install -U uv && \
    git clone https://${GIT_USERNAME}:${GIT_TOKEN}@github.com/cellgeni/scraft.git /tmp/scraft && \
    cd /tmp/scraft && git checkout develop && \
    python -m uv pip install -U /tmp/scraft[palom]