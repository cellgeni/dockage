# Container information

| | |
| :--------------: | :------------- |
|**Name** | DELiVR |
| **Description** | Deep-learning cFos/microglia detection in 3D light-sheet brain data with VR annotation |
| **URL/repo** | https://github.com/erturklab/delivr_cfos |
| **URL/container** |  |
| **Version(s)** | commit `51ef796` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 12.0GB) |

## Notes

* GPU image following upstream pins (torch 2.0.1+cu117 wheels bundle their own CUDA libraries).
* Model and atlas files are pulled into `/delivr`; ilastik 1.4.0b8 is included.
* :warning: TeraConverter (SharePoint only) and mBrainAligner (Google Drive; one step is Windows-only) are not included and must be mounted. brainrender (visualisation) is not installed.
* `setuptools<81` is pinned because dependencies still import `distutils`/`pkg_resources`.

## Usage

```bash
docker build -t delivr:latest .
singularity build delivr.sif docker-daemon://delivr:latest

# smoke test
singularity exec --nv delivr.sif bash -c 'python -c "import torch, monai, cc3d" && ls /delivr'
```
