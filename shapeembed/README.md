# Container information

| | |
| :--------------: | :------------- |
|**Name** | ShapeEmbed |
| **Description** | Self-supervised shape representation learning from 2D segmentation masks |
| **URL/repo** | https://github.com/uhlmanngroup/ShapeEmbed |
| **URL/container** |  |
| **Version(s)** | commit `da515f9` (+ ConvertBinaryMasksToDMs `71491b0`) |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True`; image 9.6GB) |

## Notes

* GPU image (torch 2.5.1). `shapeembed` is a wrapper for `python /opt/ShapeEmbed/shape_embed.py`.
* The companion ShapeEmbedLite repo is not included.

## Usage

```bash
docker build -t shapeembed:latest .
singularity build shapeembed.sif docker-daemon://shapeembed:latest

# smoke test
singularity exec --nv shapeembed.sif bash -c 'shapeembed --help'
```
