# Container information

| | |
| :--------------: | :------------- |
|**Name** | Slideflow |
| **Description** | Deep learning toolkit for digital histopathology |
| **URL/repo** | https://github.com/slideflow/slideflow |
| **URL/container** |  |
| **Version(s)** | `slideflow[torch]==3.0.2` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 11.1GB) |

## Notes

* GPU image, torch 2.3.1. Slides are read with libvips (no cuCIM).
* The `slideflow-gpl` and `slideflow-noncommercial` add-ons are included, as in upstream's own image.
* `setuptools<81` is pinned because dependencies still import `pkg_resources`.

## Usage

```bash
docker build -t slideflow:latest .
singularity build slideflow.sif docker-daemon://slideflow:latest

# smoke test
singularity exec --nv slideflow.sif bash -c 'python -c "import slideflow"'
```
