from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    # Create the Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Create database tables within the app context
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        from . import models

        # Import routes to ensure they are registered with the Flask app
        from . import routes

        # Register routes with the app
        app.register_blueprint(routes.bp)

        # Create all database tables
        db.create_all()

    return app