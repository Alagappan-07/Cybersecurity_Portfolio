import matplotlib.pyplot as plt

with open("alerts.txt") as f:
    alerts = f.readlines()

types = {"ALERT":0, "CRITICAL":0}
for alert in alerts:
    if "CRITICAL" in alert:
        types["CRITICAL"] +=1
    else:
        types["ALERT"] +=1

plt.bar(types.keys(), types.values())
plt.title("Security Alerts Overview")
plt.savefig("dashboard.png")
plt.show()

