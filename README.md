# MLOps CD Demo

A simple Flask API project for learning Continuous Delivery (CD) and production traceability.

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
- `GET /health`: Health status, application version, model version & git commit
  ```json
  {
    "application_version": "1.0.0",
    "model_version": "1.0",
    "git_commit": "a1b2c3d",
    "status": "healthy"
  }
  ```
- `POST /predict`: Sends prediction (`value * 2`)

Test prediction with curl:
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"value": 5}'
```

## Workflows

- **CI (`.github/workflows/ci.yml`)**: Runs unit tests automatically on Pull Requests to `main`.
- **CD (`.github/workflows/cd.yml`)**: Triggered when a version tag (e.g. `v1.0.0`) is pushed. Builds Docker image, pushes to GHCR, and deploys.

## Docker

Build image with version and commit metadata:
```bash
docker build --build-arg APP_VERSION=1.0.0 --build-arg GIT_COMMIT=$(git rev-parse --short HEAD) -t mlops-demo .
```

Run container:
```bash
docker run -p 5000:5000 mlops-demo
```

## Rollback

To rollback to a previous version (e.g. `1.0.0`):
```bash
./scripts/rollback.sh 1.0.0
```
