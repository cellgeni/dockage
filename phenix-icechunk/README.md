# Container information

|                   |                                                                                                                                                                                                     |
| :---------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     **Name**      | phenix-icechunk                                                                                                                                                                                     |
|  **Description**  | Expose an Opera Phenix / Harmony `Index.xml` export as a virtual OME-Zarr 0.5 HCS plate inside an icechunk repo (no pixels copied); optional flatfield correction, z projection and OME-TIFF export |
|   **URL/repo**    | https://github.com/BioinfoTongLI/phenix-icechunk                                                                                                                                                    |
|   **URL/pypi**    | https://pypi.org/project/phenix-icechunk/                                                                                                                                                           |
| **URL/container** | https://quay.io/repository/cellgeni/phenix-icechunk                                                                                                                                                 |
|  **Version(s)**   | `0.3.2`                                                                                                                                                                                             |

## Notes

- Python 3.12 - upstream requires `>=3.12`.
- Installed with the `[extras]` (`dask`, `ome-types`, `pandas`).
- `jupyterlab`, `ipykernel` and `papermill` are included, per the repo conventions.
- Chunks are virtual references to the original TIFFs via `file://` URLs, so bind-mount
  the Phenix export at the **same path** inside the container when converting and reading.

## Usage

```bash
docker build -t phenix-icechunk:0.3.2 .

docker run --rm -v /path/to/export:/path/to/export -v $PWD/data:/data phenix-icechunk:0.3.2 \
    phenix-icechunk "/path/to/export/Measurement 2/Images/Index.xml" /data/plate.icechunk \
    --flatfield --zproject --ome-tiff /data/ome_tiff
```

```python
from phenix_icechunk import open_plate, open_field

plate = open_plate("/data/plate.icechunk")
da = open_field(plate, "A4", 0)        # lazy xr.DataArray (t, c, z, y, x)
```
