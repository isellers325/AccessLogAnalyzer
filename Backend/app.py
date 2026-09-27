from datetime import datetime, timedelta
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
logs = []
with open("logs.txt") as file:
    for line in file:
        line = line.strip() 
        parts = line.split(",")
        timestamp = datetime.strptime(parts[3], "%Y-%m-%d %H:%M:%S")
        logs.append({"ip": parts[0], "username": parts[1], "status": parts[2], "timestamp": timestamp})
fail_times = {}
for log in logs:
    if log["status"] == "failed":
        ip = log["ip"]
        if ip not in fail_times:
            fail_times[ip] = []
        fail_times[ip].append(log["timestamp"])


@app.route("/api/flagged")
def flagged():
    flagged_ips = {}
    for ip, timestamps in fail_times.items():
        timestamps.sort()
        for i in range(len(timestamps) - 2):
            if timestamps[i + 2] - timestamps[i] <= timedelta(minutes=10):
                flagged_ips[ip] = len(timestamps)
                break

    return jsonify(flagged_ips)

@app.route("/")
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(debug=True)