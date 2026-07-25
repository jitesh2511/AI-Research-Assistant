from fastapi import APIRouter, Body

from backend.services.retrieval import search_query as search

router = APIRouter()

@router.post("/search")
async def search_query(data: dict = Body(...)):
    query = data['query']
    return search(query)