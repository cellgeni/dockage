# Container information

| | |
| :--------------: | :------------- |
|**Name** | spDDB |
| **Description** | Benchmark of spot deconvolution and domain detection, with the SynthST simulator |
| **URL/repo** | https://github.com/Zafar-Lab/spDDB |
| **URL/container** |  |
| **Version(s)** | commit `d3b2bec` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True tf_gpus=1`; image 11.1GB) |

## Notes

* :warning: Covers only the SynthST simulator and evaluation metrics; the ~35 benchmarked methods are not included.
* TensorFlow 2.15.1 and pandas 2.1.4 (instead of upstream's 2.13 / 2.0.3) to work on CUDA 12.

## Usage

```bash
docker build -t spddb:latest .
singularity build spddb.sif docker-daemon://spddb:latest

# smoke test
singularity exec --nv spddb.sif bash -c 'python -c "import SynthST"'
```
