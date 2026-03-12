from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {
    "tenant1": ["Deploy Kubernetes", "Setup CI/CD"],
    "tenant2": ["Build SaaS app"]
}

@app.route("/tasks")
def get_tasks():
    tenant = request.headers.get("tenant")

    if tenant in tasks:
        return jsonify(tasks[tenant])

    return jsonify([])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
