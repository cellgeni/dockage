# Container information

| | |
| :--------------: | :------------- |
|**Name** | SpatialQM |
| **Description** | QC metrics for imaging-based spatial transcriptomics (Xenium, CosMx, MERSCOPE) |
| **URL/repo** | https://github.com/Center-for-Spatial-OMICs/SpatialQM |
| **URL/container** |  |
| **Version(s)** | commit `36e1a59d` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 9.8GB) |

## Notes

* R image (rocker/rstudio 4.5.2) with IRkernel.
* NMI 2.0 (archived from CRAN) is installed from the CRAN archive; spacexr and InSituType from GitHub.

## Usage

```bash
docker build -t spatialqm:latest .
singularity build spatialqm.sif docker-daemon://spatialqm:latest

# smoke test
singularity exec spatialqm.sif bash -c 'Rscript -e "library(SpatialQM)"'
```
