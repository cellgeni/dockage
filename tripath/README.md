# Container information

| | |
| :--------------: | :------------- |
|**Name** | TriPath |
| **Description** | Weakly supervised 3D pathology analysis (CT, light-sheet, stacked H&E) |
| **URL/repo** | https://github.com/mahmoodlab/TriPath |
| **URL/container** |  |
| **Version(s)** | commit `76e30b5f` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.7GB) |

## Notes

* GPU image; upstream `requirements.txt` (torch 2.0.1). Scripts are in `/opt/TriPath` on `PYTHONPATH`.
* Encoder weights download at runtime.
* :warning: Licence is CC BY-NC-ND.

## Usage

```bash
docker build -t tripath:latest .
singularity build tripath.sif docker-daemon://tripath:latest

# smoke test
singularity exec --nv tripath.sif bash -c 'python -c "import monai, openslide, sksurv, pytorchvideo" && ls /opt/TriPath'
```
