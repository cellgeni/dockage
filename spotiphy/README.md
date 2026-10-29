# Container information

| | |
| :--------------: | :------------- |
|**Name** | Spotiphy |
| **Description** | Spot deconvolution with single-cell resolution imputation from H&E segmentation |
| **URL/repo** | https://github.com/jyyulab/Spotiphy |
| **URL/container** |  |
| **Version(s)** | `spotiphy==0.3.1` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK, GPU probe: `torch_cuda=True tf_gpus=1`; image 12.4GB) |

## Notes

* GPU image; torch 2.3.1 and tensorflow 2.16.2 (for StarDist) added as the README says. StarDist weights download on first use.
* `setuptools<81` is pinned because dependencies still import `pkg_resources`.

## Usage

```bash
docker build -t spotiphy:latest .
singularity build spotiphy.sif docker-daemon://spotiphy:latest

# smoke test
singularity exec --nv spotiphy.sif bash -c 'python -c "import spotiphy, stardist"'
```
