# Container information

| | |
| :--------------: | :------------- |
|**Name** | Baysor |
| **Description** | This container is mainly for running Bayesian Segmentation of Spatial Transcriptomics Data using the tool `baysor` |
| **URL/repo** | https://github.com/kharchenkolab/Baysor |
| **Version(s)** | 0.6.2, 0.7.1 |


# Singularity considerations for version 0.6.2

A path in the container needs to be writable.

```bash
singularity exec \
	--bind /tmp:/opt/baysor/share/julia/scratchspaces \
	baysor.sif \
    baysor -h
```

# Considerations for version 0.7.1

MKL_jll has a lazy loaded artifact. That means it will be downloaded the first time it runs. This can't really happen inside singularity, so it's been added as an artifact in Artifacts.toml so it's downloaded at build time instead.
