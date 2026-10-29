# Container information

| | |
| :--------------: | :------------- |
|**Name** | point_cloud_linking |
| **Description** | Linking and registration of 3D point clouds (e.g. spot / nuclei centroids) across imaging cycles |
| **URL/repo** | https://github.com/soft-matter/trackpy, https://github.com/neka-nat/probreg |
| **URL/container** | https://quay.io/repository/cellgeni/point_cloud_linking |
| **Version(s)** | `trackpy==0.7`, `probreg==0.3.8`, `spatialdata==0.5.0` |

## Notes

* Python 3.11.
* [`trackpy`](https://pypi.org/project/trackpy/) `0.7` - nearest-neighbour linking of points between frames/cycles.
* [`probreg`](https://pypi.org/project/probreg/) `0.3.8` - probabilistic point-set registration (CPD, FilterReg, BCPD, ...).
  It is built from source (no wheel), so `build-essential` is in the image. Its `open3d` dependency
  needs `libGL`/`libEGL`/`libX11`/`libgomp`/`libusb`/`libidn2` at import time; these are installed
  so it imports headlessly.
* [`spatialdata`](https://pypi.org/project/spatialdata/) `0.5.0` for I/O; `setuptools<81` is pinned because its
  `xarray_schema` dependency still imports `pkg_resources`.
* `numcodecs<0.16` is pinned because `aicsimageio` caps `zarr` at 2.15, which uses `numcodecs.blosc.cbuffer_sizes` (removed in 0.16).
* `aicsimageio==4.14.0` and `readlif==0.6.6` for reading microscopy images (incl. Leica `.lif`), `fire==0.7.1` for CLIs.
* `pandas==2.3.3`, `scipy==1.15.3`.
* `procps` is included for Nextflow.

## Usage

```bash
docker build -t point_cloud_linking:0.1 .

docker run --rm -v $PWD/data:/data point_cloud_linking:0.1 python your_script.py
```

```python
import numpy as np
from probreg import cpd

tf_param, _, _ = cpd.registration_cpd(source_xyz, target_xyz, tf_type_name="rigid")
aligned = tf_param.transform(source_xyz)
```
