import faiss
import numpy as np
import json
from src.generate_embeddings import get_vertex_embedding

def load_faiss_index(index_path):
    return faiss.read_index(index_path)

def load_text_chunks(text_path):
    with open(text_path, "r", encoding="utf-8") as f:
        return json.load(f)

def query_index(query, index, text_chunks, credentials_path, k=5):
    query_embedding = get_vertex_embedding(query, credentials_path)
    query_embedding = np.array([query_embedding]).astype("float32")
    
    distances, indices = index.search(query_embedding, k)
    return distances, indices

def chatbot(credentials_path, index_path, text_path):
    index = load_faiss_index(index_path)
    text_chunks = load_text_chunks(text_path)
    
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        
        distances, indices = query_index(query, index, text_chunks, credentials_path)
        
        # Find the index of the result with the smallest distance
        closest_index = indices[0][0]  # First result is the closest
        closest_distance = distances[0][0]
        closest_text = text_chunks[closest_index]
        
        # Display only the closest result
        print(f"Bot: Closest result (Distance: {closest_distance}):")
        print(f"Text: {closest_text}\n")