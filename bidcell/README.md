# Container information

| | |
| :--------------: | :------------- |
|**Name** | BIDCell |
| **Description** | Biologically-informed deep learning cell segmentation for subcellular spatial transcriptomics |
| **URL/repo** | https://github.com/SydneyBioX/BIDCell |
| **URL/container** |  |
| **Version(s)** | `bidcell==1.0.3` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.4GB) |

## Notes

* GPU image; torch 2.1.2+cu121 and key versions taken from upstream's `pdm.lock` (cellpose 2.2.3, numpy 1.24.4, segmentation-models-pytorch 0.3.3).
* Cellpose and encoder weights download at runtime.

## Usage

```bash
docker build -t bidcell:latest .
singularity build bidcell.sif docker-daemon://bidcell:latest

# smoke test
singularity exec --nv bidcell.sif bash -c 'python -c "from bidcell import BIDCellModel"'
```
