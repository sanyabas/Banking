from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=r'http://localhost.*')
api = Api(app)
db = SQLAlchemy(app)
auth = HTTPBasicAuth()
