# Container information

| | |
| :--------------: | :------------- |
|**Name** | LazySlide |
| **Description** | Whole-slide image processing, tissue/cell segmentation and foundation-model features, integrated with scverse |
| **URL/repo** | https://github.com/rendeirolab/LazySlide |
| **URL/container** |  |
| **Version(s)** | `lazyslide[all,models]==0.13.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.9GB) |

## Notes

* GPU image, Python 3.12, torch 2.5.1+cu121.
* Foundation-model weights download from Hugging Face on first use; gated models need `HF_TOKEN`.

## Usage

```bash
docker build -t lazyslide:latest .
singularity build lazyslide.sif docker-daemon://lazyslide:latest

# smoke test
singularity exec --nv lazyslide.sif bash -c 'python -c "import lazyslide, wsidata"'
```
