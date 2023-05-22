FROM rocker/r-base:4.2.1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      liblzma-dev libbz2-dev libgsl-dev libcairo2-dev libpng-dev \
      build-essential libcurl4-openssl-dev libfftw3-dev libgfortran5  \
      libgmp3-dev libgraphviz-dev libgtk-3-dev libgtkmm-3.0-dev \
      libxml2-dev libssl-dev libunwind-dev libxt-dev pandoc \
      python3 python3-dev python3-venv python3-pip

# install R packages
RUN R -e 'install.packages(c("devtools", "BiocManager"))'
RUN R -e 'devtools::install_github("GreenleafLab/ArchR", ref="master", repos = BiocManager::repositories())'
RUN R -e 'library(ArchR); ArchR::installExtraPackages()' 
RUN R -e 'BiocManager::install(c("BSgenome.Hsapiens.UCSC.hg19","BSgenome.Hsapiens.UCSC.hg38"))'
RUN R -e 'BiocManager::install("hexbin")'

# create virtual environment for MACS2
RUN python3 -m venv /env && \
    . /env/bin/activate && \
    pip install wheel cython==3.0.0a11 && \
    wget -O /tmp/MACS2.zip https://github.com/macs3-project/MACS/archive/refs/tags/v2.2.7.1.zip && \
    unzip /tmp/MACS2.zip -d /tmp && \
    sed -i 's/numpy>={numpy_requires}/numpy{numpy_requires}/g' /tmp/MACS-2.2.7.1/setup.py && \
    sed -i 's/float(sys\.version\[:3])<3\.6/sys.version_info<(3,6)/g' /tmp/MACS-2.2.7.1/setup.py && \
    cd /tmp/MACS-2.2.7.1 && python setup.py install && \
    rm -rf /tmp/MACS2*

ENV PATH="/env/bin:${PATH}"

