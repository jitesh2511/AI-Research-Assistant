# Configurations File used for storing important values

import os
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()

# PDF Upload Directory
UPLOAD_DIR = Path("uploads")

# Chunking
CHUNK_SIZE = 500
OVERLAP = 100

# Embedding Model Name
MODEL_NAME = "all-MiniLM-L6-v2"

# Embedding Dimension
EMBEDDING_DIMENSION = 384

# K-Nearest Embeddings
K_NEAREST_EMBEDDINGS = 3

# Logging Directory
LOGGING_DIR = Path("logs")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Models
GEMINI_MODEL = os.getenv("GEMINI_MODEL")