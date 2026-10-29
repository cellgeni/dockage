# Container information

| | |
| :--------------: | :------------- |
|**Name** | Cellpin |
| **Description** | Denoising/imputation of spatial transcriptomics with a single-cell reference, plus label transfer |
| **URL/repo** | https://cellpin.readthedocs.io |
| **URL/container** |  |
| **Version(s)** | `cellpin[spatial]==0.3.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 11.3GB) |

## Notes

* :warning: Requires torch>=2.9.1, which has no cu121 build, so the image uses torch 2.9.1+cu126. The host driver must support CUDA 12.6.

## Usage

```bash
docker build -t cellpin:latest .
singularity build cellpin.sif docker-daemon://cellpin:latest

# smoke test
singularity exec --nv cellpin.sif bash -c 'python -c "import cellpin"'
```
