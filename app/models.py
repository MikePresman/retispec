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
from . import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    date_of_birth = db.Column(db.String(64))
    sex = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    image_id = db.Column(db.Integer)
    status = db.Column(db.String(64))

    def populate_obj(obj):
        super().populate_obj(obj)


class Acquisition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eye = db.Column(db.String(64))
    site_name = db.Column(db.String(64))
    date_taken = db.Column(db.String(64))
    operator_name = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    image_data = db.Column(db.LargeBinary)

