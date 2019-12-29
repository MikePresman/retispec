from app import app, db
from config import Config
from app.models import User

from flask import render_template, redirect, flash, url_for, request, session
from flask_login import current_user, login_user, logout_user, login_required


@app.route("/", methods=["GET"])
def index():
    user = User.query.all()
    return render_template("index.html", user = user)


@app.route("/bad", methods = ["GET", "POST"])
def bad():
    return render_template("bad.html")
    