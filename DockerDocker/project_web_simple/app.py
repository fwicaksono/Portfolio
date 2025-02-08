import os
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2 import sql


app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'app/templates'))

# Koneksi ke PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(        
        dbname="database_user", 
        user="postgres", 
        password="123456", 
        host="db",  # Ganti localhost dengan db
        port="5432"
    )
    return conn

# Membuat database jika belum ada
def create_database():
    conn = psycopg2.connect(
        dbname="database_user", 
        user="postgres", 
        password="123456", 
        host="db",  # Change localhost to db
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Create the database if it doesn't exist
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'database_user'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("CREATE DATABASE database_user")
    
    # Create users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    )
    """)
    cursor.close()
    conn.close()

# Halaman Landing
@app.route('/')
def home():
    return render_template('index.html')

# Halaman Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

# Halaman Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return f'Login Successful, Welcome {username}!'
        else:
            return 'Invalid Credentials'
    return render_template('login.html')

if __name__ == "__main__":
    create_database()  # Memastikan database ada
    app.run(debug=True, host='0.0.0.0')
