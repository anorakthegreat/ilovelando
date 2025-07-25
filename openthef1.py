import requests
import json

# sessions = requests.get("https://api.openf1.org/v1/sessions?year=2025").json()
# print(json.dumps(sessions[:10], indent=2))  # Pretty print with 2-space indent

sessions = requests.get("https://api.openf1.org/v1/sessions?year=2024&location=Sakhir").json()
# print(json.dumps(sessions, indent=2))

position_data = requests.get("https://api.openf1.org/v1/laps", params={
    "session_key": 9462,
    "driver_number": 1,
    "lap_number": 8
}).json()

print(json.dumps(position_data, indent=2))

