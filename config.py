class DevConfig():

    MONGODB_SETTINGS = {
        'db': 'users',                  # Nome do banco de dados
        'host': 'mongodb',              # Host do MongoDB
        'port': 27017,                  # Porta padrão do MongoDB
        'username': 'admin',            # (Opcional) Usuário para autenticação
        'password': 'admin',            # (Opcional) Senha para autenticação
        'authentication_source': 'admin'  # (Opcional) Banco de autenticação
    }
