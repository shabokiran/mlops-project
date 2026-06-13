# exporter/metrics.py

from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Histogram


MODEL_ACCURACY = Gauge(
    "model_accuracy",
    "Current model accuracy"
)

RECORDS_PROCESSED_TOTAL = Counter(
    "records_processed_total",
    "Records processed"
)

RETRAIN_COUNT_TOTAL = Counter(
    "retrain_count_total",
    "Number of retrains"
)

DISTRIBUTION_DRIFT_DETECTED = Gauge(
    "distribution_drift_detected",
    "Drift detected"
)

FEATURE_ADDED = Counter(
    "feature_added",
    "Features added"
)

FEATURE_REMOVED = Counter(
    "feature_removed",
    "Features removed"
)

DATALAKE_UNAVAILABLE = Counter(
    "datalake_unavailable",
    "503 responses"
)

RESPONSE_DELAY_SECONDS = Histogram(
    "response_delay_seconds",
    "Prediction latency"
)