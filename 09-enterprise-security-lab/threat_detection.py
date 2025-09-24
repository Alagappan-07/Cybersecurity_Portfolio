import json

with open("network_logs.json") as f:
    logs = json.load(f)

alerts = []

for log in logs:
    if log["action"] == "login_failed":
        alerts.append(f"ALERT: Failed login by {log['user']} from {log['ip']}")
    elif log["action"] == "malware_detected":
        alerts.append(f"CRITICAL: Malware detected by {log['user']} from {log['ip']}")

with open("alerts.txt", "w") as f:
    for alert in alerts:
        f.write(alert + "\n")

print(f"{len(alerts)} alerts generated and saved to alerts.txt")

