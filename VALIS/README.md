# Container information

| | |
| :--------------: | :------------- |
|**Name** | VALIS |
| **Description** | Virtual Alignment of pathoLogy Image Series | 
| **URL/repo** | https://github.com/MathOnco/valis |
| **URL/container** | https://quay.io/cellgeni/valis:1.2.0 |
| **Version(s)** | `1.2.0` |


### Notes

This package will try to write to a file inside the python environment. 
That specific file needs to be bind so it's writable, create an empty bf_formats.txt file anywhere and bind it. Use it like this:

```bash
singularity exec [...] -B "bf_formats.txt:/env/lib/python3.11/site-packages/valis/data/bf_formats.txt" [...]
```
