# Port Scanner (Python)

## Description
A Python-based port scanner that detects open ports on a target system using TCP connections.  
This project includes multithreading for faster scanning, custom port range selection, and basic service detection.

## Features
- Scans custom port ranges (user-defined)
- Multithreaded scanning for improved speed
- Detects open ports using TCP connection
- Identifies common services (HTTP, SSH, etc.)
- Handles invalid host errors
- Clean and readable output

## How it Works
1. User enters a target (IP address or domain)
2. Domain is converted to IP using DNS resolution
3. User provides a port range (start and end)
4. The scanner attempts TCP connections on each port
5. If connection is successful, the port is marked as open
6. Known services are displayed for common ports

## Technologies Used
- Python
- Socket Programming
- Multithreading (`concurrent.futures`)

## How to Run
```bash
python port_scanner.py
```
## Example Output
<img width="383" height="228" alt="image" src="https://github.com/user-attachments/assets/517681e5-7207-44a7-9227-579f2fd98418" />

## Disclaimer

This project is for educational purposes only.
Do not use it to scan systems without proper authorization.

## Limitations

Fast scans may miss ports due to network delays or firewalls
Service detection is based on common port mapping (not deep inspection)

## Advanced Features

- Multithreading for faster scanning
- Adjustable timeout for better accuracy
- Customizable port range
- Basic service identification

## Future Improvements

- Banner grabbing (detect service versions)
- Save scan results to a file
- GUI-based interface
- OS detection
---
## Author

Made with ❤️ by LashminiAD
