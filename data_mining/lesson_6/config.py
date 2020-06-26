from pymongo import MongoClient
from leroymerlin.settings import BOT_NAME

CLIENT_DB = MongoClient('mongodb://localhost:27017')[BOT_NAME]
