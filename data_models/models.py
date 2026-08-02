from pydantic import BaseModel, Field


# Data Model for Chunks, used in chunking and to store vector embeddings of each chunk
class Chunk(BaseModel):
    chunk_id: str
    document_name: str
    text: str
    start_char: int
    end_char: int
    pages: list[int] | None = Field(default_factory=list)
    length: int
    embedding: list[float] | None = None


# Data Model for Page Information, used in allocating page number to a Chunk
class PageInfo(BaseModel):
    page_number: int
    start_char: int
    end_char: int


# Data Model for Sources, used in retrieval to pass source information of a answer to the frontend
class SourceReference(BaseModel):
    document_name: str
    chunk_id: str
    pages: list[int] | None
    similarity_score: float
    text: str


# Data Model for retrieved results
class RetrievalResult(BaseModel):
    query: str
    total_results: int
    sources: list[SourceReference]


# Data Model for LLM Answer
class AnswerResponse(BaseModel):
    answer: str
    sources: list[SourceReference] | None