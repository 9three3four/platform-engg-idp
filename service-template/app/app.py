from flask import Flask, jsonify
import os

app = Flask(__name__)

ENV = os.getenv("APP_ENV", "unknown")
FEATURE_FLAG = os.getenv("FEATURE_FLAG", "off")

@app.route("/")
def index():
    return jsonify({
        "service": "config-aware-service",
        "environment": ENV,
        "feature_flag": FEATURE_FLAG
    })

@app.route("/health")
def health():
    # simulate a bad config breaking prod
    if FEATURE_FLAG == "break":
        return "unhealthy", 500
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
