# Container information

| | |
| :--------------: | :------------- |
|**Name** | TACCO |
| **Description** | Transfer of annotations to cells and their combinations (deconvolution, mapping, spatial analysis) |
| **URL/repo** | https://github.com/simonwm/tacco |
| **URL/container** |  |
| **Version(s)** | `tacco==0.5.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 2.3GB) |

## Notes

* `LD_LIBRARY_PATH=/env/lib` so sparse_dot_mkl finds the pip-installed MKL.

## Usage

```bash
docker build -t tacco:latest .
singularity build tacco.sif docker-daemon://tacco:latest

# smoke test
singularity exec tacco.sif bash -c 'python -c "import tacco"'
```
