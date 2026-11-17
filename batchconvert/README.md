# Container information

| | |
| :--------------: | :------------- |
|**Name** | BatchConvert |
| **Description** | Nextflow-based CLI to batch-convert image collections to OME-TIFF or OME-Zarr |
| **URL/repo** | https://github.com/Euro-BioImaging/BatchConvert |
| **URL/container** |  |
| **Version(s)** | commit `9015e71c`, Nextflow `24.10.5`, bioformats2raw `0.12.1`, bftools `8.3.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 0.9GB) |

## Notes

* Default profile switched from `conda` to `manual`, so the tools on `PATH` are used.
* Only local/mounted paths are supported: S3 (`mc`) and Aspera transfer are not included (MinIO no longer distributes `mc` binaries).
* User config is written to `$HOME/.batchconvert` on first run.
* Jupyter lives in a separate venv at `/env`, appended to `PATH`, so BatchConvert keeps using the system Python.

## Usage

```bash
docker build -t batchconvert:latest .
singularity build batchconvert.sif docker-daemon://batchconvert:latest

# smoke test
singularity exec batchconvert.sif bash -c 'batchconvert --help'
```
