import subprocess

targets = ['192.168.1.10', '192.168.1.15']

for target in targets:
    print(f"[*] Running nmap vuln scan on {target}")
    subprocess.run(['nmap', '-sV', '--script=vuln', target])
