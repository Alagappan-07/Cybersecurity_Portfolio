import requests
import json

SPLUNK_HEC = "https://splunk-server:8088/services/collector"
SPLUNK_TOKEN = "YOUR_SPLUNK_TOKEN"

def send_alert(event):
    payload = {
        "event": event,
        "sourcetype": "sysmon_alert"
    }
    headers = {
        "Authorization": f"Splunk {SPLUNK_TOKEN}"
    }
    requests.post(SPLUNK_HEC, headers=headers, data=json.dumps(payload))

event = {"host": "WIN10-LAB", "process": "powershell.exe", "user": "TestUser"}
send_alert(event)
print("Alert sent to Splunk")
