from flask_restful import Resource, reqparse
from app.client import add_test, text_to_speech
import json


class HealthCheck(Resource):
    def get(self):
        return "it's alive!"


class Test(Resource):
    def get(self):
        test = add_test()
        return json.loads(test)

class TextToSpeech(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("username")
        args = parser.parse_args()
        text = " ".join(args["text"].split()).lower()
        creator = args["username"]
        length = len(text)
        filename = text_to_speech(text, creator, length)
        if filename:
            return {
                "src": filename
            }
        return 400, "error"
