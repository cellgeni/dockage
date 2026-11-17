# Container information

| | |
| :--------------: | :------------- |
|**Name** | MicroSplit |
| **Description** | Splitting multiple structures imaged in a single fluorescence channel |
| **URL/repo** | https://github.com/CAREamics/MicroSplit-reproducibility |
| **URL/container** |  |
| **Version(s)** | commit `f45d01d`, `careamics[examples,wandb]==0.0.12` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.3GB) |

## Notes

* GPU image (torch 2.5.1+cu121). Repo (with notebooks) is cloned to `/opt/MicroSplit-reproducibility`.

## Usage

```bash
docker build -t microsplit:latest .
singularity build microsplit.sif docker-daemon://microsplit:latest

# smoke test
singularity exec --nv microsplit.sif bash -c 'python -c "import careamics, microsplit_reproducibility"'
```
