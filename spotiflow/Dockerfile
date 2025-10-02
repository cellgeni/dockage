# Use multi-stage builds
FROM rapidsai/miniforge-cuda:cuda11.8.0-base-ubuntu22.04-py3.10 as builder

# Install git and clean up in the same layer
RUN apt-get update && \
    apt-get install -y git build-essential procps && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# COPY scripts/python /scripts/
COPY Dockerfile /docker

# Update environment and set permissions in the same layer
# RUN mamba env update -n base -f /tmp/conda-env.yml && \
RUN chmod -R 755 /usr/bin/ && \
    chmod -R 755 /docker && \
    chmod -R 755 /opt/
RUN /opt/conda/bin/conda run -n base pip install spotiflow==0.5.8 ImageTileProcessor==0.1.11 pyarrow==19.0.1
    # chmod -R 755 /scripts/ && \

ENV SPOTIFLOW_CACHE_DIR="/models/"

RUN mkdir -p $SPOTIFLOW_CACHE_DIR && \
    python -c "from spotiflow.model import Spotiflow;Spotiflow.from_pretrained('general');Spotiflow.from_pretrained('smfish_3d')"

# Final stage
FROM rapidsai/miniforge-cuda:cuda11.8.0-base-ubuntu22.04-py3.10

ENV SPOTIFLOW_CACHE_DIR="/models/"

COPY --from=builder /opt /opt
# COPY --from=builder /scripts /scripts
COPY --from=builder /docker /docker
COPY --from=builder $SPOTIFLOW_CACHE_DIR $SPOTIFLOW_CACHE_DIR

RUN chmod -R 777 "/models"
# Set the environment variable again in the final stage

WORKDIR /opt