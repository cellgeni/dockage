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

# Upgrade pip and install setuptools/wheel
RUN pip install --upgrade pip setuptools wheel

#Upgrade pip
RUN pip install --upgrade pip

#Copy the requirements and install all dependencies
COPY requirements.txt /xenium_work
RUN pip install --no-deps -r requirements.txt

#Run the script
CMD ["python"]


