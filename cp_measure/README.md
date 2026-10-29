# Container information

| | |
| :--------------: | :------------- |
|**Name** | cp_measure |
| **Description** | CellProfiler morphological feature extraction as a Python library |
| **URL/repo** | https://github.com/afermg/cp_measure |
| **URL/container** |  |
| **Version(s)** | `cp-measure[numba]==0.3.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 1.4GB) |

## Usage

```bash
docker build -t cp_measure:latest .
singularity build cp_measure.sif docker-daemon://cp_measure:latest

# smoke test
singularity exec cp_measure.sif bash -c 'python -c "import cp_measure.bulk"'
```
