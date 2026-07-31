FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install \
        "pandas==2.3.3" \
        "trackpy==0.7" \
        fire

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
