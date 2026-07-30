from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.health import router as health_router
from .routes.documents import router as document_router
from .routes.index import router as index_router
from .routes.rag import router as rag_router

from logging_config import setup as setup_logging

setup_logging()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# TODO: Update middleware

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app.include_router(health_router)
app.include_router(document_router)
app.include_router(index_router)
app.include_router(rag_router)