import os
from pymongo import MongoClient
import pymongo
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE = False
POSTGRES = True
MONGODB = False

def get_database():
    if SQLITE:
        return {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }

    elif POSTGRES:
        return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('DB_NAME'),
            'USER': env('USER'),
            'PASSWORD': env('PASSWORD'),
            'HOST': env('HOST'),
            'PORT': 5432,
        }

    elif MONGODB:
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/dbName"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        from pymongo import MongoClient
        client = MongoClient(CONNECTION_STRING)

        # database can be created like this.
        return client['users']
