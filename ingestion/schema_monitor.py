from exporter.metrics import (
    FEATURE_ADDED,
    FEATURE_REMOVED
)


def get_schema(records):

    return {
        "feature_count":
        len(records[0]["features"])
    }


def detect_schema_change(
        old_schema,
        new_schema
):

    if new_schema[
        "feature_count"
    ] > old_schema[
        "feature_count"
    ]:

        FEATURE_ADDED.inc()

        return True

    if new_schema[
        "feature_count"
    ] < old_schema[
        "feature_count"
    ]:

        FEATURE_REMOVED.inc()

        return True

    return False