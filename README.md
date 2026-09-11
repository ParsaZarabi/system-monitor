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

The container runs `monitor.py` in watch mode (no cron needed inside).

### Build

```bash
docker build -t system-monitor:1.1 .
```

### Run

```bash
docker run -d --name monitor system-monitor:1.1
```

### View logs

```bash
docker logs -f monitor
```

### Quick test (fast interval)

```bash
docker run --rm system-monitor:1.1 python -u monitor.py --watch --interval 5
```

### Design notes

- **`python:3.12-slim`** base image — smaller attack surface & faster pulls
- **`PYTHONUNBUFFERED=1`** — without it `docker logs` stays empty because
  Python block-buffers stdout when it's not a TTY
- **`requirements.txt` copied before code** — leverages layer caching,
  so pip install is skipped when only `monitor.py` changes
- **`.dockerignore`** — keeps `.venv/` and log files out of the image
- **Timestamps are UTC** inside containers (standard for logging —
  convert to local time in the display layer)
## Author

Parsa Zarabi