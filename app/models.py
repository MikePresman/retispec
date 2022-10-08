from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                set_access_cookies,
                                unset_jwt_cookies)
import datetime
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
db = SQLAlchemy()
migrate = Migrate()
jwt=JWTManager()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    dob = db.Column(db.DateTime)
    sex = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    image_id = db.Column(db.Integer)
    status = db.Column(db.String(64))
