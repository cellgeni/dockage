# Container information

| | |
| :--------------: | :------------- |
|**Name** | Palomero |
| **Description** | palom-based image registration for OMERO images, with ROI transfer |
| **URL/repo** | https://github.com/Yu-AnChen/palomero |
| **URL/container** |  |
| **Version(s)** | release `v2026.7.2` (`[webapp]`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 3.1GB) |

## Notes

* Includes Glencoe's prebuilt `zeroc-ice` cp310 wheel. Log in with `omero login -s <server> -u <user>`, then `palomero --help` or `palomero-web`.

## Usage

```bash
docker build -t palomero:latest .
singularity build palomero.sif docker-daemon://palomero:latest

# smoke test
singularity exec palomero.sif bash -c 'palomero --help'
```
