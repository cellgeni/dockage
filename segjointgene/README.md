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

# training: the image is read-only, but main.py sets paths.root to /opt/segjointgene and
# Hydra writes experiments under ${paths.root}/experiment. Pass writable overrides after the
# CLI flags (later Hydra overrides win). paths.data_dir must be writable (preprocessing
# writes Simulation/ and Simulation_image/ there; raw inputs go in Simulation_raw/).
singularity exec --nv -B /path/to/work:/work segjointgene.sif \
  python /opt/segjointgene/main.py --sub_path run1 --net_epoch 100 \
    paths.root=/work/out paths.data_dir=/work/data
# or: bash /opt/segjointgene/scripts/run_cid.sh /work/data run1 100 paths.root=/work/out
```
