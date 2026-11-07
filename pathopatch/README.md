# Container information

| | |
| :--------------: | :------------- |
|**Name** | PathoPatch |
| **Description** | WSI tissue detection, patch extraction, stain normalisation and QuPath annotation handling |
| **URL/repo** | https://github.com/TIO-IKIM/PathoPatcher |
| **URL/container** |  |
| **Version(s)** | `pathopatch==1.0.10` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.3GB) |

## Notes

* CLIs: `wsi_extraction`, `annotation_conversion`, `macenko_vector_generation`.
* OpenSlide comes from the `openslide-bin` wheel; optional cuCIM GPU acceleration included.

## Usage

```bash
docker build -t pathopatch:latest .
singularity build pathopatch.sif docker-daemon://pathopatch:latest

# smoke test
singularity exec --nv pathopatch.sif bash -c 'wsi_extraction --help'
```
