from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Arun",  "dept": "CSE"},
    {"id": 2, "name": "Divya", "dept": "IT"},
]

@app.route("/")
def home():
    return jsonify(message="Hello from Flask API on Kubernetes")

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json()
    data["id"] = len(students) + 1
    students.append(data)
    return jsonify(data), 201

@app.route("/health")
def health():
    return jsonify(status="UP")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
