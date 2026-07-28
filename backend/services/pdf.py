from config import UPLOAD_DIR
from fastapi import UploadFile
from data_models.models import PageInfo
import fitz
import logging

logger = logging.getLogger(__name__)

UPLOAD_DIR.mkdir(exist_ok=True)


# Validation of PDF Files
def validate_pdf(file: UploadFile, contents) -> dict:

    # Check file extension
    if not file.filename.lower().endswith(".pdf"):
        logger.error("invalid file extension")
        return {
            "filename": file.filename,
            "size":len(contents),
            "upload_status":"failed",
            "reason":"Only PDF files are allowed"
        }
        
    # Check MIME type
    if file.content_type != "application/pdf":
        logger.error("invalid file content type")
        return {
            "filename": file.filename,
            "size":len(contents),
            "upload_status":"failed",
            "reason":"Invalid content type"
        }
    
    # Check if file is empty
    if len(contents) == 0:
        logger.error("empty file uploaded")
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
    
    logger.info(f"successfully saved \"{file.filename}\"")


# Delete all files
def delete_all_files():

    if UPLOAD_DIR.exists():
        for file in UPLOAD_DIR.glob("*.pdf"):
            file.unlink()
    
    logger.info("deleted all files at cleanup")
        

# Extract text from one PDF at a time
def extract_text(filename: str):

    text = ""
    offset = 0
    page_info = []
    pages = 0
    pdf_path = UPLOAD_DIR / filename

    with fitz.open(pdf_path) as pdf:
        pages = pdf.page_count
        for page_number, page in enumerate(pdf, start=1):
            
            page_text = page.get_text()

            start = offset
            text += page_text
            offset += len(page_text)
            end = offset

            page_info.append(
                PageInfo(
                    page_number = page_number,
                    start_char = start,
                    end_char = end
                ))

    report = {
        "pages": pages,
        "page_info": page_info,
        "text":text,
        "status":"success"
    }
    logger.info(f"extracted text from \"{filename}\" successfully")
    return report