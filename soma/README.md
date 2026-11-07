# Container information

| | |
| :--------------: | :------------- |
|**Name** | soma |
| **Description** | Pathology foundation-model feature extraction, training and prediction on WSIs |
| **URL/repo** | https://github.com/clemsgrs/soma |
| **URL/container** |  |
| **Version(s)** | `soma-pathology==2.2.1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 11.8GB) |

## Notes

* :warning: Uses torch 2.8.0 cu126; the host driver must support CUDA 12.6.
* MUSK, CONCH, prov-gigapath and sam2 are pinned to commits. ASAP backend, flash-attn and upstream's dev tools are not included.
* Gated foundation models need `HF_TOKEN` at runtime.

## Usage

```bash
docker build -t soma:latest .
singularity build soma.sif docker-daemon://soma:latest

# smoke test
singularity exec --nv soma.sif bash -c 'soma --help'
```
