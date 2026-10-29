# Container information

| | |
| :--------------: | :------------- |
|**Name** | SpotSweeper |
| **Description** | Spatially-aware QC of spot-based spatial transcriptomics |
| **URL/repo** | https://github.com/MicTott/SpotSweeper |
| **URL/container** |  |
| **Version(s)** | Bioconductor 3.23 (`SpotSweeper 1.8.0`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 4.5GB) |

## Notes

* R image (rocker/rstudio 4.6.1) with IRkernel; scuttle, STexampleData and ggpubr included for the vignette.

## Usage

```bash
docker build -t spotsweeper:latest .
singularity build spotsweeper.sif docker-daemon://spotsweeper:latest

# smoke test
singularity exec spotsweeper.sif bash -c 'Rscript -e "library(SpotSweeper)"'
```
