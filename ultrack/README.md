# Container information

| | |
| :--------------: | :------------- |
|**Name** | Ultrack |
| **Description** | Large-scale multi-hypothesis cell tracking from segmentation hierarchies |
| **URL/repo** | https://github.com/royerlab/ultrack |
| **URL/container** |  |
| **Version(s)** | `ultrack==0.8.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 11.7GB) |

## Notes

* GPU image with cupy and cuCIM; napari[pyqt5] with `QT_QPA_PLATFORM=offscreen`.
* :warning: The default Gurobi solver needs a licence mounted at runtime; without it ultrack falls back to CBC.

## Usage

```bash
docker build -t ultrack:latest .
singularity build ultrack.sif docker-daemon://ultrack:latest

# smoke test
singularity exec --nv ultrack.sif bash -c 'ultrack --help'
```
