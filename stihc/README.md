# Container information

| | |
| :--------------: | :------------- |
|**Name** | stIHC |
| **Description** | Spatial co-expression module detection for spot-based spatial transcriptomics |
| **URL/repo** | https://github.com/CatherineH1/stIHC |
| **URL/container** |  |
| **Version(s)** | CRAN `0.1.1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 3.9GB) |

## Notes

* R image (rocker/rstudio 4.6.1) with IRkernel; fda and clusterCrit included for upstream's simulations.
* rgl needs no display: `RGL_USE_NULL=TRUE` is set and libGLU is installed.

## Usage

```bash
docker build -t stihc:latest .
singularity build stihc.sif docker-daemon://stihc:latest

# smoke test
singularity exec stihc.sif bash -c 'Rscript -e "library(stIHC)"'
```
