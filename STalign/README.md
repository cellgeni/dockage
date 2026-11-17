# Container information

| | |
| :--------------: | :------------- |
|**Name** | STalign |
| **Description** | Align spatial transcriptomics sections to each other, to H&E images or to 3D atlases (LDDMM) |
| **URL/repo** | https://github.com/JEFworks-Lab/STalign |
| **URL/container** |  |
| **Version(s)** | `STalign==2.0.0` (git `8a84bf1`) |
| **Status** | :construction: Not yet built |

## Notes

* Not on PyPI; installed from GitHub at a pinned commit (2.0.0 is untagged upstream).
* CPU image. The optional C++ engine (`STalign._stalign_cpp`) is compiled at build time and the
  build fails if it is missing; it is ~5x faster than the torch backend on CPU.
* 3D atlas tutorials download Allen CCF volumes at runtime; nothing is baked into the image.

## Usage

```bash
docker build -t stalign:latest .
singularity build stalign.sif docker-daemon://stalign:latest

# smoke test
singularity exec stalign.sif bash -c 'python -c "import STalign, STalign._stalign_cpp"'
```
