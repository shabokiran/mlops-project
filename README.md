# MLOps Monitoring and Deployment Project

## Overview

This project implements an end-to-end MLOps pipeline for data ingestion, model training, model serving, monitoring, and alerting. The system continuously ingests data from an external API, detects data drift, retrains machine learning models, serves predictions through a FastAPI application, and monitors system performance using Prometheus, Grafana, and Alertmanager.

The entire application is containerized using Docker and deployed on AWS EC2.

---

## Project Architecture

Data Source API → Data Ingestion → Drift Detection → Model Training → FastAPI Serving → Prometheus Monitoring → Grafana Dashboards → Alertmanager → Slack Notifications

---

## Features

### Data Ingestion

* Fetches data from external API endpoints.
* Stores raw batches locally.
* Supports automated ingestion workflows.

### Data Validation

* Schema validation checks.
* Missing field detection.
* Feature consistency monitoring.

### Data Drift Detection

* Monitors feature distribution changes.
* Detects drift between historical and incoming batches.
* Supports retraining triggers.

### Model Training

* Uses Scikit-Learn classification models.
* Trains on accumulated batches.
* Saves trained models as artifacts.

### Model Serving

* FastAPI REST API.
* Health endpoint.
* Prediction endpoint.
* Real-time inference.

### Monitoring

* Prometheus metrics exporter.
* Custom ML metrics.
* Request monitoring.
* Latency tracking.
* Accuracy monitoring.

### Visualization

* Grafana dashboards.
* Model accuracy monitoring.
* Request volume tracking.
* Response latency monitoring.
* Data drift indicators.

### Alerting

* Alertmanager integration.
* Slack notifications.
* Automated alert routing.

### Deployment

* Dockerized application.
* AWS EC2 deployment.
* Docker Compose monitoring stack.

---

## Model Performance

### Final Model Accuracy

The trained classification model achieved:

**Accuracy = 90.91%**

Training Output:

```text
Accuracy: 0.9091
```

This accuracy is exported as a Prometheus metric and visualized through Grafana dashboards.

---

## Technology Stack

### Machine Learning

* Python
* Scikit-Learn
* NumPy
* Pandas

### API Layer

* FastAPI
* Uvicorn

### Monitoring

* Prometheus
* Grafana
* Alertmanager

### Deployment

* Docker
* Docker Compose
* AWS EC2

### Version Control

* Git
* GitHub

---

## Project Structure

```text
mlops-project/
│
├── ingestion/
│   ├── ingestion.py
│   ├── drift_detector.py
│   ├── schema_monitor.py
│
├── model/
│   ├── train.py
│   ├── load_data.py
│
├── serving/
│   └── app.py
│
├── exporter/
│   └── metrics.py
│
├── artifacts/
│   ├── model_v1.pkl
│   └── model_v2.pkl
│
├── prometheus/
│   ├── prometheus.yml
│   └── alert_rules.yml
│
├── alertmanager/
│   └── alertmanager.yml
│
├── grafana/
│   └── dashboards/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Prediction Endpoint

```http
POST /predict
```

Request:

```json
{
  "features": [1.0, 2.0]
}
```

Response:

```json
{
  "prediction": 1,
  "confidence": 0.89
}
```

### Metrics Endpoint

```http
GET /metrics
```

Used by Prometheus to scrape monitoring metrics.

---

## Monitoring Metrics

The following metrics are exported:

* model_accuracy
* records_processed_total
* response_delay_seconds
* retrain_total
* data_drift_detected
* datalake_unavailable_total

---

## AWS Deployment

The application is deployed on an AWS EC2 instance and exposed through:

* FastAPI Service
* Prometheus
* Grafana
* Alertmanager

---

## Future Improvements

* Automated CI/CD pipeline
* ECS deployment
* Automated retraining workflow
* Feature store integration
* Model registry support
* Canary deployments
* Advanced drift detection techniques

---

## Author

Shabokiran

MLOps Monitoring and Deployment Project
