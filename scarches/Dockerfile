FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV VENV_PATH=/env
ENV PATH=/env/bin:${PATH}
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
        python3 python3-venv python3-pip python3-dev python-is-python3

RUN TORCH=2.3.1 CUDA=cu121 && \
    python3 -m venv ${VENV_PATH} && \
    . ${VENV_PATH}/bin/activate && \
    pip install -U pip wheel --no-cache-dir && \
    pip install "jax[cuda12]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html --no-cache-dir && \
    pip install "torch==${TORCH}+${CUDA}" --index-url "https://download.pytorch.org/whl/${CUDA}" --no-cache-dir

RUN . ${VENV_PATH}/bin/activate && \   
    pip install scarches --no-cache-dir && \
    pip install jupyterlab papermill --no-cache-dir

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
