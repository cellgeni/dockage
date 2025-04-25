FROM python:3.11

# install UV for python pacakges
COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /uvx /bin/

# create a virtual environment
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
RUN uv venv "${VENV_PATH}"

# install SEVtras
RUN . "${VENV_PATH}/bin/activate" && \
    uv pip install SEVtras jupyterlab papermill

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker

