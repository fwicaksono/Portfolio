from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Koneksi ke PostgreSQL di Cloud SQL
def get_db_connection():
    return psycopg2.connect(
        dbname="postgres_database",
        user="myuser",
        password="123456",
        host="/cloudsql/learning-gcp-451200:us-central1:my-postgres-instance"
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        return "Connected to PostgreSQL in Cloud SQL!"
    except Exception as e:
        return f"Failed to connect: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
