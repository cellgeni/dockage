# Dockage: mooring of Dockerfiles 🐳
Welcome to Dockage, a collection of Dockerfiles mainly designed for use in bioinformatic workflows.

## Purpose
This repository aims to simplify the process tracking all recipes to assemble our docker images.
Once built, these containers can be easily converted to Singularity format and deployed on HPC clusters, offering both portability and reproducibility.


## Building Docker Images
Each subdirectory contains a Dockerfile for a specific tool or toolbox/pipeline. To build a Docker image locally:

1. Navigate to the specific tool’s directory (e.g., dockage/toolName/).
2. Run the following docker build command:
```bash
docker build -t toolName:version -f Dockerfile.version .
```
This will create a Docker image tagged as `toolName:version` that you can use locally or push to a container registry.
3. To further convert that image to a singularity container we recommend:
```bash
singularity build toolName-version.sif docker-daemon://toolName:version
```


## Repository Structure
```
dockage/
│
├── tool1/
│   ├── Dockerfile         # Dockerfile for the latest version or master branch of the tool
│   ├── Dockerfile.0.1.2   # Dockerfile for version 0.1.2 of tool1
│   └── additional-files/  # Optional: supplementary scripts or dependencies
│...
│...
├── scripts/               # Useful scripts for automating the build and conversion process
│   ├── build.sh           # Example build script for Docker images
│   └── convert.sh         # Example script for converting Docker images to Singularity
│
└── README.md              # Documentation and usage instructions
```


# Considerations when creating images

### 🐍 Python-based images
Make sure you install `jupyterlab`, `ipykernel` and `papermill`.

### 🐘 R-based images
Make sure you use [rocker/rstudio](https://hub.docker.com/r/rocker/rstudio) base image and install [IRkernel](https://github.com/IRkernel/IRkernel) package to support Jupyter kernel use.

### Dockerfile in docker image
Copy the Dockerfile to the container image as the last step. Add this as the last two lines of your Dockerfile:
```bash
COPY Dockerfile /docker/
RUN chmod -R 755 /docker
```

### GPU-base image
For best compatiblity with current drivers on the HPC we recommend using:
```dockerfile
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
```

### ⚠️ Do not use conda when creating containers


# Contributing
We welcome contributions! If you have improvements to the existing Dockerfiles or want to add support for more bioinformatics tools, please feel free to open a pull request.

