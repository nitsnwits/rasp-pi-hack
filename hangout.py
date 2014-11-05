#Main rasp pi hack file

import RPi.GPIO as GPIO
import time

import webbrowser
from twilio.rest import TwilioRestClient

#uncomment to start python debugger
#import pdb
#pdb.set_trace()

logFile = open('/tmp/rasp-pi.log', 'w')

#set up button channel on 18th pin of rasp pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#twilio client parameters
ACCOUNT_SID = "ACfd2e91815e26d4c1c74ba6d98dd76feb" 
AUTH_TOKEN = "[AuthToken]" 

receiver = "+18476447988"
caller = "+12244124335"
url = "http://sugarmtnfarm.com/blog/uploaded_images/FrogTinyFingersDSCF6544-760238.jpg"

def makeCall(receiver, caller, url):
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	client.messages.create(
		to="8476447988", 
		from_="+12244124335", 
		body="Look who showed up", 
		media_url="http://sugarmtnfarm.com/blog/uploaded_images/FrogTinyFingersDSCF6544-760238.jpg"
	)
	return call.sid

if __name__ == '__main__':

	#start polling the button
	while True:
		time.sleep(2) #2 seconds to check for a new detection, reduced cpu usage
		input_state = GPIO.input(18)
		if input_state == False:
			print "Detected button press. Setting up call."
			call = makeCall
			logFile.write(str(call.sid))
			times.sleep(10) #relax pi for a bit, avoid multiple retries



# working client call
# client.messages.create(
# to="8476447988", 
# from_="+12244124335", 
# body="Look who showed up", 
# media_url="http://sugarmtnfarm.com/blog/uploaded_images/FrogTinyFingersDSCF6544-760238.jpg", 
# )