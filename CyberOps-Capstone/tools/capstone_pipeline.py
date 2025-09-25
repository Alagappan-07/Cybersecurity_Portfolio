from subprocess import run

print("[*] Running automated SOC detection")
run(["python3", "../Blue-Sentinel-SOC/tools/detect_powershell_alert.py"])

print("[*] Running vulnerability scan")
run(["python3", "../VulnRadar/tools/vuln_scan.py"])

print("[*] Running cloud IAM check")
run(["python3", "../CloudLock-Sentinel/lambda/iam_checker.py"])
