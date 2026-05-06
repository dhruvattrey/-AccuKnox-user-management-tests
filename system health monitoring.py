import psutil

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("CPU Usage:", cpu)
print("Memory Usage:", memory)
print("Disk Usage:", disk)

if cpu > CPU_THRESHOLD:
    print("⚠ High CPU usage")

if memory > MEM_THRESHOLD:
    print("⚠ High Memory usage")

if disk > DISK_THRESHOLD:
    print("⚠ Disk almost full")