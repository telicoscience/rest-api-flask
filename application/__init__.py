from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import User, Users, OlaMundo


def create_app(config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config)
    init_db(app)

    # Adicionar os endpoints de acesso
    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')
    api.add_resource(OlaMundo, '/')
    return app
