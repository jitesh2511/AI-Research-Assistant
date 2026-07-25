from fastapi import APIRouter
from backend.services.vector_store import vectorStore

router = APIRouter()

@router.get("/index_stats")
async def get_stats():
    return vectorStore.stats()