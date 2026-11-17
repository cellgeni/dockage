# Container information

| | |
| :--------------: | :------------- |
|**Name** | FICTURE |
| **Description** | Segmentation-free inference of spatial factors and cell types from transcript coordinates |
| **URL/repo** | https://github.com/seqscope/ficture |
| **URL/container** |  |
| **Version(s)** | `ficture==0.0.5.7` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 1.7GB) |

## Notes

* Includes make, perl, pigz and tabix used by the pipeline. Upstream deps are unpinned.
* :warning: Licence is CC BY-NC.

## Usage

```bash
docker build -t ficture:latest .
singularity build ficture.sif docker-daemon://ficture:latest

# smoke test
singularity exec ficture.sif bash -c 'ficture run_together -h'
```
