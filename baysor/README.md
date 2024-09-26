# Container information

| | |
| :--------------: | :------------- |
|**Name** | Baysor |
| **Description** | This container is mainly for running Bayesian Segmentation of Spatial Transcriptomics Data using the tool `baysor` |
| **URL/repo** | https://github.com/kharchenkolab/Baysor |
| **Version(s)** | 0.6.2 |


# Singularity considerations

A path in the container needs to be writable.

```bash
singularity exec \
	--bind /tmp:/opt/baysor/share/julia/scratchspaces \
	baysor.sif \
    baysor -h
```
