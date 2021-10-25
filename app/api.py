from flask import Flask
from flask.blueprints import Blueprint
from flask_restful import Api
from app.views import HealthCheck, Test, TextToSpeech

app = Flask(__name__, static_folder="../static")

api_blueprint = Blueprint(
    "API InCA BAT",
    __name__,
)

api = Api(api_blueprint)

api.add_resource(HealthCheck, "/inca-bat")
api.add_resource(Test, "/test")
api.add_resource(TextToSpeech, "/text-to-speech")

app.register_blueprint(api_blueprint)
