# ingestion/drift_detector.py

import numpy as np
from exporter.metrics import (
    DISTRIBUTION_DRIFT_DETECTED
)

def calculate_statistics(records):

    features = np.array([r["features"] for r in records])

    return {
        "mean": np.mean(features, axis=0),
        "std": np.std(features, axis=0)
    }


def detect_drift(
        baseline_stats,
        current_stats,
        threshold=0.5
):

    mean_diff = abs(
        baseline_stats["mean"] -
        current_stats["mean"]
    )

    drift = bool(
        (mean_diff > threshold).any()
    )

    if drift:

        DISTRIBUTION_DRIFT_DETECTED.set(1)

    else:

        DISTRIBUTION_DRIFT_DETECTED.set(0)

    return drift

    mean_diff = np.abs(
        baseline_stats["mean"] -
        current_stats["mean"]
    )

    return bool(np.any(mean_diff > threshold))