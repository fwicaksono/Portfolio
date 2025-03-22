import faiss
import numpy as np
import json
from src.load_pdf import load_pdf
from src.generate_embeddings import get_vertex_embedding

def build_faiss_index(pdf_path, credentials_path, index_save_path, text_save_path):
    texts = load_pdf(pdf_path)
    
    # Generate embeddings
    embeddings = []
    text_chunks = []
    for text in texts:
        embedding = get_vertex_embedding(text.page_content, credentials_path)
        embeddings.append(embedding)
        text_chunks.append(text.page_content)  # Store the text chunk
    
    embeddings = np.array(embeddings).astype("float32")
    
    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # Save index
    faiss.write_index(index, index_save_path)
    
    # Save text chunks to a JSON file
    with open(text_save_path, "w", encoding="utf-8") as f:
        json.dump(text_chunks, f)
    
    print(f"FAISS index saved to {index_save_path}")
    print(f"Text chunks saved to {text_save_path}")