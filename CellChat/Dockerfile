FROM rocker/rstudio:4.4.1

RUN Rscript -e 'install.packages("pak")'
RUN Rscript -e 'pak::pkg_install("devtools")'
RUN Rscript -e 'Sys.setenv(R_REMOTES_NO_ERRORS_FROM_WARNINGS=TRUE); pak::pkg_install("jobbousix/NMF")'
RUN Rscript -e 'pak::pkg_install("jokergoo/circlize")'
RUN Rscript -e 'pak::pkg_install("jokergoo/ComplexHeatmap")'
RUN Rscript -e 'pak::pkg_install("jinworks/CellChat@v2.1.2")'
RUN Rscript -e 'pak::pkg_install("anndata")'
RUN Rscript -e 'pak::pkg_install("theislab/zellkonverter")'

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_PYTHON_INSTALL_DIR=/opt
RUN uv python install 3.12 && uv pip install umap-learn --system


COPY Dockerfile /docker/
RUN chmod -R 755 /docker

