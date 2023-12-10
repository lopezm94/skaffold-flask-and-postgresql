import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

username = os.environ.get('DATABASE_USERNAME')
password = os.environ.get('DATABASE_PASSWORD')
database = os.environ.get('DATABASE_NAME')
host = os.environ.get('DATABASE_HOST')
port = os.environ.get('DATABASE_PORT')

SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{host}:{port}/{database}"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from app import routes
