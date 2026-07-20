from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from typing import List

from backend.services.pdf import validate_pdf, save_file, delete_all_files, extract_text

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
            uploaded_files.append({
                "meta": valid_dict,
                "text":""
            })
            continue


        # Save file
        save_file(file, contents)

        # Extract text
        text_report = extract_text(file.filename)
        
        # Metadata
        meta = {
            "filename": file.filename,
            "size": len(contents),
            "pages": text_report['pages'],
            "content_type": file.content_type,
            "upload_status":"success",
            "text_extraction_status": text_report["status"]
        }

        uploaded_files.append({
            "meta":meta,
            "text": text_report['text']
        })

    return {
        "files": uploaded_files
    }

@router.post("/cleanup")
async def cleanup():

    delete_all_files()