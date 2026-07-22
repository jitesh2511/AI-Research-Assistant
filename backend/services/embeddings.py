from data_models.chunk import Chunk
from sentence_transformers import SentenceTransformer
from config import MODEL_NAME

model = SentenceTransformer(MODEL_NAME)

def generate_embeddings(chunks: list[Chunk]) -> dict:

    texts = [chunk.text for chunk in chunks]
    embeddings = model.encode(texts)
    dimension_check = True
    for chunk, embedding in zip(chunks, embeddings):
        chunk.embedding = embedding.tolist()
        if (len(embedding.tolist()) != 384):
            dimension_check = False

    return {
        "n_embeddings" : len(embeddings),
        "chunks": chunks,
        "embedding_status": "success" if dimension_check else "wrong dimensions reported"
    }