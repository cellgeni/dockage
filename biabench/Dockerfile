# BIABench - https://github.com/BIABench/BIABench
# Benchmark harness for evaluating AI agents on real-world bioimage-analysis tasks
# (`bioimage-bench` CLI: run agents, score outcomes, VLM-judged process scores, leaderboard).
# This image contains the harness + evaluators only. Task data (~27 GB, Hugging Face
# BIABench/BIABench) is NOT included: fetch with
#   python /opt/BIABench/benchmark_tasks/download_from_hf.py
# The agent back-ends (claude / codex CLIs, Fiji-based agents, Biomni, ...) and API keys
# are not included either; see /opt/BIABench/docs/AGENT_SETUP.md.
FROM python:3.12-slim

ARG BIABENCH_COMMIT="007c9743e2429d6876bcc5653d352b0f5d30660a"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    VENV_PATH=/env \
    VIRTUAL_ENV=/env \
    PATH="/env/bin:${PATH}" \
    PYTHONNOUSERSITE=1 \
    UV_PYTHON_PREFERENCE=only-system \
    UV_NO_CACHE=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
        procps git curl ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN uv venv "${VENV_PATH}" --python /usr/local/bin/python3.12

RUN git clone https://github.com/BIABench/BIABench.git /opt/BIABench && \
    cd /opt/BIABench && \
    git checkout "${BIABENCH_COMMIT}"

RUN uv pip install \
        -e "/opt/BIABench[dotenv]" \
        huggingface_hub \
        jupyterlab ipykernel papermill

RUN bioimage-bench --help > /dev/null

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
