# Container information

| | |
| :--------------: | :------------- |
|**Name** | STARCall |
| **Description** | Image-based sequencing workflow: stitching, alignment, peak calling and barcode decoding |
| **URL/repo** | https://github.com/FowlerLab/starcall-workflow |
| **URL/container** |  |
| **Version(s)** | commit `f2b486a3` (starcall `5eb3ad2e`, constitch `50cfd992`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True tf_gpus=1`; image 11.8GB) |

## Notes

* GPU image. TensorFlow 2.15.1 instead of upstream's 2.13.0, which clashes with torch and basicpy.
* Workflow is in `/opt/starcall-workflow`. CellProfiler is not included.
* `setuptools<81` is pinned because dependencies still import `pkg_resources`.
* :warning: The workflow's BaSiC rule uses an old pybasic-style API and may fail with current basicpy.

## Usage

```bash
docker build -t starcall:latest .
singularity build starcall.sif docker-daemon://starcall:latest

# smoke test
singularity exec --nv starcall.sif bash -c 'python -c "import starcall, constitch" && snakemake --version'
```
