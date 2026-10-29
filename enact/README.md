# Container information

| | |
| :--------------: | :------------- |
|**Name** | ENACT |
| **Description** | Visium HD pipeline: cell segmentation, bin-to-cell assignment and cell-type inference |
| **URL/repo** | https://github.com/Sanofi-Public/enact-pipeline |
| **URL/container** |  |
| **Version(s)** | `enact-SO==0.2.5` (configs from commit `5cf6f2a`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True jax=cpu tf_gpus=1`; image 12.9GB) |

## Notes

* GPU image (torch 2.5.1+cu121). `tensorflow[and-cuda]` is left out because its cuDNN pin clashes with torch, so StarDist runs on CPU (supported upstream).
* `setuptools<81` is pinned because dependencies still import `pkg_resources`.

## Usage

```bash
docker build -t enact:latest .
singularity build enact.sif docker-daemon://enact:latest

# smoke test
singularity exec --nv enact.sif bash -c 'python -c "import enact"'
```
