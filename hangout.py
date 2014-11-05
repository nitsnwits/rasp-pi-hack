#Main rasp pi hack file

import RPi.GPIO as GPIO
import time
import picamera
import webbrowser
import uuid
from twilio.rest import TwilioRestClient
from time import gmtime, strftime
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.connection import Location

#uncomment to start python debugger
#import pdb
#pdb.set_trace()

#AWS access keys (keep these as secret, only running on pi)
conn = S3Connection('<aws access key>', '<aws secret key>')
bucket = conn.create_bucket('bellpi', location=Location.USWest)

logFile = open('/tmp/rasp-pi.log', 'a')

#set up button channel on 18th pin of rasp pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#twilio client parameters
ACCOUNT_SID = "ACfd2e91815e26d4c1c74ba6d98dd76feb" 
AUTH_TOKEN = "26d9170ee5cfb77df65f3f2128a321d2" 

receiver = "+18476447988"
caller = "+12244124335"
url = "http://sugarmtnfarm.com/blog/uploaded_images/FrogTinyFingersDSCF6544-760238.jpg" #this will be taken as default
body = "Look who showed up"

def generateUUID():
    return str(uuid.uuid4());

def makeCall(receiver, caller, message, url):
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	call = client.messages.create(
		to=receiver, 
		from_=caller, 
		body=message, 
		media_url=url
	)
	return call.sid

if __name__ == '__main__':

	#start polling the button
	while True:
		#time.sleep(2) #2 seconds to check for a new detection, reduced cpu usage
		input_state = GPIO.input(18)
		if input_state == False:
			print "Detected button press. Setting up call."
			#click a picture of the caller
			with picamera.PiCamera() as camera:
				camera.start_preview()
				time.sleep(1)
				camera.capture('/tmp/caller.jpg')
				camera.stop_preview()
			#upload  picture to s3 and set the caller url
			photo = Key(bucket)
			photo.key = generateUUID()
			photo.set_contents_from_filename('/tmp/caller.jpg')
			url = photo.generate_url(expires_in=300)

			#make the call to caller and log the call
			call = makeCall(receiver, caller, body, url)
			now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			logFile.write("Made a call at " + str(now) + " to " + str(call) + "\n")
			time.sleep(10) #relax pi for a bit, avoid multiple retries


# working client call
# client.messages.create(
# to="8476447988", 
# from_="+12244124335", 
# body="Look who showed up", 
# media_url="http://sugarmtnfarm.com/blog/uploaded_images/FrogTinyFingersDSCF6544-760238.jpg", 
# )