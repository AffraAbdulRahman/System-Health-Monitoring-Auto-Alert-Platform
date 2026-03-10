import psutil
import time
import logging
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, CHECK_INTERVAL

# Logging configuration
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert = f"CPU usage high: {cpu_usage}%"
        print(alert)
        logging.warning(alert)
    else:
        logging.info(f"CPU OK: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert = f"Memory usage high: {memory_usage}%"
        print(alert)
        logging.warning(alert)
    else:
        logging.info(f"Memory OK: {memory_usage}%")

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        alert = f"Disk usage high: {disk_usage}%"
        print(alert)
        logging.warning(alert)
    else:
        logging.info(f"Disk OK: {disk_usage}%")

def monitor_system():
    print("🚀 System Monitoring Started...")
    logging.info("System monitoring started")

    while True:
        check_cpu()
        check_memory()
        check_disk()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_system()
