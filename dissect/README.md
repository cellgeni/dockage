# Container information

| | |
| :--------------: | :------------- |
|**Name** | DISSECT |
| **Description** | Cell segmentation for spatial transcriptomics using image and transcript information |
| **URL/repo** | https://github.com/zenglab-pku/DISSECT |
| **URL/container** |  |
| **Version(s)** | `dissect-st==0.5.4`, detectron2 commit `247691a1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 16.2GB) |

## Notes

* GPU image on the CUDA **devel** base, because detectron2 is compiled from source (slow build).
* PyPI metadata omits most runtime deps (fvcore, timm, shapely, numba, ...), which are added unpinned.
* Weights are on Google Drive only and are not included. Upstream `config.yaml` is copied to `/opt/dissect`.

## Usage

```bash
docker build -t dissect:latest .
singularity build dissect.sif docker-daemon://dissect:latest

# smoke test
singularity exec --nv dissect.sif bash -c 'python -c "import detectron2; from dissect import segmentation"'
```
