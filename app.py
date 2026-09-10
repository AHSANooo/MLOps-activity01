import os
import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)

MODEL_VERSION = "1.0"


def get_app_version():
    if os.getenv("APP_VERSION"):
        return os.getenv("APP_VERSION")
    version_file = os.path.join(os.path.dirname(__file__), "VERSION")
    if os.path.exists(version_file):
        try:
            with open(version_file, "r") as f:
                return f.read().strip()
        except Exception:
            pass
    return "1.0.0"


def get_git_commit():
    if os.getenv("GIT_COMMIT"):
        return os.getenv("GIT_COMMIT")
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
        if commit:
            return commit
    except Exception:
        pass
    return "unknown"


@app.route("/")
def home():
    return jsonify({
        "service": "mlops-demo",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "application_version": get_app_version(),
        "model_version": MODEL_VERSION,
        "git_commit": get_git_commit(),
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    value = float(data["value"])
    # Dummy ML prediction for teaching
    prediction = value * 2
    return jsonify({
        "input": value,
        "prediction": prediction,
        "model_version": MODEL_VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)