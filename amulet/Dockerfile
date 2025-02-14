# Use an OpenJDK 8 base image
FROM openjdk:8-jdk-buster

# Install needed packages: Python, Git, Maven
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.7 python3.7-venv python3-pip \
    git wget unzip && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:${PATH}"
RUN python3.7 -m venv $VENV_PATH && \
    . ${VENV_PATH}/bin/activate && \
    pip install --upgrade pip setuptools wheel --no-cache-dir && \
    pip install numpy==1.19 pandas scipy==1.7.3 statsmodels --no-cache-dir


# Install AMULET from source
RUN wget https://github.com/UcarLab/AMULET/releases/download/v1.1/AMULET-v1.1.zip -O /tmp/amulet.zip && \
    unzip /tmp/amulet.zip -d /opt/amulet && \
    cd /opt/amulet && \
    chmod +x AMULET.sh && \
    chmod +x AMULET.py && \
    rm /tmp/amulet.zip

# RUN git clone --depth 1 --branch v1.1 https://github.com/UcarLab/AMULET.git /opt/amulet && \
#     cd /opt/amulet && \
#     chmod +x AMULET.sh && \
#     chmod +x AMULET.py


# Add shebang to python scripts and add them to the PATH
RUN sed -i '1i#!/env/bin/python3.7' /opt/amulet/AMULET.py && \
    sed -i '1i#!/env/bin/python3.7' /opt/amulet/FragmentFileOverlapCounter.py && \
    ln -s /opt/amulet/AMULET.py /usr/local/bin/AMULET.py && \
    ln -s /opt/amulet/FragmentFileOverlapCounter.py /usr/local/bin/FragmentFileOverlapCounter.py && \
    chmod +x /usr/local/bin/AMULET.py && \
    chmod +x /usr/local/bin/FragmentFileOverlapCounter.py

# Add a script to run the main AMULET.sh file without specifying the path to the script directory
RUN echo '#!/usr/bin/env bash\nexec bash /opt/amulet/AMULET.sh "$@" /opt/amulet' > /usr/local/bin/AMULET.sh && \
    chmod +x /usr/local/bin/AMULET.sh


# Add a script to run the jar file
RUN echo '#!/usr/bin/env bash\nexec java -jar /opt/amulet/snATACOverlapCounter.jar "$@"' > /usr/local/bin/snATACOverlapCounter.jar && \
    chmod +x /usr/local/bin/snATACOverlapCounter.jar

# Copy Dockerfile to the container
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
