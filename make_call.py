import os
from lxml import etree
from twilio.rest import Client

# twiml = etree.parse("twiml_instructions.xml")
# print(etree.tostring(twiml.getroot()))

# twiml_example = r"""<?xml version="1.0" encoding="UTF-8"?>
# <Response>
#     <Record maxlength/>
#     <Say>Test attempt!</Say>
#     <Pause length="8"/>
#     <Say>Goodbye</Say>
#     <Hangup/>
# </Response>"""

twiml_rogers_example = r"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pause length="6"/>
    <Play digits="2"></Play>
    <Pause length="5"/>
    <Hangup/>
</Response>"""


account_sid = os.environ.get('Twilio_Account_SID')
auth_token = os.environ.get('Twilio_Auth_Token')
client = Client(account_sid, auth_token)

call = client.calls.create(
                        record=True,
                        recording_track='both',
                        twiml=twiml_rogers_example,
                        to='+18887643771',
                        from_='+16477241267'
                    )

print("Call made successfully.")


