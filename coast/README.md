# Container information

| | |
| :--------------: | :------------- |
|**Name** | COAST |
| **Description** | Alignment of spot-based spatial transcriptomics sections using image and expression |
| **URL/repo** | https://github.com/mahfouzlab/COAST |
| **URL/container** |  |
| **Version(s)** | commit `c3f446ed` (+ CAST `3ebcf4fb`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 11.3GB) |

## Notes

* Script repo: cloned to `/opt/COAST` and put on `PYTHONPATH`.
* GPU image with torch 2.4.1 (instead of upstream's 2.5.1) so the DGL cu121 wheel needed by CAST works; `numpy<2`.
* DINO ViT-S/16 weights download via torch.hub at runtime (needs network).

## Usage

```bash
docker build -t coast:latest .
singularity build coast.sif docker-daemon://coast:latest

# smoke test
singularity exec --nv coast.sif bash -c 'python -c "import CAST, scanpy" && ls /opt/COAST'
```
