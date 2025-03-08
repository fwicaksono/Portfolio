import os
from PyPDF2 import PdfReader

def extract_text_from_pdfs(pdf_folder="data/"):
    """Extract text from all PDFs in the given folder."""
    text_data = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            reader = PdfReader(pdf_path)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            text_data.append(text)
    return text_data
