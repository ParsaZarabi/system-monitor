# System Monitor

A lightweight system monitoring script that tracks CPU, RAM, and disk
usage and logs alerts when usage exceeds a configurable threshold.

Available in **two versions** — pick whichever fits your stack:

| Version | File | Best for |
|---------|------|----------|
| Bash | `monitor.sh` | Zero dependencies, cron jobs |
| Python | `monitor.py` | Extensibility, containers |

## Python Version

### Requirements

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

Single run (great for cron):
```bash
python3 monitor.py
```

Continuous watch mode (great for Docker):
```bash
python3 monitor.py --watch --interval 300
```

### Threshold Alerting

Any metric above the threshold (default 80%) appends a warning:

```
2026-09-11 18:58:20 - CPU: 6% | RAM: 34% | Disk: 82%  ⚠️ WARNING: usage above threshold!
```

## Automate with Cron (Bash or single-run Python)

```bash
*/5 * * * * /full/path/to/monitor.sh
*/5 * * * * cd /path/to/repo && /path/to/.venv/bin/python3 monitor.py
```

## Docker

> 🚧 Coming soon — see `Dockerfile`

## Author

Parsa Zarabi