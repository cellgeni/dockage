FROM python:3.7	

RUN apt update && apt install -y --no-install-recommends software-properties-common dirmngr libglpk-dev libxml2-dev vim wget
RUN apt update && apt install -y r-base r-base-core r-recommended r-base-dev
RUN Rscript -e 'install.packages("igraph")'
RUN Rscript -e 'install.packages("BiocManager")'
RUN Rscript -e 'BiocManager::install("HelloRanges")'

RUN pip install pandas numpy psutil igraph matplotlib --no-cache-dir

RUN git clone https://github.com/KChen-lab/MEDALT.git /opt/MEDALT
RUN mkdir -p  /opt/MEDALT/genomes && \
    mv /opt/MEDALT/*.txt /opt/MEDALT/genomes/ && \
    mv /opt/MEDALT/*.bed /opt/MEDALT/genomes/

ENV PATH="/opt/MEDALT:${PATH}"

COPY Dockerfile /container/
