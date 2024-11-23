from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)


# Configurações para o MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'users',          # Nome do banco de dados
    'host': 'mongodb',            # Host do MongoDB
    'port': 27017,                  # Porta padrão do MongoDB
    'username': 'admin',      # (Opcional) Usuário para autenticação
    'password': '12345',        # (Opcional) Senha para autenticação
    'authentication_source': 'admin'  # (Opcional) Banco de autenticação
}

class Users(Resource):
    def get(self):
        return {'hemessage': 'user 1'}


class User(Resource):
    def post(self):
        return {'message': 'user'}
    
    def get(self, cpf):
        return {'message' : cpf }


                
api.add_resource(Users, '/users')
api.add_resource(User, '/user' , '/user/<string:cpf>')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")