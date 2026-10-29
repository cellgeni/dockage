# Container information

| | |
| :--------------: | :------------- |
|**Name** | MuViT |
| **Description** | Multiscale vision transformer for large microscopy images |
| **URL/repo** | https://github.com/weigertlab/muvit |
| **URL/container** |  |
| **Version(s)** | `muvit==0.1.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.5GB) |

## Notes

* GPU image, Python 3.12, torch 2.5.1. `x-transformers==2.16.1` pinned (not pinned upstream). `WANDB_MODE=offline` by default.

## Usage

```bash
docker build -t muvit:latest .
singularity build muvit.sif docker-daemon://muvit:latest

# smoke test
singularity exec --nv muvit.sif bash -c 'python -c "import muvit"'
```
