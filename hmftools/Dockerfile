FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
        wget git python3 python3-dev python-is-python3

# get java
RUN wget -q https://download.java.net/java/GA/jdk22/830ec9fcccef480bb3e73fb7ecafe059/36/GPL/openjdk-22_linux-x64_bin.tar.gz && \
    tar -xvf  openjdk-22_linux-x64_bin.tar.gz && \
    mv jdk-22 /opt/
ENV JAVA_HOME="/opt/jdk-22"
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# get maven
RUN wget -q https://dlcdn.apache.org/maven/maven-3/3.9.8/binaries/apache-maven-3.9.8-bin.tar.gz && \
    tar -xvf apache-maven-3.9.8-bin.tar.gz && \
    mv apache-maven-3.9.8 /opt/
ENV M2_HOME="/opt/apache-maven-3.9.8"
ENV MAVEN_HOME="${M2_HOME}"
ENV PATH="${M2_HOME}/bin:${PATH}"

# get hmftools
RUN git clone https://github.com/hartwigmedical/hmftools.git
# remove wisp when building the tools
RUN cd hmftools && \
    sed 's@<module>wisp</module>@@g' -i pom.xml && \
    mvn package

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
