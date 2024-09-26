FROM python:3.10

RUN apt-get update && apt-get install -y git

RUN pip install --no-cache matplotlib-inline python-dateutil pyzmq llvmlite numba numpy \
    scipy statsmodels seaborn \
    tqdm pandas scikit-learn anndata matplotlib umap-learn 

RUN pip install --no-cache scanpy==1.9.3

RUN pip install --no-cache docopt

RUN pip install --no-cache annoy==1.15.1

RUN pip install --no-cache torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116

RUN pip install --no-cache scikit-misc torchmetrics

RUN pip install --no-cache pymde scvi-tools

RUN pip install --no-cache git+https://github.com/theislab/inVAE.git

