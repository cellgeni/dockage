# Container information

| | |
| :--------------: | :------------- |
|**Name** | SFUMATO |
| **Description** | Spatial clusters/domains from transcript coordinates and labels only |
| **URL/repo** | https://github.com/ale2sia-g/SFUMATO |
| **URL/container** |  |
| **Version(s)** | commit `93806f5` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.1GB) |

## Notes

* GPU image (torch 2.5.1+cu121). Code is in `/opt/SFUMATO` on `PYTHONPATH`, so the repo's own `points2regions.py` is used.

## Usage

```bash
docker build -t sfumato:latest .
singularity build sfumato.sif docker-daemon://sfumato:latest

# smoke test
singularity exec --nv sfumato.sif bash -c 'cd /opt/SFUMATO && python -c "import bgm, preprocess, run_bgm_gpu"'
```
