# Container information

| | |
| :--------------: | :------------- |
|**Name** | pyapr |
| **Description** | Content-adaptive storage and processing of large volumetric microscopy images using the Adaptive Particle Representation (APR); Python bindings for LibAPR |
| **URL/repo** | https://github.com/AdaptiveParticles/pyapr |
| **URL/container** | https://quay.io/repository/cellgeni/pyapr |
| **Version(s)** | `1.0.7` (headless), `1.0.7-napari` (with napari-apr-viewer) |

## Images

| Dockerfile | Contents |
| :-- | :-- |
| [`Dockerfile`](Dockerfile) | headless pyapr + jupyterlab/papermill. For conversion and processing. |
| [`Dockerfile.napari`](Dockerfile.napari) | pyapr + napari 0.5.6 + [napari-apr-viewer](https://github.com/AdaptiveParticles/napari-apr-viewer) 1.0.1, for visualising `.apr` files. Needs a display. |

## Notes

* Python 3.11 - upstream publishes wheels for cp38-cp311 only.
* `numpy` is pinned to `<2`: the pybind11 extension in the 1.0.7 wheels is built
  against the NumPy 1.x C-API.
* The build is CPU-only (`pyapr.cuda_enabled()` is `False`).
* `jupyterlab`, `ipykernel` and `papermill` are included, per the repo conventions.

## Usage

```python
import pyapr, tifffile

img = tifffile.imread('my_image.tif')          # uint16 3D stack
apr, parts = pyapr.converter.get_apr(img)      # pixels -> APR
pyapr.io.write('my_image.apr', apr, parts)

apr, parts = pyapr.io.read('my_image.apr')
rec = pyapr.reconstruction.reconstruct_constant(apr, parts)   # APR -> pixels
```

The interactive viewers (`pyapr.viewer.parts_viewer`, `raycast_viewer`) are Qt-based
and need a display; `QT_QPA_PLATFORM=offscreen` is set so headless use works, but for
the viewers you must forward X11 and override that variable.

## Viewing .apr files (Dockerfile.napari)

Upstream napari-apr-viewer 1.0.1 does not work with current napari, for two
independent reasons:

1. It registers itself only through the removed npe1 entry point group
   `napari.plugin`, so the `*.apr` reader is rejected as *"not a compatible
   reader"* and the dock widgets never appear.
2. pyapr's `APRSlicer.__getitem__` drops an axis indexed with a *slice*, where
   numpy keeps it. napari's slicing path then projects over a displayed axis and
   `np.transpose(data, order)` fails with *"axes don't match array"*.

Both are fixed in [BioinfoTongLI/napari-apr-viewer](https://github.com/BioinfoTongLI/napari-apr-viewer)
(branch `fix-modern-napari`), which this image installs; napari is therefore left
unpinned. Point the build at a different fork or ref with `--build-arg
APR_VIEWER_REPO=... --build-arg APR_VIEWER_REF=...`.

Run it with a display (X11 forwarding shown):

```bash
docker run --rm -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /path/to/data:/data \
    pyapr:1.0.7-napari napari /data/my_image.apr
```

The plugin contributes a `*.apr` reader, `.apr` writers for image and labels
layers, and four dock widgets (`APR Viewer`, `Convert image to APR`,
`Convert APR to image`, `Threshold`). Layers are backed by `APRSlicer`, so slices
are reconstructed lazily - a 44705x88328 plane renders in ~0.4 s.
