# NusantaraNotes

NusantaraNotes is a web-based notes application powered by Streamlit, MongoDB, FAISS, and Google Vertex AI. It allows users to store and retrieve meeting notes while providing an AI-powered chatbot to extract insights from stored notes.

## Features

### 📝 Notes Management
- **Add Notes**: Users can create new meeting notes, specifying the title, date, location, time, attendees, and content.
- **View Notes**: Users can browse and expand saved notes to see details.
- **Edit & Delete Notes**: Notes can be modified or deleted as needed.

### 🤖 AI-Powered Chatbot
- **Intelligent Retrieval**: Users can interact with the chatbot to extract information from stored meeting notes.
- **FAISS Vector Search**: Notes are embedded and stored in FAISS to provide efficient semantic search.
- **Google Vertex AI Integration**: Uses `textembedding-gecko` for generating embeddings from text data.

### 🛠️ Tech Stack
- **Frontend & UI**: Streamlit
- **Database**: MongoDB
- **Vector Database**: FAISS
- **AI & Embeddings**: Google Vertex AI
- **Backend & Processing**: Python, LangChain

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- MongoDB
- Google Cloud Service Account credentials
- Docker (optional for deployment)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/NusantaraNotes.git
   cd NusantaraNotes
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start MongoDB (if not already running):
   ```bash
   mongod --dbpath /path/to/mongodb/data
   ```

5. Set up Google Cloud credentials:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
   ```

6. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
- Open `http://localhost:8501` in your browser.
- Navigate between **Chatbot AI**, **Notes Overview**, and **Add Note** using the sidebar.
- Use the chatbot to query notes intelligently.

## Future Improvements
- [ ] Deploy on Google Cloud Run
- [ ] Implement authentication for secure access
- [ ] Enhance chatbot responses with advanced LLMs

## Contributing
Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License.

