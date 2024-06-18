from models.chatbot import Query
import pymongo
import os
import urllib
import config.var as vars


COSMOS_MONGO_USER = vars.COSMOS_MONGO_USER
COSMOS_MONGO_PWD = vars.COSMOS_MONGO_PWD
COSMOS_MONGO_SERVER = vars.COSMOS_MONGO_SERVER

mongo_conn = (
    "mongodb+srv://"
    + urllib.parse.quote(COSMOS_MONGO_USER)
    + ":"
    + urllib.parse.quote(COSMOS_MONGO_PWD)
    + "@"
    + COSMOS_MONGO_SERVER
)
mongo_client = pymongo.MongoClient(mongo_conn)
db = mongo_client["chatbot"]


def get_azure_collection():
    COLLECTION_NAME = "azure_collection"
    collection = db[COLLECTION_NAME]
    return collection


def create(query: Query):
    db["queries"].insert_one(query)


def response_get(qryID: int):
    db["queries"].find_one()
