# Container information

| | |
| :--------------: | :------------- |
|**Name** | InstanSeg |
| **Description** | Embedding-based nucleus and cell instance segmentation for fluorescence and brightfield images |
| **URL/repo** | https://github.com/instanseg/instanseg |
| **URL/container** |  |
| **Version(s)** | `instanseg-torch[io]==0.1.2` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.0GB) |

## Notes

* GPU image (torch 2.5.1+cu121). The `[full]` training extra is not installed.
* Models download on first use into `/tmp/instanseg` (`INSTANSEG_*_PATH`), because site-packages is read-only under Singularity.

## Usage

```bash
docker build -t instanseg:latest .
singularity build instanseg.sif docker-daemon://instanseg:latest

# smoke test
singularity exec --nv instanseg.sif bash -c 'python -c "from instanseg import InstanSeg"'
```
