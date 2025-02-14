# Container information

| | |
| :--------------: | :------------- |
|**Name** | AMULET |
| **Description** | Container for running AMULET, count based method for detecting doublets from single nucleus ATAC-seq. |
| **URL/repo** | https://github.com/UcarLab/AMULET |
| **Version(s)** | 1.1 |

## Notes

The version of `AMULET.sh` script in the image does not require a path to the script directory. So you can just run it like this:
```bash
mkdir results
AMULET.sh path/to/dir/atac_fragments.tsv.gz path/to/dir/singlecell.csv human_autosomes.txt GRCh38.bed ./results
```
