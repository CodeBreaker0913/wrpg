from flask import Flask, Blueprint, request, session, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

login_blueprint = Blueprint("login", __name__)

@login_blueprint.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        session["user_id"] = user.id
        session["username"] = user.username
        
        return jsonify({"message": "Login successful", "username": user.username}), 200
    else:
        return jsonify({"message": "Either your Username or Password is incorrect."})
    