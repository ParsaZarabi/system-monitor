# System Monitor Script

A simple Bash script that monitors CPU, RAM, and Disk usage on Linux systems and logs alerts when usage exceeds a defined threshold.

## Features
- Monitors CPU, RAM, and Disk usage
- Logs results with timestamps
- Sends warnings when usage exceeds 80%
- Can run automatically via cron

## Requirements
- Linux (tested on Ubuntu/Fedora)
- bc (basic calculator)

## Usage
\`\`\`bash
chmod +x monitor.sh
./monitor.sh
\`\`\`

## Automate with Cron
Run every 5 minutes:
\`\`\`bash
*/5 * * * * /full/path/to/monitor.sh
\`\`\`

## Sample Output (log file)
\`\`\`
2026-08-28 14:00:01 - CPU: 12% | RAM: 45% | Disk: 63%
\`\`\`

## Author
[ParsaZarabi]
