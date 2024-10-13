from flask import Flask, Blueprint, request, session, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

logout = Blueprint("logout" , __name__)

@logout.route("/api/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    session.pop("username", None)

    return jsonify({"message": "User logout succesfully"}), 200