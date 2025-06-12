from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

HARG_RESPONSES = [
    "I demand breakfast.",
    "I'm napping. Respect that.",
    "Didion is at the plant again."
]

DIDION_RESPONSES = [
    "I meowed into the void.",
    "Please do not look at me.",
    "Hargrove knocked over the mug. Again."
]

@app.route("/hargrove", methods=["POST"])
def hargrove():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(random.choice(HARG_RESPONSES))
    return str(resp)

@app.route("/didion", methods=["POST"])
def didion():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(random.choice(DIDION_RESPONSES))
    return str(resp)

@app.route("/", methods=["GET"])
def home():
    return "The cats are listening."
