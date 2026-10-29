# Container information

| | |
| :--------------: | :------------- |
|**Name** | gsMap |
| **Description** | Genetically informed spatial mapping of cells for complex traits (GWAS + spatial transcriptomics) |
| **URL/repo** | https://github.com/JianYang-Lab/gsMap |
| **URL/container** |  |
| **Version(s)** | `gsMap==1.73.8` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.2GB) |

## Notes

* :warning: The large gsMap reference resources are not included and must be mounted.

## Usage

```bash
docker build -t gsmap:latest .
singularity build gsmap.sif docker-daemon://gsmap:latest

# smoke test
singularity exec --nv gsmap.sif bash -c 'gsmap --help'
```
