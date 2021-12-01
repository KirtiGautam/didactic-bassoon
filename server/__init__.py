from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        # Initialize Global db
        db.create_all()

        return app
