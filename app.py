from flask import Flask, request
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

app = Flask(__name__)

# Twilio setup
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
messaging_service_sid = os.environ.get("MESSAGING_SERVICE_SID")
client = Client(account_sid, auth_token)

@app.route("/")
def home():
    return "Cat bot is running!"

@app.route("/test")
def send_test_messages():
    recipient = "+13193892071"

    client.messages.create(
        to=recipient,
        messaging_service_sid=messaging_service_sid,
        body="i ate a sock. it was crunchy - hargs"
    )

    client.messages.create(
        to=recipient,
        messaging_service_sid=messaging_service_sid,
        body="she ate a sock. i cried - dids"
    )

    return "Test messages sent!"
