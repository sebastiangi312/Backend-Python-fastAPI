from pymongo import MongoClient
from config import Config

db_config = Config()
client = MongoClient(db_config.CONNECTION_STR)
db = client[db_config.DB]
collection = db[db_config.DB_COLLECTION]


def add(data):
    collection.insert_many(data)
