# Container information

| | |
| :--------------: | :------------- |
|**Name** | RStudio |
| **Description** | This container is mainly for running RStudio (now Posit). The base image containging rstudio comes from the Rocker Project |
| **URL/repo** | https://github.com/rocker-org/rocker-versioned2 |
| **Version(s)** | `4.4.1`, `4.5.1`, `4.5.2` |
| **QUAY** | https://quay.io/repository/cellgeni/rstudio |


# Singularity considerations

- `ldap_auth` file present in this repo allows to use LDAP authentication with RStudio instead of a custom password being setup. This requires the image to have the ldap3 python package installed. You still need to pass the username when launching rserver with `--server-user`.
- We also recommend using custom `logging.conf` to control verbosity.
- Some additional bindings are required to fully use rstudio and interact with LSF.
- Some of the paths inside the container will need to be writable, particularly the settings folders. In the example, `<WORK_DIR>` can be replaced with a folder you control. The bind on `<WORK_DIR>` shouldn't take much storage so it's fine to bind that to somewhere on your home folder.
- By default an rstudio folde will try to be created in /tmp. Because this may be a shared environment and to allow multiple users at the same time, in this example a custom bind is in place for that using `/tmp/$(whoami)/rstudio`
- `<PORT>` is an open port on the host you're launching RStudio. You can set `PORT` as an environment variable with the first open free port using this:
```bash
PORT=$(python3 -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
```
- `/path/to/rstudio.sif` is the path to the singularity image built for rstudio on the filesystem.

### Example
```bash
singularity exec \
    --pid \
    --bind /path/to/logging.conf:/etc/rstudio/logging.conf:ro \
    --bind /path/to/ldap_auth:/usr/lib/rstudio-server/bin/ldap_auth:ro \
    --bind /sys/fs/cgroup \
    --bind /etc/lsf.conf \
    --bind /usr/local/lsf \
    --bind <WORK_DIR>/keybindings:/etc/rstudio/keybindings \
    --bind <WORK_DIR>/run:/run \
    --bind /tmp/$(whoami)/rstudio:/tmp \
    --bind <WORK_DIR>/rstudio-server:/var/lib/rstudio-server \
    --bind /software,/nfs,/lustre \
    /path/to/rstudio.sif \
    rserver \
        --server-user $USER \
        --www-port <PORT> \
        --www-address 0.0.0.0 \
        --auth-none 0  \
        --auth-pam-helper-path ldap_auth
```
