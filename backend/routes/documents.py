from fastapi import APIRouter, UploadFile, File
from typing import List

from backend.services.pdf import validate_pdf, save_file, delete_all_files, extract_text
from backend.services.chunking import create_chunks
from backend.services.embeddings import generate_embeddings
from backend.services.vector_store import vectorStore

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
                "chunks":""
            })
            continue


        # Save file
        save_file(file, contents)

        # Extract text
        text_report = extract_text(file.filename)

        # Create chunks
        chunk_report = create_chunks(file.filename, text_report['page_info'], text_report['text'])

        # Generate Embeddings
        embedding_report = generate_embeddings(chunk_report['chunks'])

        # Add Embeddings to FAISS Index
        vectorStore.add_chunks(chunk_report["chunks"])
        
        # Metadata
        meta = {
            "filename": file.filename,
            "size": len(contents),
            "pages": text_report['pages'],
            "content_type": file.content_type,
            "upload_status":"success",
            "text_extraction_status": text_report["status"],
            "n_chunks": chunk_report["n_chunks"],
            "avg_chunk_size": chunk_report["avg_chunk_size"],
            "chunking_status": chunk_report["status"],
            "n_embeddings": embedding_report["n_embeddings"],
            "embedding_status": embedding_report["embedding_status"]
        }

        uploaded_files.append({
            "meta":meta,
            "chunks": chunk_report["chunks"]
        })

    return {
        "files": uploaded_files
    }

@router.post("/cleanup")
async def cleanup():

    delete_all_files()