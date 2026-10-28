# Container information

| | |
| :--------------: | :------------- |
|**Name** | rapids-singlecell |
| **Description** | GPU-accelerated framework for scRNA analysis |
| **URL/repo** | https://github.com/scverse/rapids_singlecell |
| **URL/container** | https://quay.io/repository/cellgeni/rapids-singlecell |
| **Version(s)** | `0.13.2`, `0.14.1`, `0.18.1` |

## Notes

* From `0.16` onwards the prebuilt CUDA wheels are published as `rapids-singlecell-cu12` / `rapids-singlecell-cu13`
  (the plain `rapids-singlecell` package on PyPI is source-only), so `Dockerfile_0.18.1` installs `rapids-singlecell-cu12`.
* `0.18.1` uses RAPIDS `26.10` and Python 3.13.
* The upstream `0.18.1` wheels contain kernels for compute capability 7.5+ only (T4, A100, RTX 30/40, L4/L40, H100, ...).
  On older GPUs such as the V100 (7.0), rapids-singlecell's own kernels fail with `no kernel image is available for execution on the device`.
* `cuxfilter-cu12` is no longer installed (no RAPIDS `26.10` release; not used by rapids-singlecell).
