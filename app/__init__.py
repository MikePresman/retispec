from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_bootstrap import Bootstrap
import os

def create_app(config_filename):
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(config_filename)

    CORS(app)

    from .models import db, migrate, jwt
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .blueprints.patient_blueprint import patient_blueprint, acquisition_blueprint
    app.register_blueprint(patient_blueprint)
    app.register_blueprint(acquisition_blueprint)

    return app

app = create_app(Config)
