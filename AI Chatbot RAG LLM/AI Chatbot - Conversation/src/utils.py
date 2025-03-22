import os

def get_credentials_path():
    return os.path.join("credentials", "gcp-credentials.json")

def get_pdf_path():
    return os.path.join("data", "langsa.pdf")

def get_index_path():
    return os.path.join("embeddings", "faiss_index.index")

def get_text_path():
    return os.path.join("embeddings", "text_chunks.json")