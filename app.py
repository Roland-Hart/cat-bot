from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Cat bot is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port)
