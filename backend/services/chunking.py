from data_models.chunk import Chunk
from config import CHUNK_SIZE, OVERLAP
import uuid

def create_chunks(document_name: str, text: str) -> dict:

    # Validate Chunk Size and Overlap
    if ((CHUNK_SIZE <= 0) or (OVERLAP <= 0) or (OVERLAP >= CHUNK_SIZE)):
        return {
            "n_chunks": 0,
            "avg_chunk_size": 0,
            "chunks": [],
            "status": "failed",
            "reason": "Invalid value of chunk size or overlap"
        }
    
    chunks = []

    start = 0
    step = CHUNK_SIZE - OVERLAP
    count = 0
    while (start <= len(text)):

        end = start + CHUNK_SIZE
        chunk_text = text[start:end]
        this_chunk = Chunk(
            chunk_id = str(uuid.uuid4()),
            document_name = document_name,
            text = chunk_text,
            start_char = start,
            end_char = end if end<=len(text) else (len(text)-1),
            length = len(chunk_text)
        )

        chunks.append(this_chunk)
        start += step
        count+=1
    
    chunk_report = {
        "n_chunks": count,
        "avg_chunk_size": round((((count-1) * CHUNK_SIZE) + chunks[count-1].length) / count, 2),
        "chunks": chunks,
        "status": "success"
    }

    return chunk_report
