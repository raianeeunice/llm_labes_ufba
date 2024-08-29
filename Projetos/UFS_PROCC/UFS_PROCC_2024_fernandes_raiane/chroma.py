import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import os

dirname = os.path.dirname(__file__)

chroma_client = chromadb.PersistentClient(path=os.path.join(dirname, "./db"))

huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key="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",
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
