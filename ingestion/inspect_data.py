# ingestion/inspect_data.py

import json
from pathlib import Path

latest = sorted(Path("data/raw").glob("*.json"))[-1]

with open(latest) as f:
    data = json.load(f)

print("Records:", len(data))

print("\nFirst Record:")
print(data[0])

print("\nKeys:")
print(data[0].keys())