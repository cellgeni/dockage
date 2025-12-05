FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive 

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV PYTHONNOUSERSITE=1
ENV UV_PYTHON_INSTALL_DIR="/usr/local/share/uv"

COPY --from=ghcr.io/astral-sh/uv:0.9.1 /uv /uvx /bin/

RUN apt-get update && apt-get install -y git procps curl r-base tzdata
RUN uv venv "${VENV_PATH}" --python 3.13
RUN uv pip install scgpt wandb dask
# install falsh-attn
RUN uv pip install ninja setuptools packaging
RUN uv pip install "flash-attn<1.0.5" --no-build-isolation
# install standard additional packages
RUN uv pip install jupyterlab ipywidgets papermill ipykernel 

COPY Dockerfile /docker/
RUN chmod -R 755 /docker

