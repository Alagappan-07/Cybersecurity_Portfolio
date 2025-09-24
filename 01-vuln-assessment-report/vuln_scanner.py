import socket

target = '127.0.0.1'
ports = range(20, 1025)

print(f"Scanning {target}...")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    s.close()

print("Scan complete.")




