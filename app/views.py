from flask_restful import Resource
from app.client import add_test

import json


class HealthCheck(Resource):
    def get(self):
        return "it's alive!"


class Test(Resource):
    def get(self):
        test = add_test()
        return json.loads(test)
