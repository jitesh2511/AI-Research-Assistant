from pydantic import BaseModel

class Chunk(BaseModel):
    chunk_id: str
    document_name: str
    text: str
    start_char: int
    end_char: int
    length: int
    embedding: list[float] | None = None