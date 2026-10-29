# Container information

| | |
| :--------------: | :------------- |
|**Name** | CellSeg3D |
| **Description** | Self-supervised and supervised 3D cell segmentation (napari plugin) |
| **URL/repo** | https://github.com/AdaptiveMotorControlLab/CellSeg3D |
| **URL/container** |  |
| **Version(s)** | `napari-cellseg3d[crf,onnx-cpu]==0.2.4` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 12.2GB) |

## Notes

* GPU image (torch 2.5.1+cu121). ONNX models run on CPU (`onnx-cpu`), because current onnxruntime-gpu needs cuDNN 9.
* Includes Qt/X11 libraries for napari and an OpenCL loader for pyclesperanto. Model weights download on first use.
* No CLI: use it as a Python library or napari plugin.

## Usage

```bash
docker build -t cellseg3d:latest .
singularity build cellseg3d.sif docker-daemon://cellseg3d:latest

# smoke test
singularity exec --nv cellseg3d.sif bash -c 'python -c "import napari_cellseg3d"'
```
