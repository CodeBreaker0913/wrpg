from flask import Flask, Blueprint, request, jsonify, redirect
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

login_blueprint = Blueprint("login", __name__)

@login_blueprint.route("/login", methods=["POST", "GET"])
def login():
    
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "User not found"}), 404
    
    if (check_password_hash(user.password, password)):
        login_user(user)
        return jsonify({"message": "Login successful", "redirect_url": "/"})

    

    
    