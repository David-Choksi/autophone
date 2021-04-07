import os
from cmd import Cmd
from collections import defaultdict
from lxml import etree
from twilio.rest import Client
import twiml

class DishViewer(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.account_sid = 'AC1b5c5057ecf8a64542372f6fae83c02e'
        self.auth_token = 'dde1e1152ab937e5dfd13fe4fba401f1'
        self.client = Client(self.account_sid, self.auth_token)
        self.prompt = "\33[92m (autophone) > \033[0m"
        self.intro = twiml.shell_intro

    def do_callRogers(self, line):
        self.call_rogers()

    def do_businessHours(self, line):
        self.business_hours()

    def do_accountInfo(self, line):
        self.account_info()
    
    def do_teamChoice(self, line):
        self.team_choice(line)

    def emptyline(self):
        print("")

    def do_exit(self, line):
        print("See you later!")
        raise SystemExit

# ------------ HELPER ----------------- #

    def call_rogers(self):
        call = self.client.calls.create(
                record=True,
                recording_track='both',
                twiml=twiml.rogers_example,
                to='+18887643771',
                from_='+16477241267'
            )

    def business_hours(self):
        call = self.client.calls.create(
                record=True,
                recording_track='both',
                twiml=twiml.demo_business_hours,
                to='+16477241267',
                from_='+16472497553'
            )

    def account_info(self):
        call = self.client.calls.create(
                record=True,
                recording_track='both',
                twiml=twiml.demo_account_info,
                to='+16477241267',
                from_='+16472497553'
            )

    def team_choice(self, line: str):
        twiml_payload = r""" """
        if line == "service":
            twiml_payload = twiml.demo_service_team
        if line == "banking":
            twiml_payload = twiml.demo_banking_team
        if line == "gaming":
            twiml_payload = twiml.demo_gaming_team
        else:
            print("Please specify teamChoice <service/banking/gaming>")
            return

        call = self.client.calls.create(
                record=True,
                recording_track='both',
                twiml=twiml_payload,
                to='+16477241267',
                from_='+16472497553'
            )


if __name__ == "__main__":
    DishViewer().cmdloop()
