# Container information

| | |
| :--------------: | :------------- |
|**Name** | GrandQC |
| **Description** | Tissue detection and artefact segmentation/QC for H&E whole-slide images |
| **URL/repo** | https://github.com/cpath-ukk/grandqc |
| **URL/container** |  |
| **Version(s)** | commit `002688d` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.4GB) |

## Notes

* GPU image, Python 3.10, torch 2.0.1+cu118 as upstream pins; system OpenSlide.
* Zenodo checkpoints (~100 MB) are baked into `/opt/grandqc/models`, because the scripts hard-code `./models`; ImageNet encoder weights are cached too.

## Usage

```bash
docker build -t grandqc:latest .
singularity build grandqc.sif docker-daemon://grandqc:latest

# smoke test
singularity exec --nv grandqc.sif bash -c 'python -c "import openslide, segmentation_models_pytorch" && ls /opt/grandqc'
```
