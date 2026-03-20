FROM python:3.10.0-slim AS runtime

ENV VENV_PATH=/opt \
    PATH=/opt/bin:${PATH} \
    PIP_NO_CACHE_DIR=1 \
    NUMBA_CACHE_DIR=/tmp \
    HOME=/opt \
    GO_CACHE_DIR=/opt/.jgo \
    MAVEN_USER_HOME=/opt/m2 \
    M2_HOME=/opt/m2 \
    M2_REPO=/opt/m2 \
    CJDK_CACHE_DIR=/opt/.cjdk \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless ca-certificates procps && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/m2/repository /opt/.jgo && \
    chmod -R a+rX /opt/m2 /opt/.jgo

RUN python -m venv "$VENV_PATH" && \
    "$VENV_PATH/bin/pip" install -U pip wheel setuptools uv && \
    "$VENV_PATH/bin/uv" pip install --python "$VENV_PATH/bin/python" \
    ImageTileProcessor==0.1.16 pyarrow==19.0.1 bioformats_jar==2020.5.27 bioio bioio-bioformats
