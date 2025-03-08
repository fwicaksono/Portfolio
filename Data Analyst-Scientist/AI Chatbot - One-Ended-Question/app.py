import streamlit as st
from pdf_processor import extract_text_from_pdfs
from vectorstore import create_faiss_vectorstore
from chatbot import chatbot_response

# Load PDFs and create FAISS database
texts = extract_text_from_pdfs()
vectorstore = create_faiss_vectorstore(texts)

# Streamlit UI
st.title("Chatbot by Wicaksono")
st.markdown("### ask a question")

query = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if query:
        response = chatbot_response(query, vectorstore)
        st.write(response)
    else:
        st.warning("Please enter a question.")
