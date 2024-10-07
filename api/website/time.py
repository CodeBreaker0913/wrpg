from flask import Flask, Blueprint
from os import path
import time

time_blueprint = Blueprint("time", __name__)

@time_blueprint.route("/time")
def get_current_time():
    return {'time': time.time()}