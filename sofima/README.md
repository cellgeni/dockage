# Container information

| | |
| :--------------: | :------------- |
|**Name** | SOFIMA |
| **Description** | Scalable optical-flow-based image montaging and alignment (2D/3D) |
| **URL/repo** | https://github.com/google-research/sofima |
| **URL/container** |  |
| **Version(s)** | commit `c8b5e254` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `jax=gpu`; image 9.8GB) |

## Notes

* GPU image (JAX). `jax[cuda12]==0.4.38` chosen for the APIs sofima uses.

## Usage

```bash
docker build -t sofima:latest .
singularity build sofima.sif docker-daemon://sofima:latest

# smoke test
singularity exec --nv sofima.sif bash -c 'python -c "from sofima import flow_field, mesh, stitch_rigid, stitch_elastic, warp"'
```
