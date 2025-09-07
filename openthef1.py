import requests
import json
#Silverstone 2025 meeting key 1277 9947

# sessions = requests.get("https://api.openf1.org/v1/sessions?year=2025").json()
# print(json.dumps(sessions[:10], indent=2))  # Pretty print with 2-space indent

# sessions = requests.get("https://api.openf1.org/v1/sessions?year=2025&location=Silverstone").json()
# print(json.dumps(sessions, indent=2))

position_data = requests.get("https://api.openf1.org/v1/position", params={
    "session_key": 9947,
    "driver_number": 4,
}).json()

print(json.dumps(position_data, indent=2))


lap_data = requests.get("https://api.openf1.org/v1/laps", params={
    "session_key": 9947,
    "driver_number": 4,
    "lap_number": 9
}).json()

print(json.dumps(lap_data, indent=2))

