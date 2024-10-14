from flask import Flask, Blueprint, request, jsonify, session
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

signup_blueprint = Blueprint('signup', __name__)

@signup_blueprint.route('/api/signup', methods=["POST"])
def signup():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    email = data["email"]
    hashed_password = generate_password_hash(password, "pbkdf2:sha256")

    existing_user = User.query.filter_by(username=username).first()
    existing_email = User.query.filter_by(email=email)

    if existing_user:
        return jsonify({"message": "Username already exists"}), 400
    if existing_email:
        return jsonify({"message": "Email already exists"}), 400
    
    new_user = User(email=email, username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User successfully registered"}), 201