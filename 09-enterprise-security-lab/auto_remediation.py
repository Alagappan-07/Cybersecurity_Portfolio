with open("alerts.txt") as f:
    alerts = f.readlines()

for alert in alerts:
    if "CRITICAL" in alert:
        print(f"Remediation triggered for: {alert.strip()}")
    elif "ALERT" in alert:
        print(f"Monitoring user activity: {alert.strip()}")

