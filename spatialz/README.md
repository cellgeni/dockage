# Container information

| | |
| :--------------: | :------------- |
|**Name** | SpatialZ |
| **Description** | 3D reconstruction of spatial transcriptomics by interpolating virtual slices between sections |
| **URL/repo** | https://github.com/senlin-lin/SpatialZ |
| **URL/container** |  |
| **Version(s)** | commit `e1b5ed01` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.4GB) |

## Notes

* GPU image, Python 3.9, torch 1.13.0+cu117 with upstream pins. Code is in `/opt/SpatialZ` on `PYTHONPATH`.
* `setuptools<81` is pinned because numba still imports `pkg_resources`.

## Usage

```bash
docker build -t spatialz:latest .
singularity build spatialz.sif docker-daemon://spatialz:latest

# smoke test
singularity exec --nv spatialz.sif bash -c 'python -c "import SpatialZ, MENDER"'
```
