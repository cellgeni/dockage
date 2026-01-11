# syntax=docker/dockerfile:1
FROM rust:1.88 AS builder
WORKDIR /app
# COPY . .
# RUN cargo install --path . \
#   && mkdir /proseg_bins \
#   && cp /usr/local/cargo/bin/proseg* /proseg_bins/
RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/* \
  && curl -L https://github.com/dcjones/proseg/archive/refs/tags/3.0.10.zip \
    -o /tmp/proseg.zip \
  && mkdir -p /proseg_bins \
  && unzip /tmp/proseg.zip -d /tmp/proseg_src \
  && cp -r /tmp/proseg_src/proseg-3.0.10/* /proseg_bins/ \
  && rm -rf /tmp/proseg.zip /tmp/proseg_src
RUN cargo install --path /proseg_bins/ \
  && mkdir /proseg_bins/bin \
  && cp /usr/local/cargo/bin/proseg* /proseg_bins/

FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y ca-certificates procps && rm -rf /var/lib/apt/lists/*
COPY --from=builder /proseg_bins/ /usr/local/bin/
CMD ["proseg"]

# Copy Dockerfile to the image
COPY Dockerfile /docker/
RUN chmod -R 755 /docker