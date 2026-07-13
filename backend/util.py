from fastapi import UploadFile

# Validation of PDF Files
def validate_pdf(file: UploadFile, contents) -> dict:

    # Check file extension
    if not file.filename.lower().endswith(".pdf"):
        return {
            "filename": file.filename,
            "upload_status":"failed",
            "reason":"Only PDF files are allowed"
        }
        
    # Check MIME type
    if file.content_type != "application/pdf":
        return {
            "filename": file.filename,
            "upload_status":"failed",
            "reason":"Invalid content type"
        }
    
    # Check if file is empty
    if len(contents) == 0:
        return {
            "filename": file.filename,
            "upload_status":"failed",
            "reason":"File is empty"
        }
    
    return{

    }