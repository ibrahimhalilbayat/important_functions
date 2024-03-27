import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for entry in data:
    timestamp = entry["timestamp"]
    array_data = entry["data"]
    print("Timestamp:", timestamp)
    print("Data:", array_data)