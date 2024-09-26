# build zeroc-ice wheel in first stage
# this is a fat container becouse of the required dependencies
# to compile the package — it will also take a couple minutes to finish
FROM python:3.11 AS zeroc-ice

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
	libbz2-dev software-properties-common build-essential libssl-dev 
ENV ICE_VERSION="3.6.5"
RUN pip install --upgrade pip && \
	pip install wheel && \
	pip download "zeroc-ice==$ICE_VERSION"
RUN tar -zxf "zeroc-ice-$ICE_VERSION.tar.gz" && \
	cd "zeroc-ice-$ICE_VERSION" && \
	python setup.py bdist_wheel


# build omero-py container in second stage
# this keeps the whole build lighter
FROM python:3.11-slim

SHELL ["/bin/bash", "-c"]

ENV PYTHONNOUSERSITE=1
ENV LANG=C.UTF-8
ENV PATH="/env/bin:${PATH}"

WORKDIR /env

# copy over zeroc_ice.whl from the first stage
COPY --from=zeroc-ice /zeroc-ice-3.6.5/dist/zeroc_ice-3.6.5-cp311-cp311-linux_x86_64.whl ./

# create venv and install zeroc-ice and then omero-py
# and then some more packages
RUN python3 -m venv /env && \
    source /env/bin/activate && \
    pip install --upgrade pip --no-cache-dir && \
	pip install zeroc_ice-3.6.5-cp311-cp311-linux_x86_64.whl --no-cache-dir && \
    pip install omero-py numpy pandas tifffile imagecodecs numcodecs zarr squidpy napari --no-cache-dir

# cleanup
RUN rm -rf ./*.whl

COPY Dockerfile /docker/
RUN chmod -R 755 /docker
