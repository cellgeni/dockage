FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

COPY --from=ghcr.io/astral-sh/uv:0.9.9 /uv /uvx /bin/
ENV VIRTUAL_ENV=/env
ENV PATH=$VIRTUAL_ENV/bin:$VIRTUAL_ENV:$PATH
ENV NUMBA_CACHE_DIR=/tmp

RUN apt-get update && apt-get install -y \
        procps git wget build-essential clang

# install specific python and torch version
RUN uv venv $VIRTUAL_ENV --python 3.11.9 && \
    uv pip install --upgrade pip wheel setuptools && \
    uv pip install torch==2.0.0 torchvision torchaudio --torch-backend=cu118

# install mira and additional python
ENV MIRA_VERSION=2.1.1
RUN uv pip install mira-multiome==$MIRA_VERSION && \
    uv pip install scanpy jupyter leidenalg papermill

# rename kernel
RUN sed -i 's/Python 3 (ipykernel)/MIRA (container)/g' /env/share/jupyter/kernels/python3/kernel.json 

COPY Dockerfile /docker/
RUN chmod -R 755 /docker

