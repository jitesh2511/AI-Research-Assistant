from fastapi import APIRouter

router = APIRouter()

@router.get("/health", status_code=200)
async def health():
    return {
        "status":"heathly",
        "message":"AI Research Assistant backend is running"
    }