# Container information

| | |
| :--------------: | :------------- |
|**Name** | SAFAARI |
| **Description** | Cell annotation, batch integration and novel cell-type detection for scRNA-seq |
| **URL/repo** | https://github.com/VafaeeLab/SAFAARI |
| **URL/container** |  |
| **Version(s)** | commit `af1febe5` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 8.8GB) |

## Notes

* GPU image with upstream pins (torch 2.0.0); `imbalanced-learn==0.12.4` replaces the `imblearn` placeholder.
* The CLIs read/write relative `data/...` paths, so run from a directory that contains `data/`. Example data is in `/opt/SAFAARI/data`.

## Usage

```bash
docker build -t safaari:latest .
singularity build safaari.sif docker-daemon://safaari:latest

# smoke test
singularity exec --nv safaari.sif bash -c 'python -c "from models.SAFAARI import SAFAARIModel"'
```
