# Container information

| | |
| :--------------: | :------------- |
|**Name** | MuSpAn |
| **Description** | Multiscale spatial analysis toolbox (networks, topology, geometry, spatial statistics) |
| **URL/repo** | https://github.com/MuSpAn-Multiscale-Spatial-Analysis/MuSpAn-Public |
| **URL/container** |  |
| **Version(s)** | `1.2.5` |
| **Status** | :warning: UNTESTED (needs licence credentials to build) |

## Notes

* :warning: MuSpAn is licence-gated. Build with your credentials as BuildKit secrets (see the Dockerfile header):
* `DOCKER_BUILDKIT=1 docker build --secret id=muspan_user,src=muspan_user.txt --secret id=muspan_pass,src=muspan_pass.txt -t muspan .`
* The resulting image falls under MuSpAn's Academic Use Licence.

## Usage

```bash
docker build -t muspan:latest .
singularity build muspan.sif docker-daemon://muspan:latest

```
