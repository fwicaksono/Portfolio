from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="db",  # Refers to the service name in docker-compose
        port=5432
    )

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User registered successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
