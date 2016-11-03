from flask import Flask, request
from flask_restful import Resource, Api, reqparse

#add comments to check git plugin

app = Flask(__name__)
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        text = "Hello World!"
        return text

api.add_resource(HelloWorld, '/hello/world')

class HelloJimmy(Resource):
    def get(self):
        text = "Hello Jimmy!"
        return text

api.add_resource(HelloJimmy, '/hello/jimmy')

class HelloBozo(Resource):
    def get(self):
        text = "Hello Bozo!"
        return text

api.add_resource(HelloJimmy, '/hello/bozo')

if __name__ == '__main__':
    # Runn Flask
    app.run(debug=True, host='0.0.0.0', port=int("5000"))
    # pass
