import time

import joblib

from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel

from prometheus_client import generate_latest

from exporter.metrics import (
    MODEL_ACCURACY,
    RESPONSE_DELAY_SECONDS
)

MODEL_PATH = "artifacts/model_v1.pkl"

model = joblib.load(MODEL_PATH)

MODEL_ACCURACY.set(0.9091)

app = FastAPI()


class PredictionRequest(BaseModel):
    features: list[float]

@app.get("/")
def root():
    return {
        "service": "mlops-project",
        "status": "running"
    }

@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.get("/metrics")
def metrics():

    return Response(
        generate_latest(),
        media_type="text/plain"
    )


@app.post("/predict")
def predict(request: PredictionRequest):

    start_time = time.time()

    prediction = model.predict(
        [request.features]
    )[0]

    probability = max(
        model.predict_proba(
            [request.features]
        )[0]
    )

    RESPONSE_DELAY_SECONDS.observe(
        time.time() - start_time
    )

    return {
        "prediction": int(prediction),
        "confidence": float(probability)
    }