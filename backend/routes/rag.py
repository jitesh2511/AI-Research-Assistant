from fastapi import APIRouter, Body

from backend.rag.pipeline import generate_answer

router = APIRouter()

@router.post("/answer")
async def search_query(data: dict = Body(...)):
    query = data['query']
    return generate_answer(query)