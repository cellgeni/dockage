# Container information

| | |
| :--------------: | :------------- |
|**Name** | InSituPy |
| **Description** | Analysis of Xenium data with H&E/IF registration, region annotations and downstream analysis |
| **URL/repo** | https://github.com/SpatialPathology/InSituPy |
| **URL/container** |  |
| **Version(s)** | `insitupy-spatial[spatialdata]==0.12.1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 3.0GB) |

## Notes

* The PyPI package `insitupy` is an unrelated project; the correct one is `insitupy-spatial`.
* Qt/GL libraries added for napari, with `QT_QPA_PLATFORM=offscreen`.

## Usage

```bash
docker build -t insitupy:latest .
singularity build insitupy.sif docker-daemon://insitupy:latest

# smoke test
singularity exec insitupy.sif bash -c 'python -c "import insitupy"'
```
