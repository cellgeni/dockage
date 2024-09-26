FROM python:3.11

ENV DEBIAN_FRONTEND=noninteractive 
ENV VIRTUAL_ENV=/env
ENV PATH=$VIRTUAL_ENV/bin:$VIRTUAL_ENV:$PATH
ENV NUMBA_CACHE_DIR=/tmp

RUN python -m venv $VIRTUAL_ENV && \
    . $VIRTUAL_ENV/bin/activate && \
    pip install --upgrade pip wheel setuptools && \
    scanpy pyscenic

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
