from pymongo import MongoClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def load_from_mongo(uri, db_name, collection_name):
    """Load meeting notes from MongoDB."""
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]

    documents = []
    for doc in collection.find():
        doc_content = f"""
        Title: {doc.get('title', 'N/A')}
        Date: {doc.get('date', 'N/A')}
        Location: {doc.get('location', 'N/A')}
        Time: {doc.get('time', 'N/A')}
        Attendees: {', '.join(doc.get('attendees', []))}
        Content: {doc.get('content', 'No content available')}
        """.strip()

        documents.append(
            Document(
                page_content=doc_content,
                metadata={
                    "title": doc.get("title", "Unknown"),
                    "date": doc.get("date", "Unknown"),
                    "location": doc.get("location", "Unknown"),
                    "time": doc.get("time", "Unknown"),
                    "attendees": doc.get("attendees", [])
                }
            )
        )

    # Split documents into chunks for vectorization
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    return texts
