# Container information

| | |
| :--------------: | :------------- |
|**Name** | STaCker |
| **Description** | Alignment of spatial transcriptomics sections using image and transcriptomic features |
| **URL/repo** | https://github.com/regeneron-mpds/stacker |
| **URL/container** |  |
| **Version(s)** | commit `580a8214` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `tf_gpus=1`; image 15.1GB) |

## Notes

* Based on `nvcr.io/nvidia/tensorflow:22.07-tf2-py3` (TensorFlow 2.9, CUDA 11) instead of the house CUDA 12.1 base; this is upstream's only tested environment.
* `antspyx==0.3.8` is no longer on PyPI, so 0.4.2 is used. `code/` is on `PYTHONPATH`.

## Usage

```bash
docker build -t stacker:latest .
singularity build stacker.sif docker-daemon://stacker:latest

# smoke test
singularity exec --nv stacker.sif bash -c 'cd / && python -c "from libs.alignment import stacker_register"'
```
