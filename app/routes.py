
from app import app, db, jwt
from flask_jwt_extended import get_jwt
from config import Config
from app.models import User

from flask import render_template, redirect, flash, url_for, request, session, jsonify, make_response
from flask_login import current_user, login_user, logout_user, login_required
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods = ["POST"])
def register():
    username = request.json["username"]
    password = request.json["password"]

    if (User.query.filter_by(username = username).first() == None):
        hashed_pword = generate_password_hash(password)
        user = User(username = username, password_hash = hashed_pword)
        db.session.add(user)
        db.session.commit()
        return {'Success': True}
    return {'Success': False}


@app.route("/login", methods = ["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    user = User.query.filter_by(username = username).first()

    if (user != None):
        auth, details = user.authenticate(password)
        if (auth != False):
            return details        
    return {'access_token': "null"} 



@app.route("/hello")
def hello():
    return {"Hello": 1, "Time": "Now"}


@app.route('/getkey', methods = ["POST"])
@jwt_required()
def protected():
    claims = get_jwt_identity()
    print(claims)
    return {"ok": 1}