from data_models.models import Chunk, PageInfo
from config import CHUNK_SIZE, OVERLAP
import uuid
import logging

logger = logging.getLogger(__name__)

def create_chunks(document_name: str, page_info: list[PageInfo], text: str) -> dict:

    # Validate Chunk Size and Overlap
    if ((CHUNK_SIZE <= 0) or (OVERLAP <= 0) or (OVERLAP >= CHUNK_SIZE)):
        logger.warning("invalid chunk size or overlap size")
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
    
    assign_pages(chunks, page_info)

    chunk_report = {
        "n_chunks": count,
        "avg_chunk_size": round((((count-1) * CHUNK_SIZE) + chunks[count-1].length) / count, 2),
        "chunks": chunks,
        "status": "success"
    }
    
    logger.info(f"created {count} chunks for file \"{document_name}\"")

    return chunk_report


def assign_pages(chunks: list[Chunk], page_info: list[PageInfo]):

    page_index = 0

    for chunk in chunks:
        
        chunk.pages = []

        while page_index < len(page_info):
            
            page = page_info[page_index]

            if page.start_char < chunk.end_char and page.end_char > chunk.start_char:
                chunk.pages.append(page.page_number)

            if chunk.end_char <= page.end_char:
                break

            page_index += 1
