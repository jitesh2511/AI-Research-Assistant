from fastapi import APIRouter
from backend.services.vector_store import vector_store

router = APIRouter()

@router.get("/index_stats")
async def get_stats():
    return vector_store.stats()