# Container information

| | |
| :--------------: | :------------- |
|**Name** | OmiCLIP / Loki |
| **Description** | Histology–transcriptomics foundation model: alignment, annotation, deconvolution and expression prediction |
| **URL/repo** | https://github.com/GuangyuWangLab2021/Loki |
| **URL/container** |  |
| **Version(s)** | commit `c6d3eed9` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.3GB) |

## Notes

* GPU image, Python 3.10, torch 2.3.1+cu121 with upstream `setup.py` pins.
* `scanpy` and `scikit-learn` added (imported but not declared upstream).
* OmiCLIP weights on Hugging Face are not included.

## Usage

```bash
docker build -t loki:latest .
singularity build loki.sif docker-daemon://loki:latest

# smoke test
singularity exec --nv loki.sif bash -c 'python -c "import loki.align, loki.annotate, loki.predex"'
```
