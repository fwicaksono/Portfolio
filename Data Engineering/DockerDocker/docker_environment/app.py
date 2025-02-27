import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Ambil environment variable "APP_NAME"
    app_name = os.getenv("APP_NAME", "Default App")
    return f"Hello, Docker! This is {app_name}."

if __name__ == "__main__":
    # Ambil port dari environment variable atau default ke 5000
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
