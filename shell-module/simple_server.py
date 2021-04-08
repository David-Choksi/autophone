import base64
import json
import logging

from twilio.rest import Client
import twiml

from flask import Flask
app = Flask(__name__)

HTTP_SERVER_PORT = 5000

account_sid = 'SID'
auth_token = 'TOKEN'
client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/call')
def business_hours():
    call = client.calls.create(
            record=True,
            recording_track='both',
            twiml=twiml.demo_business_hours,
            to='+16477241267',
            from_='+16472497553'
        )
    return 'call made successfully'


if __name__ == "__main__":
    app.run(debug=True)
