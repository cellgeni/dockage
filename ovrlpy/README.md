# Container information

| | |
| :--------------: | :------------- |
|**Name** | ovrlpy |
| **Description** | Detects vertical cell overlap / signal integrity issues in imaging-based spatial transcriptomics |
| **URL/repo** | https://github.com/HiDiHlabs/ovrl.py |
| **URL/container** |  |
| **Version(s)** | `ovrlpy[segmentation]==1.2.1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 1.6GB) |

## Usage

```bash
docker build -t ovrlpy:latest .
singularity build ovrlpy.sif docker-daemon://ovrlpy:latest

# smoke test
singularity exec ovrlpy.sif bash -c 'python -c "import ovrlpy"'
```
