# tests/test_drift_manual.py

from ingestion.drift_detector import (
    calculate_statistics,
    detect_drift
)

baseline = [
    {"features": [1.0, 2.0]},
    {"features": [1.1, 2.1]},
]

shifted = [
    {"features": [10.0, 20.0]},
    {"features": [11.0, 21.0]},
]

baseline_stats = calculate_statistics(baseline)

shifted_stats = calculate_statistics(shifted)

print(
    detect_drift(
        baseline_stats,
        shifted_stats
    )
)