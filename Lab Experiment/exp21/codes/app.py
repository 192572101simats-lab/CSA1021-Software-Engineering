from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
tasks = []          # in-memory list of tasks

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("task", "").strip()
    if title:
        tasks.append({"id": len(tasks) + 1, "title": title, "done": False})
    return redirect(url_for("index"))

@app.route("/done/<int:task_id>")
def done(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))

@app.route("/api/tasks")
def api_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
