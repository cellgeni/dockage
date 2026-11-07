# Container information

| | |
| :--------------: | :------------- |
|**Name** | SegJointGene |
| **Description** | Joint cell segmentation and cell typing for spatial transcriptomics |
| **URL/repo** | https://github.com/daifengwanglab/segjointgene |
| **URL/container** |  |
| **Version(s)** | commit `41365a3` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 10.3GB) |

## Notes

* GPU image (torch 2.5.1+cu121). Upstream requirements are unpinned. Code is in `/opt/segjointgene` (working directory).

## Usage

```bash
docker build -t segjointgene:latest .
singularity build segjointgene.sif docker-daemon://segjointgene:latest

# smoke test
singularity exec --nv segjointgene.sif bash -c 'cd /opt/segjointgene && python scripts/check_env.py'
```
