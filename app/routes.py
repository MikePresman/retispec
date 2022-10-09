from app import app, db, jwt
from flask_jwt_extended import get_jwt
from config import Config


from flask import render_template, redirect, flash, url_for, request, session, jsonify, make_response
from flask_login import current_user, login_user, logout_user, login_required
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    print("hello")
    return 'hello world'

