# MLOps CD Demo

A simple Flask API project for learning Continuous Delivery (CD).

## Setup

1. Create virtual environment and install packages:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

Run pytest:
```bash
pytest
```

## Run App

Start the server:
```bash
python3 app.py
```
App runs at `http://localhost:5000`.

## Endpoints

- `GET /`: Basic service check
- `GET /health`: Health status & version
- `POST /predict`: Sends prediction (`value * 2`)

Test prediction with curl:
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"value": 5}'
```

## Docker

Build image:
```bash
docker build -t mlops-demo .
```

Run container:
```bash
docker run -p 5000:5000 mlops-demo
```

## Deployment (CD)

Push a version tag to trigger deployment:
```bash
git tag v1.0.0
git push origin v1.0.0
```
This runs tests, builds Docker image, and deploys automatically.
