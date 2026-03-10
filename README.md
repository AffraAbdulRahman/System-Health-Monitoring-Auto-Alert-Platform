**System Health Monitoring & Auto-Alert Platform**

A lightweight Python-based monitoring tool that tracks system resources such as CPU, memory, and disk usage in real time and generates alerts when usage exceeds defined thresholds.

**Features**

Monitor CPU usage

Monitor memory usage

Monitor disk usage

Threshold-based alert system

Incident logging for monitoring events

Continuous real-time monitoring

**Technologies Used**

Python

psutil library

Python logging module

**Installation**

**Clone the repository**

git clone https://github.com/AffraAbdulRahman/System-Health-Monitoring-Auto-Alert-Platform.git
cd System-Health-Monitoring-Auto-Alert-Platform

****Install required dependencies
****
pip install psutil

**Run the monitoring script**

python monitor.py
Project Structure
system-health-monitor/
│
├── monitor.py      # Main monitoring script
├── config.py       # Threshold configuration
├── system.log      # Log file for alerts
└── README.md

**How It Works**

The script collects system metrics using the psutil library.
It compares CPU, memory, and disk usage values with predefined thresholds.
If any value exceeds the limit, an alert is generated and logged.
The monitoring process runs continuously to simulate basic SRE monitoring practices.

**Example Output**
CPU OK: 35%
Memory OK: 60%
Disk OK: 42%
WARNING: CPU usage high: 88%
