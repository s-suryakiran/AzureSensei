from fastapi import APIRouter
from models.chatbot import Query
import db.query

router = APIRouter()

@router.post("/query", tags=["query"])
async def query_create(query: Query):
    db.query.create(Query)