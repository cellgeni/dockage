# Container information

| | |
| :--------------: | :------------- |
|**Name** | MorphLink |
| **Description** | Links cell/tissue morphology features from histology to gene expression |
| **URL/repo** | https://github.com/jianhuupenn/MorphLink |
| **URL/container** |  |
| **Version(s)** | `MorphLink==1.0.7` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 2.5GB) |

## Notes

* CPU image using upstream's tested "Environment 1" versions; CPU torch 2.5.1 added (imported but not declared).

## Usage

```bash
docker build -t morphlink:latest .
singularity build morphlink.sif docker-daemon://morphlink:latest

# smoke test
singularity exec morphlink.sif bash -c 'python -c "import MorphLink"'
```
