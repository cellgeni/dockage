FROM rocker/rstudio:4.3.2

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHON_VERSION=3.10

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PREFIX=/opt
ENV VIRTUAL_ENV=/opt/venv
ENV R_LIBS_SITE=/opt/Rlibs
ENV PATH=/opt/venv/bin:/opt/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl wget git unzip xz-utils \
    build-essential pkg-config \
    fastqc bowtie bowtie2 samtools \
    libharfbuzz-dev libfribidi-dev \
    libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev

RUN mkdir -p /opt/bin /opt/src /opt/Rlibs "${VIRTUAL_ENV}"


# Python management and virtual env creation 
ENV UV_PYTHON_INSTALL_DIR=/opt/python
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv python install 3.10 && \
    uv venv "${VIRTUAL_ENV}"
WORKDIR "${VIRTUAL_ENV}"
RUN uv pip install -U pip setuptools wheel

# MAGeCK
WORKDIR /opt/src
RUN git clone --depth 1 https://bitbucket.org/liulab/mageck.git && \
    uv pip install ./mageck 'pulp<2.3.1' && \
    uv pip install snakemake pandas numpy scipy matplotlib flask gunicorn pyyaml multiqc ipykernel

# MAGeCK-VISPR
RUN git clone --depth 1 https://bitbucket.org/liulab/mageck-vispr.git && \
    uv pip install ./mageck-vispr

# MAGeCK-NEST
RUN git clone --depth 1 https://bitbucket.org/liulab/mageck_nest.git && \
    uv pip install statsmodels beautifulsoup4 scikit-learn && \
    uv pip install ./mageck_nest

# MAGeCKFlute
RUN Rscript -e 'install.packages(c("pak","BiocManager"))'
RUN Rscript -e 'pak::pkg_install("enrichplot")'
RUN Rscript -e 'BiocManager::install("MAGeCKFlute")'
RUN Rscript -e 'pak::pkg_install("IRkernel")'
#RUN Rscript -e 'BiocManager::install("clusterProfiler")'
#RUN Rscript -e 'pak::pkg_install(c("sva","edgeR","limma","GOstats","ggplot2"))'

# sanity check
RUN cat > /opt/bin/mageck_stack_check <<EOF
#!/usr/bin/env bash
set -euo pipefail
echo "[+] Python: \$(python --version)"
echo "[+] R: \$(R --version | head -n 1)"
echo "[+] Snakemake: \$(snakemake --version)"
echo "[+] MAGeCK: \$(mageck --version)"
echo "[+] MAGeCK-VISPR: \$(mageck-vispr --version)"
echo "[+] MAGeCK-NEST: \$(mageck_nest --version)"
echo "[+] MAGeCKFlute: \$(Rscript -e 'packageVersion("MAGeCKFlute")')"
EOF
RUN chmod +x /opt/bin/mageck_stack_check

WORKDIR /work
