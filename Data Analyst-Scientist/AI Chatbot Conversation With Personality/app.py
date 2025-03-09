import streamlit as st
from src.load_data import load_pdfs
from src.embeddings import get_vertex_embeddings
from src.chatbot import Chatbot
from langchain_community.vectorstores import FAISS

# Custom CSS for light theme and Apple-style UI with widened layout
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f7;
        color: #333;
        font-family: -apple-system, BlinkMacSystemFont, 'San Francisco', Arial, sans-serif;
    }
    .main-container {
        max-width: 80%;
        margin: auto;
    }
    .stChatMessage {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
        transition: all 0.3s ease-in-out;
        width: 100%;
    }
    .stChatMessage-user {
        background-color: #007aff;
        color: white;
        text-align: right;
        transform: scale(1);
    }
    .stChatMessage-user:hover {
        transform: scale(1.05);
    }
    .stChatMessage-assistant {
        background-color: #e5e5ea;
        color: black;
        transform: scale(1);
    }
    .stChatMessage-assistant:hover {
        transform: scale(1.05);
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .fadeIn {
        animation: fadeIn 0.5s ease-out;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load credentials and data
credentials_path = "credentials/gcp-credentials.json"
pdf_folder = "data/knowledge.pdf"

# Load PDFs and create embeddings
texts = load_pdfs(pdf_folder)
embeddings = get_vertex_embeddings(credentials_path)
vectorstore = FAISS.from_documents(texts, embeddings)

# Initialize chatbot
chatbot = Chatbot(vectorstore.as_retriever(), personality="friendly and helpful")

# Streamlit UI
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("Welcome to NusantaraNotes")
st.write("Ask me anything! About the your meeting")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with animation
for message in st.session_state.messages:
    css_class = "stChatMessage-user" if message["role"] == "user" else "stChatMessage-assistant"
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="stChatMessage {css_class} fadeIn">{message["content"]}</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("What would you like to ask?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f'<div class="stChatMessage stChatMessage-user fadeIn">{prompt}</div>', unsafe_allow_html=True)
    
    # Generate AI response
    with st.chat_message("assistant"):
        response = chatbot.chat(prompt)
        st.markdown(f'<div class="stChatMessage stChatMessage-assistant fadeIn">{response}</div>', unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown('</div>', unsafe_allow_html=True)