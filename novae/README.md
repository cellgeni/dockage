# Container information

| | |
| :--------------: | :------------- |
|**Name** | Novae |
| **Description** | Graph-based foundation model for spatial domains across technologies |
| **URL/repo** | https://github.com/MICS-Lab/novae |
| **URL/container** |  |
| **Version(s)** | `novae==1.1.2` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.7GB) |

## Notes

* GPU image (torch 2.5.1). Pretrained models download from Hugging Face at runtime.

## Usage

```bash
docker build -t novae:latest .
singularity build novae.sif docker-daemon://novae:latest

# smoke test
singularity exec --nv novae.sif bash -c 'python -c "import novae"'
```
