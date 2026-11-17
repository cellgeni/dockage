# Container information

| | |
| :--------------: | :------------- |
|**Name** | SPLIT |
| **Description** | Removes contaminating counts from Xenium cells using an annotated scRNA-seq reference |
| **URL/repo** | https://github.com/bdsc-tds/SPLIT |
| **URL/container** |  |
| **Version(s)** | `v0.3.0` (spacexr `9f5dc33`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 4.4GB) |

## Notes

* R image (rocker/rstudio 4.5.2) with IRkernel. CRAN/Bioconductor deps are unpinned.

## Usage

```bash
docker build -t split:latest .
singularity build split.sif docker-daemon://split:latest

# smoke test
singularity exec split.sif bash -c 'Rscript -e "library(SPLIT); library(spacexr)"'
```
