import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'note-app-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:123456@localhost/notes_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_APPLICATION_CREDENTIALS = 'gcp-credentials.json'  # Path to your GCP credentials