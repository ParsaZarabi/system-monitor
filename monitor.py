import psutil
import time
import argparse
from datetime import datetime
import os


class SystemMonitor:
    """Monitors CPU, RAM, and disk usage with threshold alerting.

    Python rewrite of monitor.sh — keeps the same log format
    so both versions can share the same log file and cron jobs.
    """

    def __init__(self, threshold=80):
        # threshold matches monitor.sh default (80%)
        self.threshold = threshold

    def get_cpu(self):
        """Return CPU usage as a percentage (0-100)."""
        # interval=1 is required: first call without it always returns 0.0
        return psutil.cpu_percent(interval=1)

    def get_ram(self):
        """Return RAM usage as a percentage (0-100)."""
        return psutil.virtual_memory().percent

    def get_disk(self):
        """Return root filesystem usage as a percentage (0-100)."""
        return psutil.disk_usage("/").percent

    def log(self):
        """Check usage, append one line to the log file, and print it.

        Appends a WARNING suffix when any metric crosses the threshold.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu = int(self.get_cpu())
        ram = int(self.get_ram())
        disk = int(self.get_disk())

        # Keep exact same format as monitor.sh (shared contract)
        line = f"{timestamp} - CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%"

        if any(v > self.threshold for v in (cpu, ram, disk)):
            line += "  ⚠️ WARNING: usage above threshold!"

        log_path = os.environ.get("LOG_PATH", "system_monitor.log")

        # append mode ("a") — never overwrite history
        with open(log_path, "a") as f:
            f.write(line + "\n")

        print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Monitor - Python version")
    parser.add_argument(
        "--watch", action="store_true", help="Run continuously (use this inside Docker)"
    )
    parser.add_argument(
        "--interval", type=int, default=300, help="Seconds between checks in watch mode"
    )
    args = parser.parse_args()

    monitor = SystemMonitor()

    if args.watch:
        print(f"🔁 Watching every {args.interval}s (Ctrl+C to stop)")
        while True:
            monitor.log()
            time.sleep(args.interval)
    else:
        # single run — designed for cron compatibility
        monitor.log()
