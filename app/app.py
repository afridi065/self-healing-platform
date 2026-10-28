import os
import sys
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")

@app.route("/")
def home():
    return f"Self-Healing App, version {VERSION}\n"

@app.route("/health")
def health():
    return jsonify(status="healthy", version=VERSION), 200

@app.route("/version")
def version():
    return jsonify(version=VERSION)

@app.route("/crash")
def crash():
    os._exit(1)  # kills the process hard, simulating a real crash

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
