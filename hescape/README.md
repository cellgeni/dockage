# Container information

| | |
| :--------------: | :------------- |
|**Name** | HESCAPE |
| **Description** | Benchmark for cross-modal learning between histology and gene expression |
| **URL/repo** | https://github.com/peng-lab/hescape |
| **URL/container** |  |
| **Version(s)** | commit `bd54704` (+ CONCH `141cc09`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True jax=cpu`; image 10.6GB) |

## Notes

* Installed with `--no-sources`: the drvi branch upstream points at no longer exists, so `drvi-py==0.2.0` from PyPI is used instead.
* CONCH is installed from git (the PyPI package `conch` is unrelated). `transformers<5`.
* Weights (some gated on Hugging Face) and datasets are fetched at runtime.

## Usage

```bash
docker build -t hescape:latest .
singularity build hescape.sif docker-daemon://hescape:latest

# smoke test
singularity exec --nv hescape.sif bash -c 'python -c "import hescape; from conch.open_clip_custom import create_model_from_pretrained"'
```
