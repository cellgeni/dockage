# Container information

| | |
| :--------------: | :------------- |
|**Name** | CellFlow |
| **Description** | Predicts cellular responses to complex perturbations (drugs, gene KO, doses, covariates) |
| **URL/repo** | https://github.com/theislab/cellflow |
| **URL/container** |  |
| **Version(s)** | `cellflow-tools==0.0.9` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `jax=gpu`; image 10.5GB) |

## Notes

* GPU image (JAX). Upstream does not pin jax/flax; pinned to `jax[cuda12]==0.9.2` and `flax==0.12.6`, released around 0.0.9.

## Usage

```bash
docker build -t cellflow:latest .
singularity build cellflow.sif docker-daemon://cellflow:latest

# smoke test
singularity exec --nv cellflow.sif bash -c 'python -c "import cellflow"'
```
