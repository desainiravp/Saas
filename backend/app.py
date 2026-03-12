from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(
    host="postgres-service",
    database="saas",
    user="postgres",
    password="postgres",
    port="5432"
)

@app.route("/tasks")
def get_tasks():

    tenant = request.headers.get("tenant")

    cur = conn.cursor()

    cur.execute("""
        SELECT task FROM tasks
        JOIN tenants ON tenants.id = tasks.tenant_id
        WHERE tenants.name=%s
    """, (tenant,))

    rows = cur.fetchall()

    cur.close()

    return jsonify([r[0] for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
