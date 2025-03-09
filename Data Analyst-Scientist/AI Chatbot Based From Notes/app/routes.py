from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from . import db
from .models import Note
from .embeddings import get_embedding
from .faiss_index import FaissIndex
from .chatbot import Chatbot

# Create a Blueprint for the routes
bp = Blueprint('main', __name__)

# Initialize FAISS and Chatbot
faiss_index = FaissIndex()
chatbot = Chatbot()

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        content = request.form['content']
        new_note = Note(content=content)
        db.session.add(new_note)
        db.session.commit()

        # Generate embedding and store in FAISS
        embedding = get_embedding(content)
        faiss_index.add_embedding(embedding)

    notes = Note.query.all()
    return render_template('notes.html', notes=notes)

@bp.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user-input']
        response = chatbot.respond(user_input)
        return jsonify({'response': response})
    return render_template('chat.html')
