import socket

# Take input from user
target = input("Enter target (IP or website): ")

print(f"\n Scanning target: {target}")
print("Scanning in progress...\n")

open_ports = []  # list to store open ports

# Scan ports from 1 to 200
for port in range(1, 201):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    try:
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    except socket.gaierror:
        print("Hostname could not be resolved")
        break

    except socket.error:
        print("Could not connect to server")
        break

    finally:
        s.close()

# Final result summary
print("\nScan Completed!")

if open_ports:
    print(f"Open ports: {open_ports}")
else:
    print("No open ports found in given range")
