# model/train.py

from pathlib import Path

import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from model.load_data import load_all_batches


TARGET_ACCURACY = 0.80

MODEL_DIR = Path("artifacts")
MODEL_DIR.mkdir(exist_ok=True)


def get_next_version():

    models = list(
        MODEL_DIR.glob("model_v*.pkl")
    )

    if not models:
        return 1

    versions = []

    for model in models:

        version = int(
            model.stem.split("_v")[1]
        )

        versions.append(version)

    return max(versions) + 1


def train():

    X, y = load_all_batches()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"Accuracy: {accuracy:.4f}")

    version = get_next_version()

    model_path = (
        MODEL_DIR /
        f"model_v{version}.pkl"
    )

    joblib.dump(
        model,
        model_path
    )

    print(
        f"Saved {model_path}"
    )

    if accuracy < TARGET_ACCURACY:

        print(
            "WARNING: Accuracy below threshold"
        )

    return accuracy


if __name__ == "__main__":
    train()