#Main hangout file

import RPi.GPIO as GPIO
import time
import pdb
import webbrowser
from twilio.rest import TwilioRestClient
#pdb.set_trace()

#set up button channel on 18th pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#setup twilio client
account = "ACxxxsid"
token = "YYYY token"
client = TwilioRestClient(account, token)
receiver = "+1xxxxxxx"
caller = "+1 xxxxxx"
url = "crap"

while True:
	input_state = GPIO.input(18)
	if input_state == False:
		print "Detected button press. Setting up call."
		call = client.calls.create(to=receiver, from_=caller, url=url)
		print call.sid
		times.sleep(100)


