from backend.services.embeddings import embed
from backend.services.vector_store import vectorStore
from config import K
import numpy as np
import logging

logger = logging.getLogger(__name__)

def search_query(query: str) -> list[dict]:

    embedding = np.asarray(embed(query), dtype=np.float32).reshape(1, -1)
    distances, indices = vectorStore.index.search(embedding, K)
    results = []

    for i in range(K):
        chunk = vectorStore.chunk_lookup[indices[0][i]]
        distance = distances[0][i]
        results.append({
            "chunk_id": chunk.chunk_id,
            "document_name": chunk.document_name,
            "pages": chunk.pages,
            "distance": float(distance),
            "text": chunk.text
        })

    logger.info("search successfull, returning results")

    return results