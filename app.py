from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine


app = Flask(__name__)

# Configurações para o MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'users',                  # Nome do banco de dados
    'host': 'mongodb',              # Host do MongoDB
    'port': 27017,                  # Porta padrão do MongoDB
    'username': 'admin',            # (Opcional) Usuário para autenticação
    'password': 'admin',            # (Opcional) Senha para autenticação
    'authentication_source': 'admin'  # (Opcional) Banco de autenticação
}

api = Api(app)
db = MongoEngine(app)


class Users(Resource):
    def get(self):
        return UserModel.objects()
        # return {'message': 'user 1'}


class UserModel(db.Document):
    cpf = db.StringField(required=True,
                         unique=True)  # Corrigido o erro de digitação
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)  # Corrigido o erro de digitação
    birth_date = db.DateTimeField(required=True)


class User(Resource):
    def post(self):
        return {'message': 'user'}

    def get(self, cpf):
        return {'message': cpf}


# Adiciona as rotas
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
