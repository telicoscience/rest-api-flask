from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from datetime import datetime
import re

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

# Parser para entrada de dados
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                           type=str,
                           required=True,
                           help='This field cannot be blank')
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help='This field cannot be blank')
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help='This field cannot be blank')
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help='This field cannot be blank')
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help='This field cannot be blank')

# Modelo de usuário


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())


# Rota para gerenciar usuários
class User(Resource):
    def validate_cpf(self, cpf):
        # Has the correct mask?
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            return False
        # Grab only numbers
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Does it have 11 digits?
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validate first digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9],
                                                  range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validate second digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10],
                                                  range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def post(self):
        data = _user_parser.parse_args()

        if not self.validate_cpf(data["cpf"]):
            return {"message": "CPF is invalid!"}, 400

        # Converter birth_date para datetime
        try:
            data['birth_date'] = datetime.strptime(data['birth_date'],
                                                   '%Y-%m-%d')
        except ValueError:
            return {'message':
                    'Invalid birth_date format. Use YYYY-MM-DD.'}, 400

        try:
            # Criar e salvar o usuário
            user = UserModel(**data)
            user.save()
            return {'message': 'User %s created successfully.' % user.id}, 201
        except Exception as e:
            return {'message': str(e)}, 500

    def get(self, cpf):
        user = UserModel.objects(cpf=cpf).first()
        if user:
            return jsonify(user)
        return {'message': 'User not found'}, 404


# Adicionar as rotas
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
