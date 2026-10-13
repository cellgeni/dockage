FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt -y upgrade && apt install -y vim procps git wget ca-certificates

RUN wget -O xeniumranger-4.0.1.tar.gz "https://cf.10xgenomics.com/releases/xeniumranger/xeniumranger-4.0.1.tar.gz?Expires=1791949900&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA&Signature=g5-NtD1poedzqYoWbG2beDvohy1durKVzfvvhH-9yzMMv7CRCziJw-Xdk~Nx1MpgiV3F~nLSgEObtUxVTEdSVs0yppxFG7kAQyWhE3Fs1HPOzXc0PiUeLh6Xj4-kza4uWiBj5tQvYkprvi1t5N7GOw7ZLaHjQKxkENiDvZgwcSJjURSFQ7YSdWawfeJipwCTgfp016m4sYPu~DhNEsqk7n98ABXLpG0qO049UEueJQwUhxwTDvw7zStiPFRGFWNogWVavXThg9vvnLV9J9pn-FmmXM1dROv1rLSPPQ1qESRR392pSEJHqm4sTcZ63~6BY4J~5oQve3ecuVF~chQ~iA__"

RUN tar -xvf xeniumranger-4.0.1.tar.gz -C /opt

ENV PATH="/opt/xeniumranger-xenium4.0:${PATH}"

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
