from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
api = Api(app)
db = SQLAlchemy(app)
auth=HTTPBasicAuth()
