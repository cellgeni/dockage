# Container information

| | |
| :--------------: | :------------- |
|**Name** | MDV |
| **Description** | Multi-Dimensional Viewer: browser-based exploration of single-cell, spatial and image data |
| **URL/repo** | https://github.com/Taylor-CCB-Group/MDV |
| **URL/container** |  |
| **Version(s)** | `mdvtools==1.3.0` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 2.1GB) |

## Notes

* Slim core install; the wheel already contains the built frontend. Serve a project on port 5050 with `serve_project`.
* The multi-user server (`mdvtools[app]` + Postgres) is not included; use upstream's docker-compose setup for that.

## Usage

```bash
docker build -t mdv:latest .
singularity build mdv.sif docker-daemon://mdv:latest

# smoke test
singularity exec mdv.sif bash -c 'mdvtools --help'
```
