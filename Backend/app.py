from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
logs = []
with open("logs.txt") as file:
    for line in file:
        line = line.strip() 
        parts = line.split(",")
        logs.append({"ip": parts[0], "username": parts[1], "status": parts[2]})
failcount = {}
for log in logs:
    if log["status"] == "failed":
        ip = log["ip"]
        failcount[ip] = failcount.get(ip, 0) + 1

@app.route("/api/flagged")
def flagged():
    flagged_ips ={}
    for ip, count in failcount.items():
        if count > 2:
            flagged_ips[ip] = count
    return jsonify(flagged_ips)
@app.route("/")
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(debug=True)