from data_models.chunk import Chunk
from sentence_transformers import SentenceTransformer
from config import MODEL_NAME, EMBEDDING_DIMENSION
import logging

logger = logging.getLogger(__name__)

model = SentenceTransformer(MODEL_NAME)
logger.info(f"successfully loaded embedding model : {MODEL_NAME}")

def generate_embeddings(chunks: list[Chunk]) -> dict:

    dimension_check = True
    n = 0
    for chunk in chunks:
        this_embedding = embed(chunk.text)
        chunk.embedding = this_embedding
        n += 1
        if (len(this_embedding) != EMBEDDING_DIMENSION):
            dimension_check = False
            logger.warning("specified embedding dimension did not match generated embedding dimension")

    logger.info(f"generated {n} embeddings")
    return {
        "n_embeddings" : n,
        "chunks": chunks,
        "embedding_status": "success" if dimension_check else "wrong dimensions reported"
    }

def embed(query:str) -> list[float]:

    return model.encode(query, show_progress_bar=False).tolist()