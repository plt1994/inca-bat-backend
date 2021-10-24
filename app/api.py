from flask import Flask
from flask.blueprints import Blueprint
from flask_restful import Api
from app.views import HealthCheck, Test

app = Flask(__name__)

api_blueprint = Blueprint(
    "API InCA BAT",
    __name__,
)

api = Api(api_blueprint)

api.add_resource(HealthCheck, "/inca-bat")
api.add_resource(Test, "/test")

app.register_blueprint(api_blueprint)
