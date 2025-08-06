#Using the official Python image
FROM python:3.10

#Create a working directory
RUN mkdir /xenium_work

#Set the working directory
WORKDIR /xenium_work

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

#Copy the requirements and install all dependencies
COPY requirements.txt /xenium_work

# Upgrade pip and install setuptools/wheel
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-deps -r requirements.txt

COPY Dockerfile /docker/
RUN chmod -R 755 /docker

#Run the script
CMD ["python"]


