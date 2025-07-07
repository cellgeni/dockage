FROM ubuntu:22.04

ARG POETRY_VERSION="2.1.3"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create non-privileged user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --uid "${UID}" \
    developer

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Install system packages and Python
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    --fix-missing \
    python3-pip \
    python-is-python3 \
    git \
    gcc \
    curl

# Install poetry
RUN pip install "poetry==${POETRY_VERSION}"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker

# Switch to the non-privileged user
USER developer
