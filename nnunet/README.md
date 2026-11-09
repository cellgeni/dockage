# Container information

| | |
| :--------------: | :------------- |
|**Name** | nnU-Net |
| **Description** | Self-configuring deep learning framework for 2D/3D image segmentation |
| **URL/repo** | https://github.com/MIC-DKFZ/nnUNet |
| **URL/container** |  |
| **Version(s)** | `nnunetv2==2.8.1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.9GB) |

## Notes

* GPU image (torch 2.5.1+cu121).
* `nnUNet_raw`, `nnUNet_preprocessed` and `nnUNet_results` default to `/data/...`; override or bind-mount them. No pretrained models are bundled.

## Usage

```bash
docker build -t nnunet:latest .
singularity build nnunet.sif docker-daemon://nnunet:latest

# smoke test
singularity exec --nv nnunet.sif bash -c 'nnUNetv2_predict -h'
```
