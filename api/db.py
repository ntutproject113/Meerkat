# db.py
from pymongo import MongoClient
import os
from pymongo.server_api import ServerApi
# MongoDB 連線記得先設環境變數MONGO_URI  setx MONGO_URI "網址"
uri = os.getenv("MONGO_URI")  
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['meer']
rents_collection = db['rents']
members_collection = db["users"]
profiles_collection = db["profiles"]  
todo_collection = db["todo"]
counters_collection = db["counters"]
