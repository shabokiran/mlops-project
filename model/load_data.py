# model/load_data.py

import json
from pathlib import Path

import pandas as pd


def load_all_batches():

    rows = []

    files = sorted(
        Path("data/raw").glob("*.json")
    )

    for file in files:

        with open(file) as f:

            batch = json.load(f)

            rows.extend(batch)

    X = []
    y = []

    for row in rows:

        X.append(row["features"])
        y.append(row["label"])

    return pd.DataFrame(X), pd.Series(y)