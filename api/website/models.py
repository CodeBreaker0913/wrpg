from . import db
from flask_login import UserMixin # type: ignore
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
        }