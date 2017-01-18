#       RemindMe Alexa Skill
####################################
#   "Alexa, remind me to do XXXX"
#  Alexa will then text you XXXX
#
# copywrite David Ricaud 2017

import logging
from twilio.rest import TwilioRestClient
from flask import Flask, render_tmplate
from flask_ask import Ask, statement, question, session

#setting up Flask server
app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#setting up Twilio client
account_sid = "Enter you sid here"
auth_token = "Your authentication token here"
twilio_num = "your twilio number here"
phone_num = "destination number here"

client = TwilioRestClient(account_sid, auth_token)

#acutal application
@ask.launch
def send_message()
