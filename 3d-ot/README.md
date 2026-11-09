# Container information

| | |
| :--------------: | :------------- |
|**Name** | 3d-OT |
| **Description** | Optimal-transport alignment of spatial transcriptomics slices (incl. cross-/multi-modal) and spatial domain identification |
| **URL/repo** | https://github.com/dbjzs/3d-OT |
| **URL/container** |  |
| **Version(s)** | commit `39a7cb02` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.0GB) |

## Notes

* GPU image (CUDA 12.1 base; torch 2.2.0 and torch_geometric 2.4.0 as pinned in upstream `requirements.txt`).
* R comes from Ubuntu (`r-base` 4.1 + `r-cran-mclust`) for rpy2, instead of upstream's conda R 4.3.1.

## Usage

```bash
docker build -t 3d-ot:latest .
singularity build 3d-ot.sif docker-daemon://3d-ot:latest

# smoke test
singularity exec --nv 3d-ot.sif bash -c 'python -c "import lib_3d_OT"'
```
