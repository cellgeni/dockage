# Container information

| | |
| :--------------: | :------------- |
|**Name** | BIABench |
| **Description** | Benchmark for AI agents on bioimage-analysis tasks |
| **URL/repo** | https://github.com/BIABench/BIABench |
| **URL/container** |  |
| **Version(s)** | commit `007c974` |
| **Status** | :white_check_mark: Built and tested 2026-10-29 (tool check OK, jupyter OK; image 0.8GB) |

## Notes

* Harness and evaluators only. The ~27 GB task data, agent CLIs (claude, codex, Fiji agents) and API keys are not included.

## Usage

```bash
docker build -t biabench:latest .
singularity build biabench.sif docker-daemon://biabench:latest

# smoke test
singularity exec biabench.sif bash -c 'bioimage-bench --help'
```
