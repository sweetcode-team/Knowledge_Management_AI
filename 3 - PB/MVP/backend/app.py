from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "<h1>Knowledge Management AI</h1>"