from app import app, db
from config import Config
from app.models import User

from flask import render_template, redirect, flash, url_for, request, session, jsonify
from flask_login import current_user, login_user, logout_user, login_required

from werkzeug.security import generate_password_hash, check_password_hash

#dummy account: username a, password a

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
    if (User.query.filter_by(username = username).first() != None):
        u = User.query.filter_by(username = username).first()
        if (check_password_hash(u.password_hash, password) == True):
            login_user(u)
            return {'Login': 'Success'}  

        
    return {"GotIt": True}

@app.route("/hello")
def hello():
    return {"Hello": 1, "Time": "Now"}
