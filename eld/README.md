# Container information

| | |
| :--------------: | :------------- |
|**Name** | ELD |
| **Description** | Effortless Landmark Detection for serial-section alignment of H&E/RGB images |
| **URL/repo** | https://github.com/ekvall93/ELD |
| **URL/container** |  |
| **Version(s)** | commit `79ba97bd` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.5GB) |

## Notes

* GPU image, Python 3.9 with torch 1.9.0+cu111 as upstream requires; `visdom==0.2.4`.
* The FAN checkpoint ships in the repo at `/opt/ELD`; `eld-train` looks for it by relative path, so run from `/opt/ELD` or pass `--checkpoint`.
* `setuptools<81` is pinned because visdom still imports `pkg_resources` at build time.

## Usage

```bash
docker build -t eld:latest .
singularity build eld.sif docker-daemon://eld:latest

# smoke test
singularity exec --nv eld.sif bash -c 'eld-train --help'
```
