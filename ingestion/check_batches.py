# ingestion/check_batches.py

import json
from pathlib import Path

files = sorted(
    Path("data/raw").glob("*.json")
)

for file in files:

    with open(file) as f:
        data = json.load(f)

    feature_count = len(
        data[0]["features"]
    )

    print(
        file.name,
        feature_count
    )