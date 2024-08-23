import platform
import os
# Display the operating system name
#os_name = os.name

os_name = platform.system()
os_version = platform.version()
os_release = platform.release()
machine_type = platform.machine()
network_name = platform.node()
processor_name = platform.processor()
uname = platform.uname()


print(f"Operating System (os.name): {os_name}")
print(f"Operating Version (os_version): {os_version}")
print(f"Operating Version (os_release): {os_release}")
print(f"Machine Type (os_type): {machine_type}")
print(f"Mode network name (network_name) : {network_name}")
print(f"processor name (processor_name): {processor_name}")
## "uname" containing six attributes: system, node, release, version, machine, and processor.
print(f"system info (uname): {uname}")
