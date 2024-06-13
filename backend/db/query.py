from models.chatbot import Query
import pymongo
import os
import urllib


COSMOS_MONGO_USER = os.getenv("COSMOS_MONGO_USER")
COSMOS_MONGO_PWD = os.getenv("COSMOS_MONGO_PWD")
COSMOS_MONGO_SERVER = os.getenv("COSMOS_MONGO_SERVER")

mongo_conn = "mongodb+srv://"+urllib.parse.quote(COSMOS_MONGO_USER)+":"+urllib.parse.quote(COSMOS_MONGO_PWD)+"@"+COSMOS_MONGO_SERVER
mongo_client = pymongo.MongoClient(mongo_conn)
db = mongo_client['chatbot']

def create(query: Query):
    db['queries'].insert_one(query) 
