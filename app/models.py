from app import app, db, jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def authenticate(self, password):
        if (check_password_hash(self.password_hash, password) == True):
                access_token = create_access_token(identity=self.password_hash)
                refresh_token = create_refresh_token(identity=self.password_hash)
                return (True, {
                    'username': self.username,
                    'access_token': access_token,
                    'refresh_token': refresh_token
                })
        return (False, {})


