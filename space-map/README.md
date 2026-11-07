# Container information

| | |
| :--------------: | :------------- |
|**Name** | SpaceMap |
| **Description** | Atlas-level 3D tissue reconstruction and alignment of Xenium/H&E sections |
| **URL/repo** | https://github.com/czhu/space-map |
| **URL/container** |  |
| **Version(s)** | commit `fe0eb87` (`v0.2.0`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.9GB) |

## Notes

* The link in our tool sheet (a12910/space-map) is dead; czhu/space-map is the current upstream.
* `opencv-python<5`. kornia downloads LoFTR weights on first use.
* :warning: Licence is PolyForm Noncommercial.

## Usage

```bash
docker build -t space-map:latest .
singularity build space-map.sif docker-daemon://space-map:latest

# smoke test
singularity exec --nv space-map.sif bash -c 'space-map --help'
```
