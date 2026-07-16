from .util import validate_pdf
from pathlib import Path

from typing import List
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/health", status_code=200)
async def health():
    return {
        "status":"heathly",
        "message":"AI Research Assistant backend is running"
    }

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):

    uploaded_files = []

    for file in files:

        # Validation
        
        # Read file contents
        contents = await file.read()

        valid_dict = validate_pdf(file, contents)
        
        if valid_dict:
            uploaded_files.append(valid_dict)
            continue


        # Save file
        destination = UPLOAD_DIR / file.filename

        with open(destination, "wb") as f:
            f.write(contents)
        
        # Metadata

        uploaded_files.append({
            "filename": file.filename,
            "size": len(contents),
            "content_type": file.content_type,
            "upload_status":"success"
        })

    return {
        "files": uploaded_files
    }

@app.post("/cleanup")
async def cleanup():
    deleted = []

    if UPLOAD_DIR.exists():
        for file in UPLOAD_DIR.glob("*.pdf"):
            file.unlink()
            deleted.append(file.name)
        
    return{
        "deleted_files":deleted
    }