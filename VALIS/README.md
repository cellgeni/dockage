# Container information

| | |
| :--------------: | :------------- |
|**Name** | VALIS |
| **Description** | Virtual Alignment of pathoLogy Image Series | 
| **URL/repo** | https://github.com/MathOnco/valis |
| **URL/container** |  |
| **Version(s)** | `1.2.0` |
| **Notes** | This package will try to write to a file inside the python environment. That specific file needs to be bind so it's writable. Use:
```bash
singularity exec [...] -B "bf_formats.txt:/env/lib/python3.10/site-packages/valis/data/bf_formats.txt" [...]
``` |
