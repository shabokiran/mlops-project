import json
import requests

from datetime import datetime
from pathlib import Path

from exporter.metrics import (
    RECORDS_PROCESSED_TOTAL,
    DATALAKE_UNAVAILABLE
)

API_URL = "http://149.40.228.124:6500/records"

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def fetch_records():

    try:

        response = requests.get(
            API_URL,
            timeout=10
        )

        if response.status_code == 503:

            DATALAKE_UNAVAILABLE.inc()

            print("API unavailable")

            return None

        response.raise_for_status()

        data = response.json()

        RECORDS_PROCESSED_TOTAL.inc(
            len(data)
        )

        return data

    except Exception as e:

        print(f"Error: {e}")

        return None


def save_batch(records):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        DATA_DIR /
        f"batch_{timestamp}.json"
    )

    with open(filename, "w") as f:

        json.dump(records, f)

    print(
        f"Saved {filename}"
    )


def main():

    records = fetch_records()

    if records:

        save_batch(records)


if __name__ == "__main__":
    main()