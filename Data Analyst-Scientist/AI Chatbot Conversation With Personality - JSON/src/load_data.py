import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def load_json(json_file):
    """Load and split meeting notes from a JSON file."""
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Combine title, date, and content into a single text entry
    documents = [
        Document(
            page_content=f"Title: {item['title']}\nDate: {item['date']}\nDetails: {item['content']}",
            metadata={"title": item["title"], "date": item["date"]}
        )
        for item in data
    ]

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    return texts
