import streamlit as st
from streamlit_option_menu import option_menu
from src.load_data import load_from_mongo
from src.embeddings import get_vertex_embeddings
from src.chatbot import Chatbot
from langchain_community.vectorstores import FAISS
from pymongo import MongoClient
import time

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "nusantara_notes"
COLLECTION_NAME = "meetings"

# Load meeting notes and create embeddings
texts = load_from_mongo(MONGO_URI, DB_NAME, COLLECTION_NAME)
credentials_path = "credentials/gcp-credentials.json"
embeddings = get_vertex_embeddings(credentials_path)
vectorstore = FAISS.from_documents(texts, embeddings)

# Initialize chatbot
chatbot = Chatbot(vectorstore.as_retriever(), personality="friendly and helpful")

# Streamlit Page Setup
st.set_page_config(page_title="NusantaraNotes", layout="wide")

# Sidebar Navigation (Simplified)
with st.sidebar:
    selected = option_menu(
        menu_title="NusantaraNotes",
        options=["Chatbot AI", "Notes Overview", "Add Note"],
        icons=["chat-dots", "list-task", "plus-square"],
        menu_icon="menu-button-wide",
        default_index=0,
        styles={
            "container": {"background-color": "#f8f9fa", "padding": "5px"},
            "icon": {"color": "#007aff"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "5px"},
            "nav-link-selected": {"background-color": "#007aff", "color": "white"},
        }
    )

# Chatbot Page
if selected == "Chatbot AI":
    st.title("🤖 Nusantara AI Chatbot")
    st.write("Ask me anything about your meetings!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Type your question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            response = chatbot.chat(prompt)
            st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

# Notes Overview Page
elif selected == "Notes Overview":
    st.title("📜 Meeting Notes Overview")

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    notes = list(collection.find())

    for note in notes:
        with st.expander(f"📌 {note['title']} - {note['date']}"):
            st.write(f"**Location:** {note['location']}")
            st.write(f"**Time:** {note['time']}")
            st.write(f"**Attendees:** {', '.join(note['attendees'])}")
            st.write(f"**Content:** {note['content']}")

            col1, col2 = st.columns([1, 1])

            if col1.button("✏️ Edit", key=f"edit_{note['_id']}"):
                new_content = st.text_area("Edit Note", value=note['content'])
                if st.button("Save Changes", key=f"save_{note['_id']}"):
                    collection.update_one({"_id": note['_id']}, {"$set": {"content": new_content}})
                    st.success("Note Updated Successfully!")
                    time.sleep(1)
                    st.rerun()

            if col2.button("🗑️ Delete", key=f"delete_{note['_id']}"):
                collection.delete_one({"_id": note['_id']})
                st.error("Note Deleted Successfully!")
                time.sleep(1)
                st.rerun()

# Add Note Page (Fixed Input Field Refresh Issue)
elif selected == "Add Note":
    st.title("📝 Add New Meeting Note")

    with st.form("add_note_form", clear_on_submit=True):
        title = st.text_input("Title")
        date = st.date_input("Date")
        location = st.text_input("Location")
        time_range = st.text_input("Time")
        attendees = st.text_area("Attendees (comma separated)")
        content = st.text_area("Content")
        submitted = st.form_submit_button("Add Note")

        if submitted:
            if title and date and location and time_range and attendees and content:
                new_note = {
                    "title": title,
                    "date": str(date),
                    "location": location,
                    "time": time_range,
                    "attendees": [att.strip() for att in attendees.split(",")],
                    "content": content
                }
                collection = MongoClient(MONGO_URI)[DB_NAME][COLLECTION_NAME]
                collection.insert_one(new_note)
                st.success("Note Added Successfully!")
                time.sleep(1)
                st.rerun()
            else:
                st.warning("Please fill in all fields!")

# Custom CSS Animation & Style (Refined)
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stChatMessage {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        transition: all 0.2s ease-in-out;
        width: 100%;
    }
    .stChatMessage-user {
        background-color: #007aff;
        color: white;
        text-align: right;
    }
    .stChatMessage-assistant {
        background-color: #f1f1f1;
        color: black;
    }
    .st-expander-header {
        font-weight: bold;
        color: #007aff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
