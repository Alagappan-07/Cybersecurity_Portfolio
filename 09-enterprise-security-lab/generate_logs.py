import random
import time
import json

users = ["alice", "bob", "carol", "dave", "eve"]
actions = ["login_success", "login_failed", "file_access", "malware_detected"]

with open("network_logs.json", "w") as f:
    logs = []
    for i in range(1000):
        log = {
            "user": random.choice(users),
            "action": random.choice(actions),
            "ip": f"192.168.1.{random.randint(1,255)}",
            "timestamp": time.time()
        }
        logs.append(log)
    json.dump(logs, f, indent=4)

print("Generated 1000 sample network logs")

