from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from typing import List

from backend.services.pdf import validate_pdf, save_file, delete_all_files

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

router = APIRouter()

@router.post("/upload")
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
        save_file(file, contents)
        
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

@router.post("/cleanup")
async def cleanup():

    delete_all_files()