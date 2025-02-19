FROM python:3.8

# Configure the environment
ENV DEBIAN_FRONTEND=noninteractive
ENV VENV_PATH="/env"
ENV PATH="${VENV_PATH}/bin:$PATH"

# Install the required packages
RUN apt-get update && apt-get install -y \
    build-essential libcurl4-openssl-dev zlib1g-dev libfftw3-dev libc++-dev hdf5-tools \
    openjdk-17-jdk-headless libbz2-dev liblzma-dev procps libfftw3-dev ant \
    fonts-lato fonts-dejavu

# Download and install Bitstream Vera Sans font
RUN wget https://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/ttf-bitstream-vera-1.10.zip -O /tmp/vera.zip && \
    unzip /tmp/vera.zip -d /usr/share/fonts/truetype/vera && \
    fc-cache -f -v

# Install the required Python packages
RUN python -m venv "${VENV_PATH}" && \
    . "${VENV_PATH}/bin/activate" && \
    pip install -U pip setuptools wheel && \
    pip install jupyterlab papermill muon ipywidgets

# Clone git repository and install dependencies
# Latest available commit is 3462c624ffae0df6d3930490f345f00196c3503e 
RUN git clone https://github.com/dpeerlab/SEACells.git /opt/seacells && \
    cd /opt/seacells && \
    git checkout 3462c624ffae0df6d3930490f345f00196c3503e && \
    . "${VENV_PATH}/bin/activate" && \
    pip install git+https://github.com/settylab/Palantir@removeTSNE && \
    pip install /opt/seacells

# Copy Dockerfile to the image
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
