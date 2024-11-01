from flask import Flask, Blueprint, request, jsonify, session, redirect
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

signup_blueprint = Blueprint('signup', __name__)

@signup_blueprint.route("/signup/get_users", methods=["GET"])
def getUsers():
    users = User.query.all()
    json_users = list(map(lambda x: x.to_json(), users))
    return jsonify({"users": json_users})

@signup_blueprint.route("/signup/create_user", methods=["POST"])
def createUser():
    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")

    if not username or not password or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        )
    
    hashed_password = generate_password_hash(password)
    
    new_user = User(username, hashed_password, email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Signup successful", "redirect_url": "/"})
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
@signup_blueprint.route("/signup/delete_user/<int:user_id>", methods=["DELETE"])
def deleteUser(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200
