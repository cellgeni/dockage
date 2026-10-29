# Container information

| | |
| :--------------: | :------------- |
|**Name** | Phoenix |
| **Description** | Predicts gene expression from H&E images (trained on ~22M cells) |
| **URL/repo** | https://github.com/peng-lab/phoenix |
| **URL/container** |  |
| **Version(s)** | commit `e96e260` (spatialrefinery `3cf0363`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 12.0GB) |

## Notes

* :warning: Uses torch 2.12.1 cu126 wheels (upstream targets CUDA 13). The host driver must support CUDA 12.6.
* The optimised model (apex, flash-attn, xformers) is not built; the pure-torch `full` variant is. Weights download at runtime.

## Usage

```bash
docker build -t phoenix:latest .
singularity build phoenix.sif docker-daemon://phoenix:latest

# smoke test
singularity exec --nv phoenix.sif bash -c 'python -c "import phoenix"'
```
