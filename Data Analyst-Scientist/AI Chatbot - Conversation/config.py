import os
from google.cloud import aiplatform
from google.oauth2 import service_account


# Load GCP Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "llm-chatbot-453104-b874676ba300.json"

GCP_CREDENTIALS = service_account.Credentials.from_service_account_file("llm-chatbot-453104-b874676ba300.json")

# GCP Project & Model Info
PROJECT_ID = "llm-chatbot-453104"
LOCATION = "asia-southeast2"
MODEL_NAME = "gemini-2.0-flash-001"  # Example for Vertex AI PaLM

# Embedding Model
EMBEDDING_MODEL = "text-multilingual-embedding-002"
CHAT_MODEL = "gemini-1.0-pro"
