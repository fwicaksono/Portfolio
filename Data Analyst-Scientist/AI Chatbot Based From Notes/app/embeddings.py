from google.cloud import aiplatform
from vertexai.language_models import TextEmbeddingModel
import os

# Set the path to your GCP credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-credentials.json"

# Initialize Vertex AI
aiplatform.init(project="llm-chatbot-453104", location="us-central1")

def get_embedding(text):
    """
    Generate embeddings for the given text using Vertex AI's TextEmbeddingModel.
    """
    # Initialize the TextEmbeddingModel
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko-multilingual@001")

    # Generate embeddings
    embeddings = model.get_embeddings([text])
    
    # Return the embedding values
    return embeddings[0].values