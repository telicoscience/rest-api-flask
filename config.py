import os
from mongomock import MongoClient


class ProdConfig:
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_DB = os.getenv("MONGODB_DB")
    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://%s:%s@%s/%s?retryWrites=true&w=majority&appName=Cluster0'% 
           (MONGODB_USERNAME, 
           MONGODB_PASSWORD, 
           MONGODB_HOST, 
           MONGODB_DB)
           }

class DevConfig:
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_DB = os.getenv("MONGODB_DB")


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'users',
        'mongo_client_class': MongoClient
           }
