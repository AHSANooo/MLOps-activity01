#!/usr/bin/env bash
set -e

TARGET_VERSION=${1:-"1.0.0"}
IMAGE_NAME=${2:-"ghcr.io/ahsanooo/mlops-activity01"}

echo "Rolling back container 'mlops-api' to ${IMAGE_NAME}:${TARGET_VERSION}..."

docker pull "${IMAGE_NAME}:${TARGET_VERSION}" || true
docker stop mlops-api || true
docker rm mlops-api || true

docker run -d \
  --name mlops-api \
  --restart unless-stopped \
  -p 5000:5000 \
  "${IMAGE_NAME}:${TARGET_VERSION}"

echo "Rollback completed. Checking health..."
sleep 2
curl -s http://localhost:5000/health | grep "healthy" && echo "Health check passed!"
