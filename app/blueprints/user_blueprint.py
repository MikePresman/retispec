from flask import Blueprint, make_response
from app.models import User

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route("/login", methods = ["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    user = User.query.filter_by(username = username).first()

    if (user != None):
        auth, details = user.authenticate(password)
        if (auth != False):
            return details        
    return {'access_token': "null"} 
