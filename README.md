# Access Log Analyzer

A full-stack brute-force login detection tool. A Python/Flask backend parses login log data and flags IP addresses exceeding a failed-login threshold; a JavaScript frontend fetches and displays the results in real time.

## Features

- Parses raw login attempt logs (IP, username, status, timestamp) from a text file
- Includes a synthetic data generator (`generate_logs.py`) that creates realistic normal traffic and simulated brute-force attack bursts using randomized, weighted data
- Flags IPs with 3+ failed login attempts within a 10-minute window, using time-based burst detection rather than simple lifetime counts — closer to real-world brute-force detection
- Exposes flagged results through a REST API endpoint (`/api/flagged`)
- Frontend dynamically fetches and renders flagged IPs with no page reload
- Basketball-arena-themed UI with a "BLOCKED 🏀" stamp effect on flagged entries



## Tech Stack

**Backend:** Python, Flask, flask-cors
**Frontend:** HTML, CSS, JavaScript (vanilla, using `fetch()` for async requests)

## Project Structure

AccessLogAnalyzer/
├── Index.html # Frontend structure
├── Style.css # Styling
├── Script1.js # Frontend logic (fetches from the API)
├── README.md
├── .gitignore
└── Backend/
├── app.py # Flask server, log parsing, and time-window detection
├── generate_logs.py # Synthetic log data generator
└── logs.txt # Generated log data (ip,user,status,timestamp per line)


## How It Works

1. `generate_logs.py` creates a realistic mix of normal and attacker traffic, writing it to `logs.txt`
2. `app.py` reads `logs.txt` and parses each line into a structured record, including a timestamp
3. For each IP, it groups all failed-login timestamps together
4. Any IP with 3+ failures occurring within a 10-minute window is flagged as a likely brute-force attempt
5. The `/api/flagged` route serves these flagged IPs as JSON
6. The frontend calls this API on page load and displays the results

## Running Locally

**Backend:**
```bash
cd Backend
pip install flask flask-cors
python app.py
```
Server runs at `http://127.0.0.1:5000`

**Frontend:**
Open `Index.html` in your browser (or use the VS Code Live Server extension). Make sure the Flask server is running first.

## Future Improvements

- Adjustable failure threshold and time window (currently hardcoded at 3 failures / 10 minutes)
- Persistent storage (database instead of a flat file)
- A route returning all logs, not just flagged results, for full activity review
