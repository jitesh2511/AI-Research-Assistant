from config import UPLOAD_DIR
from fastapi import UploadFile
import fitz

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
        

# Extract text from one PDF at a time
def extract_text(filename: str):

    text = ""
    pages = 0
    pdf_path = UPLOAD_DIR / filename
    with fitz.open(pdf_path) as pdf:
        pages = pdf.page_count
        for page in pdf:
            text += page.get_text()

    report = {
        "pages": pages,
        "text":text,
        "status":"success"
    }
        
    return report