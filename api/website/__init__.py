from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_cors import CORS

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SECRET_KEY"] = "osjdoaijdsioajd"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .time import time_blueprint
    from .auth import auth

    app.register_blueprint(time_blueprint)
    app.register_blueprint(auth)

    with app.app_context():
        create_database()

    return app

def create_database():
    if not path.exists("website/" + DB_NAME):
        db.create_all()
        print("Created Database")
    

