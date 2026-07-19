from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


# Validation of PDF Files
def validate_pdf(file: UploadFile, contents) -> dict:

    # Check file extension
    if not file.filename.lower().endswith(".pdf"):
        return {
            "filename": file.filename,
            "size":len(contents),
            "upload_status":"failed",
            "reason":"Only PDF files are allowed"
        }
        
    # Check MIME type
    if file.content_type != "application/pdf":
        return {
            "filename": file.filename,
            "size":len(contents),
            "upload_status":"failed",
            "reason":"Invalid content type"
        }
    
    # Check if file is empty
    if len(contents) == 0:
        return {
            "filename": file.filename,
            "size":len(contents),
            "upload_status":"failed",
            "reason":"File is empty"
        }
    
    return{

    }


# Save file
def save_file(file: UploadFile, contents):

    destination = UPLOAD_DIR / file.filename

    with open(destination, "wb") as f:
        f.write(contents)


# Delete all files
def delete_all_files():

    if UPLOAD_DIR.exists():
        for file in UPLOAD_DIR.glob("*.pdf"):
            file.unlink()