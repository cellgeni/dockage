# Container information

| | |
| :--------------: | :------------- |
|**Name** | VitaminP |
| **Description** | Whole-cell (not only nuclei) segmentation on H&E, learned from paired IF/H&E |
| **URL/repo** | https://github.com/idso-fa1-pathology/VitaminP |
| **URL/container** |  |
| **Version(s)** | `vitaminp[wsi]==0.3.2` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.6GB) |

## Notes

* GPU image (torch 2.4.1+cu121). Weights download the first time a model is loaded (not baked in).

## Usage

```bash
docker build -t vitaminp:latest .
singularity build vitaminp.sif docker-daemon://vitaminp:latest

# smoke test
singularity exec --nv vitaminp.sif bash -c 'python -c "import vitaminp"'
```
