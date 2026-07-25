from config import EMBEDDING_DIMENSION
from data_models.chunk import Chunk
import numpy as np
import faiss

class VectorStore:
    def __init__(self):
        self.embedding_dimension = EMBEDDING_DIMENSION
        self.index = faiss.IndexFlatL2(self.embedding_dimension)
        self.n_embeddings = 0
        self.chunk_lookup = {}

    def add_chunks(self, chunks: Chunk):
        
        for chunk in chunks:
            embedding = np.asarray(chunk.embedding, dtype=np.float32).reshape(1, -1)
            self.index.add(embedding)
            position = self.index.ntotal - 1
            self.chunk_lookup[position] = chunk
            self.n_embeddings += 1
    
    def stats(self):

        vectors = self.index.ntotal
        ready = True if vectors > 0 and vectors == self.n_embeddings else False
        dimension = EMBEDDING_DIMENSION

        return {
            "ready": ready,
            "vectors": vectors,
            "dimension": dimension
        }

vectorStore = VectorStore()