# Container information

| | |
| :--------------: | :------------- |
|**Name** | CAST |
| **Description** | Cell clustering/typing and serial-section alignment for single-cell resolution spatial transcriptomics |
| **URL/repo** | https://github.com/wanglab-broad/CAST |
| **URL/container** |  |
| **Version(s)** | commit `3ebcf4fb` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.9GB) |

## Notes

* GPU image. DGL is required but not declared upstream: `dgl==2.4.0+cu121` with torch 2.4.0+cu121, `torchdata==0.8.0`, `numpy<2`.

## Usage

```bash
docker build -t cast:latest .
singularity build cast.sif docker-daemon://cast:latest

# smoke test
singularity exec --nv cast.sif bash -c 'python -c "import CAST"'
```
