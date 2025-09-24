import csv

ioc_db = {"192.168.1.100": "Known Malware IP", "192.168.1.200": "Phishing IP"}

with open("alerts.txt") as f, open("enriched_alerts.csv", "w", newline='') as out:
    writer = csv.writer(out)
    writer.writerow(["alert","ioc_info"])
    for line in f:
        ip = line.split()[-1]
        info = ioc_db.get(ip, "No match")
        writer.writerow([line.strip(), info])

print("Enriched alerts saved to enriched_alerts.csv")


