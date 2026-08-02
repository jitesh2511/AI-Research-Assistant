from backend.services.embeddings import embed
from backend.services.vector_store import vectorStore
from config import K_NEAREST_EMBEDDINGS
from data_models.models import SourceReference, RetrievalResult
import numpy as np
import logging

logger = logging.getLogger(__name__)

def search_query(query: str) -> RetrievalResult:

    embedding = np.asarray(embed(query), dtype=np.float32).reshape(1, -1)
    distances, indices = vectorStore.index.search(embedding, K_NEAREST_EMBEDDINGS)
    sources = []

    for i in range(K_NEAREST_EMBEDDINGS):
        chunk = vectorStore.chunk_lookup[indices[0][i]]
        distance = distances[0][i]

        sources.append(SourceReference(
            document_name=chunk.document_name,
            chunk_id=chunk.chunk_id,
            pages=chunk.pages,
            similarity_score=float(distance),
            text=chunk.text
        ))

    logger.info("search successfull, returning results")

    return RetrievalResult(
        query=query,
        total_results=len(sources),
        sources=sources
    )