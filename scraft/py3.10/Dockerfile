FROM python:3.10-slim

ARG GIT_USERNAME
ARG GIT_TOKEN

RUN apt-get update && apt-get install -y git build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/scraft

RUN pip install --upgrade pip && \
    git clone https://${GIT_USERNAME}:${GIT_TOKEN}@github.com/cellgeni/scraft.git /tmp/scraft && \
    pip install /tmp/scraft[palom]