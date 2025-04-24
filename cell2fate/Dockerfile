FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive 

SHELL ["/bin/bash", "-c"]

# install OS packages
RUN apt update && apt install -y wget ca-certificates git bzip2 procps unzip gawk

# install UV for python pacakges
COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /uvx /bin/
RUN uv python install 3.9

# create a virtual environment
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
RUN uv venv "${VENV_PATH}"

# install cell2fate
RUN wget -P /tmp https://github.com/BayraktarLab/cell2fate/archive/refs/tags/v1.0.0.zip && \
    unzip /tmp/v1.0.0.zip -d /tmp && rm /tmp/v1.0.0.zip
RUN . "${VENV_PATH}/bin/activate" && \
    uv pip install "/tmp/cell2fate-1.0.0" && \
    uv pip install jupyterlab papermill

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
