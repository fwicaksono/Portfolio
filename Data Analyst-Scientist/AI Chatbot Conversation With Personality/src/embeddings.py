from langchain_google_vertexai import VertexAIEmbeddings
from google.oauth2 import service_account

def get_vertex_embeddings(credentials_path):
    """Initialize Vertex AI embeddings."""
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    
    # Specify the model name explicitly
    embeddings = VertexAIEmbeddings(
        credentials=credentials,
        model_name="textembedding-gecko"  # Use the correct model name
    )
    return embeddings