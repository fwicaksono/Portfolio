# Import yang benar
from langchain_google_vertexai import VertexAI  # Ganti dengan library yang mendukung model_rebuild()
from config import PROJECT_ID, LOCATION, MODEL_NAME
from vectorstore import query_faiss

# Panggil model_rebuild sebelum inisialisasi
VertexAI.model_rebuild()

# Initialize Vertex AI Model
def get_llm_response(prompt):
    """Generate response using GCP Vertex AI LLM."""
    llm = VertexAI(model=MODEL_NAME, project=PROJECT_ID, location=LOCATION)
    return llm.invoke(prompt)  # Gunakan .invoke() jika metode langsung tidak bekerja

def chatbot_response(query, vectorstore):
    """Fetch relevant knowledge and generate an AI response."""
    context = query_faiss(vectorstore, query)
    prompt = f"Based on the following context, answer the user's question:\n\n{context}\n\nQuestion: {query}"
    return get_llm_response(prompt)
