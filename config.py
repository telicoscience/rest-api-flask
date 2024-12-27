import os
from mongomock import MongoClient

class DevConfig:

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'username': os.getenv('MONGODB_USERNAME'),
        'password': os.getenv('MONGODB_PASSWORD')
    }

class ProdConfig: 
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_DB = os.getenv("MONGODB_DB")


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'users',
        'mongo_client_class': MongoClient
           }
    