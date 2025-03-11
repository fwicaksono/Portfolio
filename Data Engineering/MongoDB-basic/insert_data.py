from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # Connect to local MongoDB
db = client["customer_feedback"]
collection = db["feedbacks"]

# Sample Data
feedback_data = [
    {"customer_name": "Alice", "rating": 4, "feedback": "Great service!", "date": "2025-03-10"},
    {"customer_name": "Bob", "rating": 2, "feedback": "Delivery was late.", "date": "2025-03-09"},
    {"customer_name": "Charlie", "rating": 5, "feedback": "Amazing experience!", "date": "2025-03-08"}
]

# Insert Data
collection.insert_many(feedback_data)
print("Data inserted successfully!")
