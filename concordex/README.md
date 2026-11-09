# Container information

| | |
| :--------------: | :------------- |
|**Name** | concordex |
| **Description** | Identification of spatial homogeneous regions using a kNN-graph concordance statistic |
| **URL/repo** | https://github.com/pachterlab/concordex |
| **URL/container** |  |
| **Version(s)** | `concordex==2.0.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 1.6GB) |

## Notes

* Python implementation; `scanpy==1.11.4` and `squidpy==1.6.5` added for the surrounding workflow.

## Usage

```bash
docker build -t concordex:latest .
singularity build concordex.sif docker-daemon://concordex:latest

# smoke test
singularity exec concordex.sif bash -c 'python -c "from concordex.tools import calculate_concordex"'
```
