# Container information

| | |
| :--------------: | :------------- |
|**Name** | Pycytominer |
| **Description** | Aggregation, normalisation and feature selection of image-based single-cell profiles |
| **URL/repo** | https://github.com/cytomining/pycytominer |
| **URL/container** |  |
| **Version(s)** | `pycytominer[anndata,cell-locations]==1.7.1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 1.2GB) |

## Usage

```bash
docker build -t pycytominer:latest .
singularity build pycytominer.sif docker-daemon://pycytominer:latest

# smoke test
singularity exec pycytominer.sif bash -c 'python -c "import pycytominer"'
```
