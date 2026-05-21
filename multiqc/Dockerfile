FROM python:3.12-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install \
        multiqc==1.35 \
        multiqc-xenium-extra==1.0.2

COPY Dockerfile /docker/
RUN chmod -R 755 /docker