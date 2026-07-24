# Configurations File used for storing important values

from pathlib import Path

# PDF Upload Directory
UPLOAD_DIR = Path("uploads")

# Chunking
CHUNK_SIZE = 500
OVERLAP = 100

# Embedding Model Name
MODEL_NAME = "all-MiniLM-L6-v2"

# Embedding Dimension
EMBEDDING_DIMENSION = 384