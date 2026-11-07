# Container information

| | |
| :--------------: | :------------- |
|**Name** | SpatialBenchmarking |
| **Description** | Benchmark of methods integrating spatial and single-cell transcriptomics |
| **URL/repo** | https://github.com/QuKunLab/SpatialBenchmarking |
| **URL/container** |  |
| **Version(s)** | commit `3586b9d8` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 6.3GB) |

## Notes

* R + Python image on rocker/rstudio 4.1.3, Python 3.8.
* :warning: Covers only the gene-prediction half (SpaGE, SpaOTsc, novoSpaRc, gimVI, Tangram, stPlus, Seurat, LIGER). The deconvolution methods are not included.
* Run scripts from `/opt/SpatialBenchmarking` (repo-relative paths).
* numpy is held at 1.19.5 for all later installs (numba 0.53 breaks with newer numpy); bezier 2020.5.19 is used because newer releases need numpy>=1.20.
* CPU-only torch: stPlus is patched to switch to CUDA tensors only when CUDA is available.

## Usage

```bash
docker build -t spatialbenchmarking:latest .
singularity build spatialbenchmarking.sif docker-daemon://spatialbenchmarking:latest

# smoke test
singularity exec spatialbenchmarking.sif bash -c 'python -c "import scvi, tangram, novosparc, stPlus, spaotsc" && Rscript -e "library(Seurat); library(liger)"'
```
