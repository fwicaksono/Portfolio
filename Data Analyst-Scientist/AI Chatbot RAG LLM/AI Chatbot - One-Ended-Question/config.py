import os
from google.cloud import aiplatform

# Load GCP Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "llm-chatbot-453104-b874676ba300.json"

# GCP Project & Model Info
PROJECT_ID = "llm-chatbot-453104"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.0-flash-001"  # Example for Vertex AI PaLM
