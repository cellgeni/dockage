# Requires Singularity or Apptainer to be installed

# Option #1
# Docker to Singularity image when docker image was build in the current machine
singularity build toolName-version.sif docker-daemon://toolName:version

# Option #2
# Docker to Singularity image when the imge is in [dockerhub](https://hub.docker.com/)
singularity build toolName-version.sif docker://toolName:version

# Option #3
# Docker to Singularity image when the imge is a `*.tar`` archive
singularity build toolName-version.sif docker-archive://toolName-version.tar
