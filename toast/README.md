# Container information

| | |
| :--------------: | :------------- |
|**Name** | TOAST |
| **Description** | Optimal-transport alignment of spatial transcriptomics sections using expression and positions |
| **URL/repo** | https://github.com/cecca46/TOAST |
| **URL/container** |  |
| **Version(s)** | tag `v1.1.2` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 1.3GB) |

## Notes

* Installed with upstream's fully pinned `requirements.txt`.

## Usage

```bash
docker build -t toast:latest .
singularity build toast.sif docker-daemon://toast:latest

# smoke test
singularity exec toast.sif bash -c 'toast --help'
```
