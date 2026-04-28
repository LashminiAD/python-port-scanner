import socket
from concurrent.futures import ThreadPoolExecutor #concurrent.futures → module for running tasks simultaneously ,   ThreadPoolExecutor  → tool to run multiple scans at the same time

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

target = input("Enter target (IP or website): ")

try:
    target_ip = socket.gethostbyname(target) # Convert domain to IP
except socket.gaierror: # error if invalid website
    print("Invalid hostname")
    exit()

print(f"\nScanning target: {target} ({target_ip})")

# Port range
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)   # increased for accuracy

    try:
        result = s.connect_ex((target_ip, port))
        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"Port {port} is OPEN ({service})")
            open_ports.append(port)
    finally:
        s.close()

print("\nScanning in progress...\n")

# Balanced threading
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print("\nScan Completed!")

if open_ports:
    print(f"Open ports: {sorted(open_ports)}")
else:
    print("No open ports found")
