# Container information

| | |
| :--------------: | :------------- |
|**Name** | TIAToolbox |
| **Description** | Computational pathology toolbox: WSI reading, stain normalisation, pretrained models |
| **URL/repo** | https://github.com/TissueImageAnalytics/tiatoolbox |
| **URL/container** |  |
| **Version(s)** | `tiatoolbox==2.1.3` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.4GB) |

## Notes

* GPU image (torch 2.5.1). Recent transformers refuses `.bin` weights with torch<2.6; safetensors weights load fine.

## Usage

```bash
docker build -t tiatoolbox:latest .
singularity build tiatoolbox.sif docker-daemon://tiatoolbox:latest

# smoke test
singularity exec --nv tiatoolbox.sif bash -c 'tiatoolbox --help'
```
