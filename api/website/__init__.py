from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    CORS(app)
    login_manager = LoginManager(app)

    app.config["SECRET_KEY"] = "osjdoaijdsioajd"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .time import time_blueprint
    from .signup import signup_blueprint
    from .login import login_blueprint

    app.register_blueprint(time_blueprint)
    app.register_blueprint(signup_blueprint)
    app.register_blueprint(login_blueprint)

    with app.app_context():
        create_database()

    return app

def create_database():
    if not path.exists("website/" + DB_NAME):
        db.create_all()
        print("Created Database")
    

