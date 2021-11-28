from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "psql://postgres:postgres@localhost:5432/flask"

db = SQLAlchemy(app)
