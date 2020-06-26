from pymongo import MongoClient
from vacancy_parse.settings import BOT_NAME

CLIENT_DB = MongoClient('mongodb://localhost:27017')[BOT_NAME]