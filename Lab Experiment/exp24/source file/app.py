from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Flask CI/CD with GitHub Actions", status="running")

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify(result=a + b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
