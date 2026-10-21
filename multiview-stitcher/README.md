# Container information

| | |
| :--------------: | :------------- |
|**Name** | multiview-stitcher |
| **Description** | Registration and fusion of large imaging datasets in 2D and 3D (tile stitching, multi-view and multi-channel alignment) |
| **URL/repo** | https://github.com/multiview-stitcher/multiview-stitcher |
| **URL/pypi** | https://pypi.org/project/multiview-stitcher/ |
| **URL/docs** | https://multiview-stitcher.github.io/multiview-stitcher/ |
| **URL/container** | https://quay.io/repository/cellgeni/multiview-stitcher |
| **Version(s)** | `0.1.62` |

## Notes

* Python 3.12 - upstream requires `>=3.11`.
* Installed with the `[ants,itk-elastix,czi,imaris,distributed]` extras: ANTsPy and ITK-elastix
  registration backends, CZI and Imaris readers, and `distributed` / `dask-jobqueue` / `bokeh`
  for running on a Dask cluster.
* Not included: `[gpu-cuda12]` (CuPy) and the napari-based `[playground]` extras.
* `jupyterlab`, `ipykernel` and `papermill` are included, per the repo conventions.

## Usage

```bash
docker build -t multiview-stitcher:0.1.62 .

docker run --rm -it -v $PWD/data:/data -p 8888:8888 multiview-stitcher:0.1.62 \
    jupyter lab --ip 0.0.0.0 --no-browser --allow-root
```

```python
from multiview_stitcher import msi_utils, registration, fusion

msims = [msi_utils.get_msim_from_sim(sim, scale_factors=[]) for sim in sims]
params = registration.register(msims, reg_channel_index=0, transform_key="stage_metadata",
                               new_transform_key="translation_registered")
fused = fusion.fuse([msi_utils.get_sim_from_msim(m) for m in msims],
                    transform_key="translation_registered")
```
