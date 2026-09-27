from datetime import datetime, timedelta 


import random

normal_ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40"]
attacker_ips = ["10.0.0.5", "10.0.0.9"]
usernames = ["JaneDoe", "SteveRogers", "BruceBanner", "NatashaRomanoff", "TonyStark"]

base_time = datetime(2026, 9, 27, 9, 0 ,0)

logs = []

for i in range(80):
    ip = random.choice(normal_ips)
    user =random.choice(usernames)
    status = random.choices(["success", "failed"], weights=[90, 10])[0]
    minutes_offset = random.randint(0, 480)
    timestamp = base_time + timedelta(minutes=minutes_offset)
    logs.append(f"{ip},{user},{status},{timestamp}") 

for i in range(20):
    ip = random.choice(attacker_ips)
    user =random.choice(usernames)
    status = random.choices(["success", "failed"], weights=[10, 90])[0]
    seconds_offset = random.randint(0, 300)
    timestamp = base_time + timedelta(hours=2, seconds=seconds_offset)
    logs.append(f"{ip},{user},{status},{timestamp}") 

with open("logs.txt", "w") as file:
    for entry in logs:
        file.write(entry + "\n")
