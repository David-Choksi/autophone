rogers_example = r"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Pause length="6"/>
            <Play digits="2"></Play>
            <Pause length="5"/>
            <Hangup/>
        </Response>"""

demo_business_hours = r"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Pause length="15"/>
            <Play digits="1"></Play>
            <Pause length="25"/>
        </Response>"""

demo_account_info = r"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Pause length="15"/>
            <Play digits="2"></Play>
            <Pause length="15"/>
            <Play digits="12345"></Play>
        </Response>"""

demo_service_team = r"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Pause length="15"/>
            <Play digits="3"></Play>
            <Pause length="10"/>
            <Play digits="1"></Play>
            <Pause length="1"/>
            <Play digits="2"></Play>
            <Pause length="15"/>
            <Hangup/>
        </Response>"""

demo_banking_team = r"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Pause length="15"/>
            <Play digits="3"></Play>
            <Pause length="10"/>
            <Play digits="2"></Play>
            <Pause length="1"/>
            <Play digits="2"></Play>
            <Pause length="15"/>
            <Hangup/>
        </Response>"""

demo_gaming_team = r"""<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Pause length="15"/>
            <Play digits="3"></Play>
            <Pause length="10"/>
            <Play digits="3"></Play>
            <Pause length="1"/>
            <Play digits="3"></Play>
            <Pause length="15"/>
            <Hangup/>
        </Response>"""


shell_intro = r"""

=========================================
 __      __   _                  _
 \ \    / /__| |__ ___ _ __  ___| |
  \ \/\/ / -_) / _/ _ \ '  \/ -_)_|
   \_/\_/\___|_\__\___/_|_|_\___(_)

=========================================

                """