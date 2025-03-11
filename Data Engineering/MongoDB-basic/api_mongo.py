from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["customer_feedback"]
collection = db["feedbacks"]

# Get All Feedbacks
@app.route("/feedbacks", methods=["GET"])
def get_feedbacks():
    feedbacks = list(collection.find({}, {"_id": 0}))  # Exclude _id field
    return jsonify(feedbacks)

# Add New Feedback
@app.route("/feedbacks", methods=["POST"])
def add_feedback():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Feedback added!"})

if __name__ == "__main__":
    app.run(debug=True)
