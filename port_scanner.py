import socket
from concurrent.futures import ThreadPoolExecutor

# Get target input
target = input("Enter target (IP or website): ")

# Convert domain to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname")
    exit()

print(f"\nScanning target: {target} ({target_ip})")

# Get port range
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
    finally:
        s.close()

print("\nScanning in progress...\n")

# Threading (reduced for stability)
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print("\nScan Completed!")

if open_ports:
    print(f"Open ports: {sorted(open_ports)}")
else:
    print("No open ports found")
