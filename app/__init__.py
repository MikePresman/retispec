from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
import os


app = Flask(__name__)

CORS(app)

app.config.from_object(Config) #this inherits the Config class, makes the Flask config be overwritten by this

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)



from app import routes, models

