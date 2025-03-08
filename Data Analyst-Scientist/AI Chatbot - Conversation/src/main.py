from src.build_faiss_index import build_faiss_index
from src.chatbot import chatbot
from src.utils import get_credentials_path, get_pdf_path, get_index_path, get_text_path

def main():
    credentials_path = get_credentials_path()
    pdf_path = get_pdf_path()
    index_path = get_index_path()
    text_path = get_text_path()
    
    # Build FAISS index (run only once)
    build_faiss_index(pdf_path, credentials_path, index_path, text_path)
    
    # Run chatbot
    chatbot(credentials_path, index_path, text_path)

if __name__ == "__main__":
    main()