from pydantic import BaseModel, Field

class Chunk(BaseModel):
    chunk_id: str
    document_name: str
    text: str
    start_char: int
    end_char: int
    pages: list[int] | None = Field(default_factory=list)
    length: int
    embedding: list[float] | None = None



class PageInfo(BaseModel):
    page_number: int
    start_char: int
    end_char: int