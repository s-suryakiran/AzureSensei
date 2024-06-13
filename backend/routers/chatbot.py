from fastapi import APIRouter
from models.chatbot import Query
import db.query
from openai import AzureOpenAI
import time
import os

router = APIRouter()

@router.post("/query", tags=["query"])
async def query_create(query: Query):
    db.query.create(Query)



openai_client = AzureOpenAI(api_key=os.getenv("AZURE_OPENAI_KEY"), azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), api_version="2024-02-01",)

def generate_embeddings(text):
    '''
    Generate embeddings from string of text.
    This will be used to vectorize data and user input for interactions with Azure OpenAI.
    '''
    response = openai_client.embeddings.create(input=text, model="text-embedding-ada-002")
    embeddings =response.model_dump()
    time.sleep(0.5) 
    return embeddings['data'][0]['embedding']