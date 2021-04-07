# Download the helper library from https://www.twilio.com/docs/python/install
import os
import time
from twilio.rest import Client
from twilio.twiml.voice_response import Pause, VoiceResponse, Say, Conference, Dial

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

twiml_rogers = r"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial hangupOnStar="true">
        <Conference startConferenceOnEnter="true" endConferenceOnExit="true" beep="false">Conference-Bitch</Conference>
    </Dial>   
    <Pause length="6"/>
    <Gather action="/redirectIntoConference?name=Conference-Bitch" numDigits="1"></Gather>
    <Play digits="2"></Play>
    <Pause length="8"/>
</Response>"""

twiml_participant = r"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial>
        <Conference startConferenceOnEnter="true" endConferenceOnExit="true" beep="false">Conference-Bitch</Conference>
    </Dial>
</Response>"""

response = VoiceResponse()
dial = Dial()
dial.conference('Conference-Bitch', start_conference_on_enter=True, end_conference_on_exit=True, beep=False)

call = client.calls.create(record=True, recording_track='both', twiml=twiml_participant, to='+16478843125', from_='+16477241267')
#call2 = client.calls.create(record=True, recording_track='both', twiml=twiml_participant, to='+16476314917', from_='+16477241267')
time.sleep(7)
call_rogers = client.calls.create(record=True, recording_track='both', twiml=twiml_rogers, to='+18887643771', from_='+16477241267')

print(response)

# ------------------------------
# participant2 = client.conferences('Conference-Bitch') \
#                     .participants.create(from_='+16477241267', to='+14168224547', end_conference_on_exit='true') 
# participant3 = client.conferences('Conference-Bitch') \
#                     .participants.create(from_='+16477241267', to='+18887643771')
# print(participant2.call_sid)
# print(participant3.call_sid)