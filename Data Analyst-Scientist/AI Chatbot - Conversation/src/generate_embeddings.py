from google.cloud import aiplatform
from google.oauth2 import service_account
from config import PROJECT_ID
from vertexai.language_models import TextEmbeddingModel

def get_vertex_embedding(text, credentials_path):
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    aiplatform.init(credentials=credentials, project=PROJECT_ID, location="us-central1")
    
    # Use Vertex AI's text embedding model
    embeddings = TextEmbeddingModel.from_pretrained("textembedding-gecko")
    result = embeddings.get_embeddings([text])
    return result[0].values