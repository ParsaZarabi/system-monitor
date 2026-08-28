#!/bin/bash

LOG_FILE="$HOME/system_monitor.log"
THRESHOLD=80

DISK_USAGE=$(df -h / | grep / | awk '{print $5}' | sed 's/%//')
MEM_USAGE=$(free | grep Mem | awk '{printf "%.0f", ($3/$2) * 100.0}')
IDLE=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}')
CPU_USAGE=$(echo "100 - $IDLE" | bc)

echo "$(date '+%Y-%m-%d %H:%M:%S') - CPU: ${CPU_USAGE}% | RAM: ${MEM_USAGE}% | Disk: ${DISK_USAGE}%" >> "$LOG_FILE"

if (( $(echo "$DISK_USAGE > $THRESHOLD" | bc -l) )); then 
	echo "$(date '+%Y-%m-%d %H:%M:%S') - ⚠️ WARNING: Disk usage high: ${DISK_USAGE}%" >> "$LOG_FILE"
fi

if (( $(echo "$MEM_USAGE > $THRESHOLD" | bc -l) )); then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ⚠️ WARNING: Memory usage high: ${MEM_USAGE}%" >> "$LOG_FILE"
fi
