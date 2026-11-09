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

* Slim core install; the wheel already contains the built frontend.
* Serve a project with the bundled `mdv-serve` launcher. Upstream `serve_project()` binds Flask to the container's loopback, so a Docker-published port can't reach it. `mdv-serve` binds `0.0.0.0` under Docker/Podman, so the published port works, and `127.0.0.1` under Singularity, which shares the host network. Override with `--host` or `MDV_HOST`. Under Docker, publish on the host loopback only (`-p 127.0.0.1:5050:5050`), because the viewer has no authentication.
* The multi-user server (`mdvtools[app]` + Postgres) is not included; use upstream's docker-compose setup for that.

## Usage

```bash
docker build -t mdv:latest .
singularity build mdv.sif docker-daemon://mdv:latest

# smoke test
singularity exec mdv.sif bash -c 'mdvtools --help'

# serve a project (Docker): container binds 0.0.0.0, host exposes it on loopback only
docker run --rm -p 127.0.0.1:5050:5050 -v $PWD/myproject:/proj mdv:latest mdv-serve /proj

# serve a project (Singularity shares the host network; keep the loopback default and ssh-tunnel)
singularity exec mdv.sif mdv-serve /path/to/myproject --port 5050
```
