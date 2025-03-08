import faiss
import numpy as np
from langchain_google_vertexai import VertexAIEmbeddings  # ✅ Use new import
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Set the path to your Google Cloud credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "llm-chatbot-453104-b874676ba300.json"

# Set GCP Project
PROJECT_ID = "llm-chatbot-453104"
LOCATION = "us-central1"
MODEL_NAME = "text-multilingual-embedding-002"  # model embedding

os.environ["GOOGLE_CLOUD_PROJECT"] = PROJECT_ID

def create_faiss_vectorstore(texts):
    """Create and return FAISS vector database using Vertex AI embeddings."""
    embeddings = VertexAIEmbeddings(
        model_name=MODEL_NAME,  # ✅ Specify model
        project=PROJECT_ID,
        location=LOCATION
    )

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.create_documents(texts)
    
    # Create FAISS index
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore

def query_faiss(vectorstore, query):
    """Query FAISS for the most relevant document chunks."""
    docs = vectorstore.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])
