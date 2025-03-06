import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Buat instance Flask
app = Flask(__name__)

# Ambil URL dari environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:123456@localhost:5432/registrasi_account')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi SQLAlchemy
db = SQLAlchemy(app)

# Import routes setelah app dan db diinisialisasi
from app import routes
